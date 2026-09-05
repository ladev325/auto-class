import time
import subprocess
import os
import json

CHECK_INTERVAL = 5

subjects = None
schedule = None

def update_files():
    global subjects, schedule
    subjects = parse_json("subjects.json")
    schedule = parse_json("schedule.json")["schedule"]

def millis():
    return int(time.perf_counter() * 1000)


def notify(text, timeout_ms, critical=False):
    urgency = "critical" if critical else "normal"
    subprocess.run(["notify-send", "-t", str(timeout_ms), "-u", urgency, text])


def parse_json(name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, name)
    with open(file_path, "r") as file:
        return json.load(file)