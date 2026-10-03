# Base44 development environment

- This checkout contains two standalone Tk/Turtle desktop scripts, not a web application. `.base44` provides a browser-accessible development desktop using Xvfb, x11vnc, and noVNC on port 3000. No external services or credentials are needed.
- Run `docker compose -f docker-compose.base44.yml up -d --build`. Python/Tk comes from Debian's `/usr/bin/python3`; the base image's `/usr/local/bin/python` does not have Tk installed.
- All editable code is bind-mounted from the checkout. Turtle has no hot-reload mechanism: close and reopen a demo from the launcher after changing its source. Restart the desktop service after changing the launcher or desktop configuration, then reload the preview.
- In the preview, press Connect, then choose a demo. The `key events` file intentionally has no extension and requests numeric input in an xterm before installing its event handlers.
- Original code is unchanged. Known upstream defect: `key events` calls `pen.forward()` without a distance in its Space handler; the movement input is also overwritten by the drawing loop. Do not claim this control works until the user requests a fix.
- Healthchecks verify the X display, the RFB desktop handshake, the launcher window, and the HTTP preview. Check `docker compose -f docker-compose.base44.yml ps` and `curl -fsS http://localhost:3000/`.
- The desktop is development-only and unauthenticated; VNC itself is bound to container localhost and only the web preview is exposed. Do not deploy this configuration as a public production desktop.
- Verification completed: HTTP entry serves noVNC, live preview Connect succeeded, and screenshot showed the launcher. Demo canvas interactions could not be automatically verified because the preview tab became unavailable.
