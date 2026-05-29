#!/usr/bin/env bash
# Start a local server and open the archive browser.
# Usage: ./serve.sh  (Ctrl-C to stop)
set -e
cd "$(dirname "$0")"
PORT="${1:-8731}"

if [ ! -f data.json ]; then
  echo "data.json not found, generating it first…"
  python3 build_browser_data.py
fi

echo "Opening browser at http://127.0.0.1:${PORT}/index.html…"
( sleep 1 && open "http://127.0.0.1:${PORT}/index.html" ) &
python3 -m http.server "$PORT" --bind 127.0.0.1
