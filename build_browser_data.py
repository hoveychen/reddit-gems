#!/usr/bin/env python3
"""Process posts.jsonl into a compact JSON for the browser viewer.

Output: data.json with cleaned + classified posts.
Drops deleted posts, dedupes by GitHub repo, caps per-author at 3.
Classifies each post into a theme based on title/url/flair keywords.
Extracts media type for browser embedding.
"""
import json
import os
import re
from collections import defaultdict

HERE = os.path.dirname(__file__)
IN_PATH = os.path.join(HERE, "posts.jsonl")
OUT_PATH = os.path.join(HERE, "data.json")


THEME_RULES = [
    ("AI / LLM", [
        r"\bllm\b", r"\bai\b", r"\bgpt\b", r"chatgpt", r"claude", r"agent",
        r"llama", r"openai", r"anthropic", r"copilot", r"mcp\b",
        r"stable diffusion", r"diffusion", r"transformer", r"embedding",
        r"hugging\s?face", r"langchain", r"voice clon", r"text to speech",
        r"tts\b", r"machine learning", r"deep learning", r"\bnlp\b",
        r"neural", r"prompt", r"token usage", r"vibecod",
    ]),
    ("Terminal / TUI", [
        r"\btui\b", r"\bcli\b", r"terminal", r"\bzsh\b", r"\bbash\b",
        r"command line", r"command-line", r"\bssh\b",
        r"htop", r"ncurses", r"\bvim\b", r"neovim", r"emacs",
    ]),
    ("Self-hosted SaaS Replacement", [
        r"self[- ]?host", r"open[- ]?source", r"alternative to",
        r"firebase alternative", r"postman alternative",
        r"google\s?(?:photos|analytics|drive|maps) alternative",
        r"slack alternative", r"discord alternative", r"notion alternative",
        r"trello alternative", r"\bsupabase\b", r"\bappwrite\b",
        r"\blemmy\b", r"\bowncast\b", r"\bplanka\b", r"\bbudibase\b",
        r"\btooljet\b", r"\bcal\.com\b", r"calendso", r"hoppscotch",
    ]),
    ("GitHub Meta", [
        r"github profile", r"github readme", r"github repo",
        r"git history", r"git city", r"git kingdom", r"\.gitignore",
        r"git client", r"contribution graph", r"github star",
        r"\breadme\b template", r"git cheat", r"git commit graph",
        r"github wrapped",
    ]),
    ("Music / Spotify", [
        r"spotify", r"apple music", r"amazon music", r"soundcloud",
        r"youtube music", r"playlist", r"\bmp3\b", r"\bflac\b",
        r"audiobook", r"lossless", r"lyric", r"music player",
        r"music theor", r"midi\b", r"daw\b",
    ]),
    ("Privacy / Security", [
        r"privacy", r"vpn\b", r"tor\b", r"fingerprint", r"tracker",
        r"track(?:ing|er)", r"adblock", r"ad-block", r"surveillance",
        r"encrypt", r"crypto(?!currency)", r"2fa\b", r"two[- ]factor",
        r"password", r"osint", r"pentest", r"\bhack(?:er|ing)\b",
        r"steganograph", r"firewall", r"phishing",
    ]),
    ("Quirky / Joke", [
        r"\bfuck\b", r"\bshit\b", r"useless", r"silly",
        r"for no reason", r"meme\b", r"shitpost", r"prank",
        r"nyan", r"trump", r"reee+", r"poke\?mon",
        r"butt\b", r"morse\s?code", r"esoteric language",
    ]),
    ("OS / Low Level", [
        r"\bos\b(?:\s|$)", r"operating system", r"kernel", r"bootloader",
        r"\bbios\b", r"\bx86\b", r"\barm\d?\b", r"assembly", r"\bgrub\b",
        r"compiler", r"interpreter", r"\bemulat", r"raspberry pi",
        r"raspi\b", r"\briscv\b", r"risc-v", r"firmware",
        r"reverse engineer", r"hardware",
    ]),
    ("Educational / Awesome List", [
        r"awesome[- ]", r"build your own", r"learn to ", r"how to build",
        r"resources for", r"curated list", r"cheatsheet", r"\btutorial\b",
        r"step by step", r"from scratch", r"interview prep",
        r"algorithm", r"data structure",
    ]),
    ("Browser Extension", [
        r"chrome extension", r"firefox extension", r"browser extension",
        r"web ?extension", r"extension that", r"\bvscode\b extension",
        r"editor extension",
    ]),
    ("Visual / Creative", [
        r"wallpaper", r"3d\s", r"render", r"shader",
        r"fractal", r"generative", r"procedural", r"ascii art",
        r"emoji", r"sticker", r"\bgame engine\b", r"glsl",
    ]),
    ("Politics / Society", [
        r"politic", r"election", r"climate", r"vaccine", r"covid",
        r"protest", r"war\b", r"conflict", r"refuge", r"senator",
        r"government", r"misinformation", r"fake news",
        r"social good", r"non[- ]profit", r"charity", r"justice",
    ]),
    ("Productivity / Workflow", [
        r"productivity", r"task\s?manage", r"todo", r"to[- ]do",
        r"calendar", r"note[- ]?taking", r"kanban", r"workflow",
        r"time track", r"\bpomodoro\b", r"habit",
    ]),
]


def classify(post):
    title = (post.get("title") or "").lower()
    url = (post.get("url") or "").lower()
    flair = (post.get("link_flair_text") or "").lower()
    text = f"{title} || {url} || {flair}"
    matched = []
    for theme, patterns in THEME_RULES:
        for pat in patterns:
            if re.search(pat, text):
                matched.append(theme)
                break
    if not matched:
        return ["Other / Misc"]
    return matched


