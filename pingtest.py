#!/usr/bin/env python3
from ping3 import ping
from datetime import datetime
from time import sleep
from sys import argv

HOST = "google.com"
HIGH_MS = 100
MID_MS = 70
DELAY = 1

NO_COLOR='\033[0m'
RED_BG='\033[7;31;40m'
GREEN='\033[6;32;40m'
YELLOW='\033[6;33;40m'
RED='\033[6;31;40m'

print(f"Pinging {HOST}")

while True:
    latency = ping(HOST, unit='ms')
    now = datetime.now().strftime("%m-%d %H:%M:%S")

    if not latency or latency < 1:
        color = RED_BG
        p = "TIMEOUT"
    elif latency < MID_MS:
        color = GREEN
        p = f"{latency:.0f}ms"
    elif latency < HIGH_MS:
        color = YELLOW
        p = f"{latency:.0f}ms"
    else:
        color = RED
        p = f"{latency:.0f}ms"

    print(f"{color}{now}: {p}{NO_COLOR}")
    sleep(DELAY)

