#!/usr/bin/env bash
# 启动本地服务器并在浏览器打开档案浏览器。
# 用法: ./serve.sh  (Ctrl-C 停止)
set -e
cd "$(dirname "$0")"
PORT="${1:-8731}"

if [ ! -f data.json ]; then
  echo "data.json 不存在，先生成…"
  python3 build_browser_data.py
fi

echo "在 http://127.0.0.1:${PORT}/index.html 启动浏览器…"
( sleep 1 && open "http://127.0.0.1:${PORT}/index.html" ) &
python3 -m http.server "$PORT" --bind 127.0.0.1
