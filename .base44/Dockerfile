FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-tk xvfb x11vnc novnc websockify openbox xterm x11-utils curl \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf vnc.html /usr/share/novnc/index.html
WORKDIR /app
