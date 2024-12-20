# Uptime Notifier

This is a simple uptime notifier that checks every minute how much time has passed since the computer has booted.
If it's more than THRESHOLD (default is 9 hours), it shows a notification.

*Runs only on MacOS.*

Allow python notifications from System Settings. If you run a multi-monitor setup, you might need to check `Allow notifications when mirroring or sharing the display`.

OPTIONAL: Edit the file `com.example.uptime-notifier.plist` to update the `main.py` file's location, 
copy it to `~/Library/LaunchAgents/` and 
run `launchctl load ~/Library/LaunchAgents/com.example.uptime-notifier.plist` to start the service automatically at system boot.