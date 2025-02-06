#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import subprocess
import re
import platform
import sys

THRESHOLD = 9  # 9 hours
stop_flag = False

if platform.system() != 'Darwin':
    print("This script can only be run on macOS.")
    sys.exit(1)

def notify(title, text):
    global stop_flag
    script = f'''
    display dialog "{text}" with title "{title}" buttons {{"Stop Notifications", "OK"}} default button "OK"
    '''
    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    if "Stop Notifications" in result.stdout:
        stop_flag = True
        return True

def get_uptime_seconds():
    result = subprocess.run(['uptime'], capture_output=True, text=True)
    uptime_str = result.stdout.strip()
    days, hours, minutes = 0, 0, 0

    # Parse the uptime string
    days_match = re.search(r'(\d+) day', uptime_str)
    if days_match:
        days = int(days_match.group(1))

    time_match = re.search(r'up\s+((\d+)\s+days?,\s+)?(\d+):(\d+)', uptime_str)
    if time_match:
        if time_match.group(2):
            days = int(time_match.group(2))
        hours = int(time_match.group(3))
        minutes = int(time_match.group(4))
    else:
        minutes_match = re.search(r'up\s+(\d+)\s+mins?', uptime_str)
        if minutes_match:
            minutes = int(minutes_match.group(1))

    total_seconds = days * 86400 + hours * 3600 + minutes * 60
    return total_seconds

def main():
    global stop_flag
    threshold_hours_in_seconds = THRESHOLD * 60 * 60

    while not stop_flag:
        try:
            uptime_seconds = get_uptime_seconds()
            if uptime_seconds >= threshold_hours_in_seconds:
                hours = int(uptime_seconds // 3600)
                minutes = int((uptime_seconds % 3600) // 60)
                notify("Working hours", f"{hours} hours and {minutes} minutes have passed since the computer started.")
                break
            time.sleep(60)  # Check every minute
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()