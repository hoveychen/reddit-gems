# reddit-gems — r/coolgithubprojects full archive & browser

A complete archive of every post from [r/coolgithubprojects](https://www.reddit.com/r/coolgithubprojects/) across 12 years (2014–2026), plus curated picks and a browser page that renders images and video inline.

**Live site**: https://hoveychen.github.io/reddit-gems/

## What this is

- **25,794** posts fully archived (source: [Arctic Shift](https://arctic-shift.photon-reddit.com/), the successor to Pushshift)
- Deduped and de-spammed down to **14,604** posts, classified into 14 themes
- The browser page embeds images / YouTube / Reddit HLS video / multi-image gallery carousels, with filters by theme, language, year and score, plus search, favorites and infinite scroll
- Bilingual UI (English / 中文) — toggle in the top-right

## Files

| File | Purpose |
|---|---|
| `index.html` | Single-file browser (dark theme, no build step) |
| `data.json` | 14,604 deduped + theme-classified posts (the browser's data source) |
| `serve.sh` | One-command local launch (starts an HTTP server and opens the browser) |
| `scrape.py` | Scrapes all posts from Arctic Shift (resumable) |
| `build_browser_data.py` | `posts.jsonl` → `data.json` (dedupe, classify, extract media links) |
| `build_digest.py` | Generates `top.md` / `by_language.md` / `by_year.md` / `stats.md` |
| `build_clean_top.py` | Generates the de-spammed `top_clean.md` |
| `curated.md` / `curated_clean.md` | Hand-picked themed selections (Chinese, one-line note each) |
| `top.md` / `top_clean.md` | Top 500 by score (raw / deduped) |
| `by_language.md` / `by_year.md` / `stats.md` | By language, by year, overall stats |

> `posts.jsonl` (the 86 MB raw archive) is not committed — run `python3 scrape.py` to regenerate it.

## Run locally

```bash
./serve.sh              # start a server and open the browser
# or pick a port
./serve.sh 8080
```

Must be served over a local HTTP server — opening `file://` directly will fail (`fetch` is blocked by CORS).

## Rebuild the data from scratch

```bash
python3 scrape.py              # scrape everything → posts.jsonl
python3 build_browser_data.py  # → data.json (for the browser)
python3 build_digest.py        # → markdown digests
python3 build_clean_top.py     # → de-spammed Top 500
```

## Known limitations

- **Video / gallery media**: about 87% of videos and 70% of galleries play inline; the rest are older posts where Arctic Shift never captured the `media` field, so they show a thumbnail and link out to Reddit.
- **Expired tokens**: archived v.redd.it video links carry signed tokens; in practice Reddit's CDN does not strictly enforce expiry, so old videos still play — but this is not guaranteed long-term.
- **`data.json` media comes from Reddit's CDN**: the browser page needs network access to load images/video.

## Data source & license

Post metadata comes from the public [Arctic Shift](https://arctic-shift.photon-reddit.com/) API. All content is the property of its respective authors / Reddit; this repository is for research and archival purposes only.
