#!/usr/bin/env python3
"""Scrape r/coolgithubprojects full history via Arctic Shift API."""
import http.client
import json
import os
import sys
import time
import urllib.request
import urllib.error

API = "https://arctic-shift.photon-reddit.com/api/posts/search"
SUB = "coolgithubprojects"
LIMIT = 100
OUT_PATH = os.path.join(os.path.dirname(__file__), "posts.jsonl")
STATE_PATH = os.path.join(os.path.dirname(__file__), ".cursor")
SLEEP_BETWEEN = 0.6
MAX_RETRIES = 5


def load_cursor():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH) as f:
            return int(f.read().strip())
    return 1300000000


def save_cursor(ts):
    with open(STATE_PATH, "w") as f:
        f.write(str(ts))


def fetch(after):
    url = f"{API}?subreddit={SUB}&limit={LIMIT}&sort=asc&after={after}"
    req = urllib.request.Request(url, headers={"User-Agent": "coolgithubprojects-archive/1.0"})
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)["data"]
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError,
                json.JSONDecodeError, http.client.IncompleteRead) as e:
            wait = (attempt + 1) * 2
            print(f"  [retry {attempt + 1}/{MAX_RETRIES}] {e} - sleeping {wait}s", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Failed after {MAX_RETRIES} retries at after={after}")


def main():
    cursor = load_cursor()
    total = 0
    if os.path.exists(OUT_PATH):
        with open(OUT_PATH) as f:
            total = sum(1 for _ in f)
        print(f"Resuming: {total} posts already saved, cursor={cursor}", flush=True)
    else:
        print("Starting fresh scrape", flush=True)

    out = open(OUT_PATH, "a")
    page = 0
    while True:
        page += 1
        posts = fetch(cursor)
        if not posts:
            print(f"Done — empty response at cursor={cursor}", flush=True)
            break

        for p in posts:
            out.write(json.dumps(p, ensure_ascii=False) + "\n")
        out.flush()

        new_cursor = posts[-1]["created_utc"]
        total += len(posts)
        save_cursor(new_cursor)
        import datetime as dt
        date_str = dt.datetime.fromtimestamp(new_cursor, dt.UTC).strftime("%Y-%m-%d")
        print(f"page {page:>4}: +{len(posts):>3} (total {total:>6}) cursor={new_cursor} [{date_str}]", flush=True)

        if len(posts) < LIMIT:
            print(f"Last page received ({len(posts)} < {LIMIT}). Done.", flush=True)
            break

        cursor = new_cursor
        time.sleep(SLEEP_BETWEEN)

    out.close()
    print(f"\nTotal posts saved: {total}", flush=True)


if __name__ == "__main__":
    main()