def gh_repo(url):
    m = re.match(r"https?://(?:www\.)?github\.com/([^/]+/[^/?#]+)", url or "")
    return m.group(1).lower().rstrip(".git") if m else None


def media_kind(post):
    url = post.get("url") or ""
    if re.match(r"https?://i\.redd\.it/", url) or re.search(r"\.(?:png|jpe?g|gif|webp)(?:\?|$)", url, re.I):
        return "image"
    if "v.redd.it" in url:
        return "reddit_video"
    if "reddit.com/gallery" in url:
        return "reddit_gallery"
    if re.search(r"(?:youtube\.com/watch\?v=|youtu\.be/)", url):
        return "youtube"
    if "github.com" in url:
        return "github"
    if re.match(r"https?://", url):
        return "link"
    return "none"


def extract_yt_id(url):
    m = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{6,})", url or "")
    return m.group(1) if m else None


def unescape(u):
    return (u or "").replace("&amp;", "&")


def extract_reddit_video(post):
    rv = ((post.get("media") or {}).get("reddit_video")
          or (post.get("secure_media") or {}).get("reddit_video") or {})
    if not rv:
        return None
    out = {"is_gif": bool(rv.get("is_gif"))}
    if rv.get("hls_url"):
        out["hls"] = unescape(rv["hls_url"])
    if rv.get("fallback_url"):
        out["mp4"] = unescape(rv["fallback_url"])
    if rv.get("width"):
        out["w"] = rv["width"]
    if rv.get("height"):
        out["h"] = rv["height"]
    return out if (out.get("hls") or out.get("mp4")) else None


def extract_gallery(post):
    gdata = post.get("gallery_data") or {}
    mm = post.get("media_metadata") or {}
    items = gdata.get("items") or []
    imgs = []
    # Prefer gallery_data ordering; fall back to media_metadata key order.
    order = [it.get("media_id") for it in items] if items else list(mm.keys())
    for mid in order:
        meta = mm.get(mid)
        if not isinstance(meta, dict):
            continue
        s = meta.get("s") or {}
        url = None
        if meta.get("e") == "AnimatedImage":
            url = s.get("gif") or s.get("mp4")
        else:
            url = s.get("u")
        if not url:
            # last resort: highest-res preview
            ps = meta.get("p") or []
            if ps:
                url = ps[-1].get("u")
        if url:
            imgs.append(unescape(url))
    return imgs or None


def main():
    posts = []
    with open(IN_PATH) as f:
        for line in f:
            posts.append(json.loads(line))
    print(f"loaded {len(posts)} raw posts")

    # Drop deleted/meta
    posts = [
        p for p in posts
        if (p.get("author") or "") != "[deleted]"
        and "reddit.com/r/coolgithubprojects" not in (p.get("url") or "")
        and "[deleted by user]" not in (p.get("title") or "").lower()
    ]
    print(f"after drop deleted: {len(posts)}")

    # Dedupe by repo
    best = {}
    no_repo = []
    for p in posts:
        r = gh_repo(p.get("url") or "")
        if r is None:
            no_repo.append(p)
            continue
        cur = best.get(r)
        if cur is None or p.get("score", 0) > cur.get("score", 0):
            best[r] = p
    deduped = list(best.values()) + no_repo
    print(f"after repo dedupe: {len(deduped)}")

    # Author cap 3
    deduped.sort(key=lambda p: p.get("score", 0), reverse=True)
    cnt = defaultdict(int)
    kept = []
    for p in deduped:
        a = p.get("author") or ""
        if cnt[a] >= 3:
            continue
        cnt[a] += 1
        kept.append(p)
    print(f"after author cap: {len(kept)}")

    # Build compact records
    out = []
    for p in kept:
        url = p.get("url") or ""
        thumb = p.get("thumbnail") or ""
        if thumb in ("default", "self", "nsfw", "spoiler", "image"):
            thumb = ""
        kind = media_kind(p)
        record = {
            "id": p["id"],
            "title": p["title"],
            "url": url,
            "score": p.get("score", 0),
            "n_comments": p.get("num_comments", 0),
            "author": p.get("author", ""),
            "flair": p.get("link_flair_text") or "",
            "created_utc": p["created_utc"],
            "permalink": f"https://reddit.com{p['permalink']}",
            "selftext": (p.get("selftext") or "")[:600],
            "thumbnail": thumb,
            "kind": kind,
            "themes": classify(p),
        }
        if kind == "youtube":
            record["yt_id"] = extract_yt_id(url)
        if kind == "github":
            record["repo"] = gh_repo(url)
        if kind == "reddit_video":
            vid = extract_reddit_video(p)
            if vid:
                record["video"] = vid
        if kind == "reddit_gallery":
            imgs = extract_gallery(p)
            if imgs:
                record["gallery"] = imgs
        out.append(record)

    # Sort by score desc for default ordering
    out.sort(key=lambda p: p["score"], reverse=True)

    with open(OUT_PATH, "w") as f:
        json.dump({"posts": out, "total": len(out)}, f, ensure_ascii=False, separators=(",", ":"))
    size = os.path.getsize(OUT_PATH) / 1024 / 1024
    print(f"wrote {OUT_PATH} ({size:.1f} MB, {len(out)} posts)")

    # Quick theme tally
    theme_counts = defaultdict(int)
    for p in out:
        for t in p["themes"]:
            theme_counts[t] += 1
    print("\nTheme distribution:")
    for t, c in sorted(theme_counts.items(), key=lambda x: -x[1]):
        print(f"  {c:>5}  {t}")


if __name__ == "__main__":
    main()
