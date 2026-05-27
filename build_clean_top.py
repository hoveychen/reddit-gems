#!/usr/bin/env python3
"""Generate dedupe'd + spam-filtered Top 500 from posts.jsonl.

Strategy:
1. Dedupe by GitHub repo (owner/repo): keep the highest-scoring submission.
2. Cap per author at 3 (keeps top-3 scoring posts per submitter).
3. Drop deleted/removed posts (author == '[deleted]' or title contains '[deleted]').
4. Drop crossposts/links to /r/ itself (where url contains 'reddit.com/r/coolgithubprojects').
5. Re-rank by score, take top 500.
"""
import json
import os
import re
from collections import defaultdict
from datetime import datetime, UTC

HERE = os.path.dirname(__file__)
IN_PATH = os.path.join(HERE, "posts.jsonl")
OUT_PATH = os.path.join(HERE, "top_clean.md")


def gh_repo(url):
    m = re.match(r"https?://(?:www\.)?github\.com/([^/]+/[^/?#]+)", url or "")
    if not m:
        return None
    owner_repo = m.group(1)
    return owner_repo.lower().rstrip(".git")


def load_posts():
    posts = []
    with open(IN_PATH) as f:
        for line in f:
            posts.append(json.loads(line))
    return posts


def fmt_post(p, idx):
    date = datetime.fromtimestamp(p["created_utc"], UTC).strftime("%Y-%m-%d")
    flair = p.get("link_flair_text") or ""
    flair_tag = f" `{flair}`" if flair else ""
    title = p["title"].replace("\n", " ").replace("|", "\\|")
    url = p.get("url", "")
    score = p.get("score", 0)
    n_comments = p.get("num_comments", 0)
    author = p.get("author", "")
    permalink = f"https://reddit.com{p['permalink']}"
    return (
        f"{idx}. **[{title}]({url})**{flair_tag}  \n"
        f"   score `{score}` · comments `{n_comments}` · `{date}` · u/{author} · "
        f"[reddit]({permalink})"
    )


def main():
    raw = load_posts()
    print(f"Raw posts: {len(raw)}")

    # Stage 1: drop deleted / removed / self-meta
    stage1 = []
    drop_deleted = 0
    drop_meta = 0
    for p in raw:
        if (p.get("author") or "") == "[deleted]":
            drop_deleted += 1
            continue
        if "[deleted by user]" in (p.get("title") or "").lower():
            drop_deleted += 1
            continue
        url = p.get("url") or ""
        if "reddit.com/r/coolgithubprojects" in url:
            drop_meta += 1
            continue
        stage1.append(p)
    print(f"After drop deleted/meta: {len(stage1)} (dropped {drop_deleted} deleted, {drop_meta} self-meta)")

    # Stage 2: dedupe by GitHub repo (keep highest score per repo)
    best_per_repo = {}
    no_repo_posts = []
    for p in stage1:
        repo = gh_repo(p.get("url") or "")
        if repo is None:
            no_repo_posts.append(p)
            continue
        cur = best_per_repo.get(repo)
        if cur is None or p.get("score", 0) > cur.get("score", 0):
            best_per_repo[repo] = p

    deduped = list(best_per_repo.values()) + no_repo_posts
    print(f"After dedupe by repo: {len(deduped)} "
          f"(merged {len(stage1) - len(deduped)} duplicate-repo submissions; "
          f"{len(no_repo_posts)} had no parseable GitHub URL)")

    # Stage 3: per-author cap at 3 (keep top-3 by score)
    deduped.sort(key=lambda p: p.get("score", 0), reverse=True)
    per_author_count = defaultdict(int)
    capped = []
    capped_out = 0
    for p in deduped:
        a = p.get("author") or ""
        if per_author_count[a] >= 3:
            capped_out += 1
            continue
        per_author_count[a] += 1
        capped.append(p)
    print(f"After per-author cap (3): {len(capped)} (capped {capped_out} extras)")

    # Stage 4: top 500
    top = capped[:500]
    print(f"Final top: {len(top)}")

    # Compute deltas vs raw-by-score top 500
    raw_top = sorted(raw, key=lambda p: p.get("score", 0), reverse=True)[:500]
    raw_ids = {p["id"] for p in raw_top}
    new_in_clean = [p for p in top if p["id"] not in raw_ids]
    print(f"\nNew posts that surfaced into top 500 (not in raw top 500): {len(new_in_clean)}")

    with open(OUT_PATH, "w") as f:
        f.write("# r/coolgithubprojects — Cleaned Top 500\n\n")
        f.write("**Cleaning rules applied:**\n\n")
        f.write("1. Removed deleted/removed posts.\n")
        f.write("2. Removed meta-posts linking to the sub itself.\n")
        f.write("3. **Dedupe by GitHub repo**: same `owner/repo` collapsed to its highest-scoring submission "
                f"(merged {len(stage1) - len(deduped)} duplicate-repo submissions).\n")
        f.write(f"4. **Per-author cap at 3**: each user contributes at most 3 posts (capped out {capped_out} extras).\n\n")
        f.write(f"This surfaced **{len(new_in_clean)}** posts into the top 500 that were buried in the raw ranking.\n\n")
        f.write("---\n\n")
        for i, p in enumerate(top, 1):
            f.write(fmt_post(p, i) + "\n\n")

    print(f"\nWrote {OUT_PATH}")


if __name__ == "__main__":
    main()
