#!/bin/sh
set -eu
Xvfb :99 -screen 0 1280x800x24 -nolisten tcp &
DISPLAY_PID=$!
trap 'kill "$DISPLAY_PID" 2>/dev/null || true' EXIT
until xdpyinfo -display :99 >/dev/null 2>&1; do sleep 0.2; done
openbox --config-file /app/.base44/openbox.xml &
x11vnc -display :99 -localhost -rfbport 5900 -forever -shared -nopw -quiet &
/usr/bin/python3 /app/.base44/launcher.py &
exec websockify --web /usr/share/novnc 3000 localhost:5900
