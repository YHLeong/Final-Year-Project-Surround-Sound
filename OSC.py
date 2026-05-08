import time
from dataclasses import dataclass
from pythonosc import udp_client

# ==================================================
# CONFIG
# ==================================================

REAPER_IP = "127.0.0.1"
REAPER_PORT = 8001

GMA3_IP = "127.0.0.1"
GMA3_PORT = 8000
GMA3_ADDR = "/gma3/cmd"

MARKER_ACTIONS = {
    1: 40161,
    2: 40162,
    3: 40163,
}

# ==================================================
# OSC CLIENTS
# ==================================================

reaper = udp_client.SimpleUDPClient(REAPER_IP, REAPER_PORT)
gma3 = udp_client.SimpleUDPClient(GMA3_IP, GMA3_PORT)

# ==================================================
# SHOW DATA
# ==================================================

@dataclass
class ShowBlock:
    marker: int
    start_cue: int
    end_cue: int
    duration: float


SHOW = [
    ShowBlock(marker=1, start_cue=1,  end_cue=5,  duration=2),
    ShowBlock(marker=2, start_cue=6,  end_cue=10, duration=2),
    ShowBlock(marker=3, start_cue=11, end_cue=15, duration=5),
]

# ==================================================
# REAPER
# ==================================================

def reaper_play():
    reaper.send_message("/action/1007", 1.0)
    print("REAPER PLAY")


def reaper_stop():
    reaper.send_message("/action/1016", 1.0)
    print("REAPER STOP")


def reaper_jump_marker(marker: int):
    action_id = MARKER_ACTIONS.get(marker)

    if action_id is None:
        raise ValueError(f"Invalid marker: {marker}")

    reaper.send_message(f"/action/{action_id}", 1.0)
    print(f"REAPER MARKER {marker}")

# ==================================================
# grandMA3
# ==================================================

def gma3_cue(cue: int):
    command = f"Goto Cue {cue} Sequence 1"

    gma3.send_message(GMA3_ADDR, command)

    print(f"GMA3 CUE {cue}")

# ==================================================
# SHOW ENGINE
# ==================================================

def prepare_reaper(marker: int):
    reaper_stop()
    time.sleep(0.2)

    reaper_jump_marker(marker)
    time.sleep(0.2)

    reaper_play()


def run_block(block: ShowBlock):
    total_cues = (block.end_cue - block.start_cue) + 1
    cue_delay = block.duration / total_cues

    prepare_reaper(block.marker)

    for cue in range(block.start_cue, block.end_cue + 1):
        gma3_cue(cue)
        time.sleep(cue_delay)

# ==================================================
# MAIN
# ==================================================

def main():
    for index, block in enumerate(SHOW, start=1):
        print(f"\n=== BLOCK {index} ===")

        run_block(block)

    print("\nSHOW COMPLETE")


if __name__ == "__main__":
    main()