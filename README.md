# reddit-gems — r/coolgithubprojects 全量档案 & 浏览器

[r/coolgithubprojects](https://www.reddit.com/r/coolgithubprojects/) 12 年(2014–2026)全部帖子的归档、主题精选，以及一个能直接看图片/视频的浏览页面。

**在线浏览**: https://hoveychen.github.io/reddit-gems/

## 这是什么

- **25,794** 条帖子全量归档（数据源 [Arctic Shift](https://arctic-shift.photon-reddit.com/)，Pushshift 的继任者）
- 去重 + 反 spam 后 **14,604** 条，分到 14 个主题
- 浏览页面支持：图片 / YouTube / Reddit 视频(HLS) / 多图相册内嵌播放，按主题/语言/年份/分数筛选，搜索，无限滚动

## 文件说明

| 文件 | 作用 |
|---|---|
| `index.html` | 单文件浏览器（暗色主题，无构建依赖） |
| `data.json` | 14,604 条去重 + 主题分类的帖子（浏览页面的数据源） |
| `serve.sh` | 本地一键启动（起 HTTP 服务器并打开浏览器） |
| `scrape.py` | 从 Arctic Shift 抓取全量帖子（支持断点续传） |
| `build_browser_data.py` | `posts.jsonl` → `data.json`（去重、分类、提取媒体直链） |
| `build_digest.py` | 生成 `top.md` / `by_language.md` / `by_year.md` / `stats.md` |
| `build_clean_top.py` | 生成反 spam 版 `top_clean.md` |
| `curated.md` / `curated_clean.md` | 人工主题精选（中文，每条一句话点评） |
| `top.md` / `top_clean.md` | 按分数排序的 Top 500（原始 / 去重版） |
| `by_language.md` / `by_year.md` / `stats.md` | 按语言、按年、总体统计 |

> `posts.jsonl`（86 MB 原始全量数据）不在仓库里——跑 `python3 scrape.py` 即可重新抓取。

## 本地运行

```bash
./serve.sh              # 起服务器并打开浏览器
# 或指定端口
./serve.sh 8080
```

必须走本地 HTTP 服务器，不能直接 `file://` 打开（`fetch` 会被 CORS 拦）。

## 从零重建数据

```bash
python3 scrape.py              # 抓全量 → posts.jsonl
python3 build_browser_data.py  # → data.json（浏览页面用）
python3 build_digest.py        # → 各种 markdown 摘要
python3 build_clean_top.py     # → 反 spam Top 500
```

## 已知限制

- **视频/相册媒体**：约 87% 的视频、70% 的相册能在页面内播放；其余是 Arctic Shift 当年未抓到 `media` 字段的老帖，只显缩略图 + 跳转 Reddit。
- **过期 token**：归档时捕获的 v.redd.it 视频链接带签名 token，实测 Reddit CDN 不严格校验过期，老视频仍可播；但不保证长期有效。
- **`data.json` 媒体来自 Reddit CDN**：浏览页面需联网加载图片/视频。

## 数据来源与许可

帖子元数据来自 [Arctic Shift](https://arctic-shift.photon-reddit.com/) 公开 API。所有内容版权归各自原作者/Reddit 所有，本仓库仅作研究归档用途。
