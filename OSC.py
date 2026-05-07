import time
from pythonosc import udp_client

# ==================================================
# REAPER CONFIG
# ==================================================

REAPER_IP = "127.0.0.1"
REAPER_PORT = 8001

reaper = udp_client.SimpleUDPClient(REAPER_IP, REAPER_PORT)

# ==================================================
# grandMA3 CONFIG
# ==================================================

GMA3_IP = "127.0.0.1"
GMA3_PORT = 8000
GMA3_ADDR = "/gma3/cmd"

gma3 = udp_client.SimpleUDPClient(GMA3_IP, GMA3_PORT)

# ==================================================
# REAPER FUNCTIONS
# ==================================================

def reaper_play():
    reaper.send_message("/action/1007", 1.0)
    print("REAPER PLAY")

def reaper_stop():
    reaper.send_message("/action/1016", 1.0)
    print("REAPER STOP")

def reaper_jump_marker(marker_number):

    marker_action = {
        1: 40161,
        2: 40162,
        3: 40163
    }

    action_id = marker_action.get(marker_number)

    if action_id:
        reaper.send_message(f"/action/{action_id}", 1.0)
        print(f"REAPER MARKER {marker_number}")

# ==================================================
# grandMA3 FUNCTION
# ==================================================

def gma3_cue(cue_number):

    command = f"Goto Cue {cue_number} Sequence 1"

    gma3.send_message(GMA3_ADDR, command)

    print(f"GMA3 CUE {cue_number}")

# ==================================================
# SHOW BLOCK FUNCTION
# ==================================================

def run_block(marker, start_cue, end_cue, duration):

    total_cues = (end_cue - start_cue) + 1

    # Time gap between each cue
    cue_delay = duration / total_cues

    # ------------------------------
    # REAPER
    # ------------------------------

    reaper_stop()

    time.sleep(0.2)

    reaper_jump_marker(marker)

    time.sleep(0.2)

    reaper_play()

    # ------------------------------
    # grandMA3 cue sequence
    # ------------------------------

    for cue in range(start_cue, end_cue + 1):

        gma3_cue(cue)

        time.sleep(cue_delay)