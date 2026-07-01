#!/usr/bin/env bash
# =====================================================================
# Sustineri Connective Map — headless render pipeline
# Renders an HTML source to a high-res PNG via the pre-installed Chromium.
# Usage: render.sh <input.html> <output.png> <WIDTH> <HEIGHT>
# =====================================================================
set -euo pipefail

CHROME="/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
IN="$1"; OUT="$2"; W="$3"; H="$4"

"$CHROME" \
  --headless --no-sandbox --disable-gpu \
  --hide-scrollbars --force-device-scale-factor=2 \
  --default-background-color=00000000 \
  --window-size="${W},${H}" \
  --screenshot="$OUT" \
  "file://$(cd "$(dirname "$IN")" && pwd)/$(basename "$IN")" >/dev/null 2>&1

echo "rendered -> $OUT (${W}x${H} @2x)"
