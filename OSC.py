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