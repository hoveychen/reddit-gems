#!/usr/bin/env python3
"""Generate Markdown digests from posts.jsonl."""
import json
import os
import re
from collections import Counter, defaultdict
from datetime import datetime, UTC

HERE = os.path.dirname(__file__)
IN_PATH = os.path.join(HERE, "posts.jsonl")
TOP_PATH = os.path.join(HERE, "top.md")
BY_FLAIR_PATH = os.path.join(HERE, "by_language.md")
BY_YEAR_PATH = os.path.join(HERE, "by_year.md")
STATS_PATH = os.path.join(HERE, "stats.md")


def load_posts():
    posts = []
    with open(IN_PATH) as f:
        for line in f:
            posts.append(json.loads(line))
    return posts


def gh_repo(url):
    m = re.match(r"https?://github\.com/([^/]+/[^/?#]+)", url or "")
    return m.group(1) if m else None


def fmt_post(p, idx=None):
    date = datetime.fromtimestamp(p["created_utc"], UTC).strftime("%Y-%m-%d")
    flair = p.get("link_flair_text") or ""
    flair_tag = f" `{flair}`" if flair else ""
    title = p["title"].replace("\n", " ").replace("|", "\\|")
    url = p.get("url", "")
    score = p.get("score", 0)
    n_comments = p.get("num_comments", 0)
    permalink = f"https://reddit.com{p['permalink']}"
    prefix = f"{idx}. " if idx else "- "
    return (
        f"{prefix}**[{title}]({url})**{flair_tag}  \n"
        f"   score `{score}` · comments `{n_comments}` · `{date}` · "
        f"[reddit]({permalink})"
    )


def write_top(posts):
    ranked = sorted(posts, key=lambda p: p.get("score", 0), reverse=True)
    with open(TOP_PATH, "w") as f:
        f.write("# r/coolgithubprojects — Top 500 by Score\n\n")
        f.write(f"Total posts archived: **{len(posts)}**  \n")
        f.write(f"Range: {datetime.fromtimestamp(min(p['created_utc'] for p in posts), UTC).date()} → "
                f"{datetime.fromtimestamp(max(p['created_utc'] for p in posts), UTC).date()}\n\n")
        for i, p in enumerate(ranked[:500], 1):
            f.write(fmt_post(p, i) + "\n\n")
    print(f"wrote {TOP_PATH}")


def write_by_flair(posts):
    by_flair = defaultdict(list)
    for p in posts:
        flair = (p.get("link_flair_text") or "OTHER").strip().upper()
        by_flair[flair].append(p)

    with open(BY_FLAIR_PATH, "w") as f:
        f.write("# r/coolgithubprojects — Top by Language Flair\n\n")
        for flair in sorted(by_flair, key=lambda k: -len(by_flair[k])):
            bucket = by_flair[flair]
            ranked = sorted(bucket, key=lambda p: p.get("score", 0), reverse=True)
            f.write(f"## {flair} ({len(bucket)} posts)\n\n")
            for p in ranked[:25]:
                f.write(fmt_post(p) + "\n\n")
            f.write("\n")
    print(f"wrote {BY_FLAIR_PATH}")


def write_by_year(posts):
    by_year = defaultdict(list)
    for p in posts:
        year = datetime.fromtimestamp(p["created_utc"], UTC).year
        by_year[year].append(p)

    with open(BY_YEAR_PATH, "w") as f:
        f.write("# r/coolgithubprojects — Top 30 by Year\n\n")
        for year in sorted(by_year):
            ranked = sorted(by_year[year], key=lambda p: p.get("score", 0), reverse=True)
            f.write(f"## {year} ({len(by_year[year])} posts)\n\n")
            for p in ranked[:30]:
                f.write(fmt_post(p) + "\n\n")
            f.write("\n")
    print(f"wrote {BY_YEAR_PATH}")


def write_stats(posts):
    by_year = Counter()
    by_flair = Counter()
    repos = Counter()
    for p in posts:
        by_year[datetime.fromtimestamp(p["created_utc"], UTC).year] += 1
        by_flair[(p.get("link_flair_text") or "—").upper()] += 1
        r = gh_repo(p.get("url", ""))
        if r:
            repos[r] += 1

    with open(STATS_PATH, "w") as f:
        f.write("# r/coolgithubprojects — Archive Stats\n\n")
        f.write(f"- Total posts: **{len(posts)}**\n")
        f.write(f"- Unique GitHub repos: **{len({gh_repo(p.get('url','')) for p in posts if gh_repo(p.get('url',''))})}**\n")
        f.write(f"- Date range: {datetime.fromtimestamp(min(p['created_utc'] for p in posts), UTC).date()} → "
                f"{datetime.fromtimestamp(max(p['created_utc'] for p in posts), UTC).date()}\n\n")

        f.write("## Posts per Year\n\n")
        f.write("| Year | Posts |\n|---|---|\n")
        for y in sorted(by_year):
            f.write(f"| {y} | {by_year[y]} |\n")

        f.write("\n## Top Language Flairs\n\n")
        f.write("| Flair | Posts |\n|---|---|\n")
        for flair, n in by_flair.most_common(30):
            f.write(f"| {flair} | {n} |\n")

        f.write("\n## Most-Submitted Repos (top 30)\n\n")
        f.write("| Repo | Times Submitted |\n|---|---|\n")
        for repo, n in repos.most_common(30):
            f.write(f"| [{repo}](https://github.com/{repo}) | {n} |\n")

    print(f"wrote {STATS_PATH}")


def main():
    posts = load_posts()
    print(f"loaded {len(posts)} posts")
    write_top(posts)
    write_by_flair(posts)
    write_by_year(posts)
    write_stats(posts)


if __name__ == "__main__":
    main()
