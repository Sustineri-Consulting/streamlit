#!/usr/bin/env bash
# Render each map HTML to a 1080x1080 PNG via headless Chromium.
set -e
CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"
mkdir -p exports
for html in maps/*.html; do
  name="$(basename "${html%.html}")"
  "$CHROME" --headless --no-sandbox --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=1 --window-size=1080,1080 \
    --default-background-color=FFFFFFFF \
    --screenshot="exports/${name}.png" "$html" 2>/dev/null
  echo "rendered exports/${name}.png"
done
