# r/coolgithubprojects — 主题精选

老板研究用。从 Top 500 (按 score 排序) 里按主题挑出**值得点开**的项目, 每条都有一句话理由说为什么有意思。

去掉了反复刷榜的同一项目、自推 spam、"awesome-list 套娃"、以及单纯"我做了个 X 的克隆"无新意的条目。

12 年数据里我看到三波浪潮: **2015-2019 教程/awesome 列表**为王 → **2020-2022 自托管 SaaS 替代品 + 终端 TUI**爆发 → **2023+ AI/LLM 工具**接管 → **2026 GitHub-meta 游戏化**冒头。

---

## 1. AI / LLM 工具 (2023 起的主线)

最近三年这个分类完全主导榜单, 老板最该花时间的就是这块。

- **[Memoir — Git for AI Memory](https://reddit.com/r/coolgithubprojects/comments/1t5jh09/)** (2026-05, score 247) — 给 agent 的记忆做了 git 式的 explain / rewind / branch, 概念非常新, 跟当前 Claude Code memory 思路同源
- **[Serge — self-hosted ChatGPT (LLaMa)](https://reddit.com/r/coolgithubprojects/comments/11xzdx6/)** (2023-03, score 163) — 完全离线的 ChatGPT 替代, 早期本地 LLM 部署的代表
- **[AgentGPT — autonomous AI agents in browser](https://reddit.com/r/coolgithubprojects/comments/12g9l32/)** (2023-04, score 102) — 浏览器里跑 autonomous agent 的早期火爆案例
- **[FauxPilot — open-source GitHub Copilot server](https://reddit.com/r/coolgithubprojects/comments/wult7p/)** (2022-08, score 83) — Copilot 的自托管版, AI 编程辅助早期项目
- **[HuggingChat with web search](https://reddit.com/r/coolgithubprojects/comments/141emy0/)** (2023-06, score 86) — HuggingFace 的开源 ChatGPT 替代
- **[Adrenaline — GPT-3 调试器](https://reddit.com/r/coolgithubprojects/comments/108gios/)** (2023-01, score 89) — 自动修 bug 并解释错误, 早期 AI 编程辅助
- **[LLM contract layer (enforce agent rules at tool boundary)](https://reddit.com/r/coolgithubprojects/comments/1tkulgw/)** (2026-05, score 86) — agent 不听规则时强制在 tool 调用边界拦截, 真问题真方案
- **[Multi-pane agentic markdown workspace](https://reddit.com/r/coolgithubprojects/comments/1t46swq/)** (2026-05, score 176) — 给 LLM 协作的多面板 markdown 工作台
- **[Intelligence terminal (26 global data sources + AI analyst)](https://reddit.com/r/coolgithubprojects/comments/1rtdonf/)** (2026-03, score 368) — 自托管情报终端, 把全球数据源汇总后给 AI 分析
- **[Steganography engine — hide files in JPEG/MP4/audio using ML](https://reddit.com/r/coolgithubprojects/comments/1sue17a/)** (2026-04, score 354) — ML 驱动的隐写术, 编译成无依赖单文件
- **[Cate v1.0 — infinite canvas IDE](https://reddit.com/r/coolgithubprojects/comments/1tmef9f/)** (2026-05, score 321) — Figma 式的代码编辑器, 无限画布
- **[CLI that cuts AI coding tokens 97%](https://reddit.com/r/coolgithubprojects/comments/1t6qd9q/)** (2026-05, score 185) — 给 Claude/Cursor 这类 AI 编码省 token, 10k 下载
- **[TUI to see where Claude Code tokens actually go](https://reddit.com/r/coolgithubprojects/comments/1suiq7j/)** (2026-04, score 146) — Claude Code 的 token 流向可视化, 跟老板 fleet 业务高度相关
- **[Open-source flight search for AI agents](https://reddit.com/r/coolgithubprojects/comments/1t06f3y/)** (2026-04, score 163) — 给 agent 用的航班搜索 API, 700 stars
- **[Stable Diffusion Latent Space Explorer](https://reddit.com/r/coolgithubprojects/comments/12v5j0v/)** (2023-04, score 76) — SD 的 latent space 研究工具
- **[Vimtutor for AI coding](https://reddit.com/r/coolgithubprojects/comments/1rr6i6i/)** (2026-03, score 139) — 终端里学 context window/MCP/tools, 互动式教程
- **[Voice clone in 5 seconds (real-time)](https://reddit.com/r/coolgithubprojects/comments/c3pwym/)** (2019-06, score 154) — 5 秒克隆声音, real-time TTS

## 2. 终端 / TUI 工具 (一直长青)

- **[Rich — Python terminal rendering](https://reddit.com/r/coolgithubprojects/comments/gdbxmr/)** (2020-05, score 158) — Python 圈终端美化的事实标准库
- **[lazygit — terminal UI for git](https://reddit.com/r/coolgithubprojects/comments/r5ugcy/)** (2021-11, score 99) — git 命令行的 Go 写的 TUI, 早成主流
- **[Sampler — configurable CLI dashboard](https://reddit.com/r/coolgithubprojects/comments/u7i9h6/)** (2022-04, score 165) — 配置化的终端 dashboard
- **[Serie — rich git commit graph in terminal](https://reddit.com/r/coolgithubprojects/comments/1ru1p5u/)** (2026-03, score 102) — 终端里的彩色 commit graph
- **[cosmo-tui — NASA data in terminal](https://reddit.com/r/coolgithubprojects/comments/1sy1spv/)** (2026-04, score 188) — 终端实时显示 wildfires / 小行星 / ISS / APOD
- **[Devzat — Discord 但在 SSH 终端](https://reddit.com/r/coolgithubprojects/comments/tecnpx/)** (2022-03, score 90) — 终端里的 Discord, 通过 ssh 连接, 有频道/DM/emoji/语法高亮
- **[mangadesk — terminal manga 客户端](https://reddit.com/r/coolgithubprojects/comments/nbif30/)** (2021-05, score 133) — 终端里看漫画
- **[Awk Raycaster FPS](https://reddit.com/r/coolgithubprojects/comments/6jypr6/)** (2017-06, score 131) — 完全用 awk 写的终端 FPS, 经典脑洞
- **[NBA-Go — 终端看 NBA](https://reddit.com/r/coolgithubprojects/comments/7b4f9d/)** (2017-11, score 75)
- **[football-cli — 终端看球赛](https://reddit.com/r/coolgithubprojects/comments/1t5bz6y/)** (2026-05, score 174)
- **[cliflix — 终端流媒体](https://reddit.com/r/coolgithubprojects/comments/9naj7p/)** (2018-10, score 110) — 命令行直接搜片即看
- **[Toipe — Rust 终端打字测试](https://reddit.com/r/coolgithubprojects/comments/tvapra/)** (2022-04, score 95)
- **[gpg-tui — GPG 密钥管理 TUI](https://reddit.com/r/coolgithubprojects/comments/nnnvh8/)** (2021-05, score 87)
- **[Pokemon Terminal](https://reddit.com/r/coolgithubprojects/comments/6flqr9/)** (2017-06, score 76) — 终端壁纸 = 宝可梦
- **[Periodic table CLI](https://reddit.com/r/coolgithubprojects/comments/o48swr/)** (2021-06, score 140)

## 3. 自托管 SaaS 替代品

- **[Supabase — open Firebase alternative](https://reddit.com/r/coolgithubprojects/comments/nlglrw/)** (2021-05, score 129)
- **[Appwrite (Firebase alt) — $10m seed](https://reddit.com/r/coolgithubprojects/comments/qi8v3x/)** (2021-10, score 77)
- **[Calendso (后改名 Cal.com) — Calendly 替代](https://reddit.com/r/coolgithubprojects/comments/mtl38r/)** (2021-04, score 72)
- **[Notesnook — E2E 加密 Evernote 替代](https://reddit.com/r/coolgithubprojects/comments/x3vrep/)** (2022-09, score 76)
- **[Owncast — 自托管 Twitch](https://reddit.com/r/coolgithubprojects/comments/kgugpt/)** (2020-12, score 78)
- **[LibrePhotos — 自托管 Google Photos](https://reddit.com/r/coolgithubprojects/comments/kntjhw/)** (2020-12, score 78)
- **[Lemmy — Rust 写的 Reddit 替代](https://reddit.com/r/coolgithubprojects/comments/c46nf8/)** (2019-06, score 95)
- **[Planka — Trello 替代 (React/Sails/Redux)](https://reddit.com/r/coolgithubprojects/comments/dfozpj/)** (2019-10, score 95)
- **[Shynet — 无 cookie 的 Google Analytics 替代](https://reddit.com/r/coolgithubprojects/comments/g61p43/)** (2020-04, score 102)
- **[Authentik — 开源 IdP (OAuth/SAML/LDAP)](https://reddit.com/r/coolgithubprojects/comments/xwdeo6/)** (2022-10, score 94)
- **[ToolJet — Retool/PowerApps 替代](https://reddit.com/r/coolgithubprojects/comments/tho1rb/)** (2022-03, score 128)
- **[Budibase — 低代码 Retool 替代](https://reddit.com/r/coolgithubprojects/comments/tgxr3u/)** (2022-03, score 83)
- **[Hoppscotch (前 Postwoman) — Postman 替代](https://reddit.com/r/coolgithubprojects/comments/hki548/)** (2020-07, score 102) — 同项目反复登顶, 60k+ stars
- **[NOMAD — 自托管旅行计划器](https://reddit.com/r/coolgithubprojects/comments/1ry5q9e/)** (2026-03, score 75)
- **[Awesome OSS Alternatives](https://reddit.com/r/coolgithubprojects/comments/xketrq/)** (2022-09, score 84) — SaaS 替代品的索引表, 元资源
- **[Clone Wars — 70+ 开源克隆站点列表](https://reddit.com/r/coolgithubprojects/comments/m4awk2/)** (2021-03, score 96)

## 4. GitHub 元话题 (2026 兴起的奇怪潮流)

整个 sub 在 2026 年突然爆发了"把 GitHub 本身做成游戏/可视化"的潮流。

- **[GitKingdom — repos 变成幻想世界建筑, stars 决定建筑大小](https://reddit.com/r/coolgithubprojects/comments/1s2nr4q/)** (2026-03, score 330)
- **[Git City — 每个开发者 = 3D 像素艺术建筑](https://reddit.com/r/coolgithubprojects/comments/1rh8jyu/)** (2026-02, score 94)
- **[GitHub 贡献图 → 可驾驶的 3D 城市](https://reddit.com/r/coolgithubprojects/comments/1s726uc/)** (2026-03, score 99)
- **[Globe of devs coding around the world](https://reddit.com/r/coolgithubprojects/comments/1rryysc/)** (2026-03, score 120)
- **[Repo Death Certificates — 给废弃 repo 发死亡证书](https://reddit.com/r/coolgithubprojects/comments/1s1bvha/)** (2026-03, score 148) — 这个反 cargo-cult 的设定挺机智
- **[1400+ people roast their GitHub repos](https://reddit.com/r/coolgithubprojects/comments/1s0scjl/)** (2026-03, score 75)
- **[GitHub Profile Visualizer](https://reddit.com/r/coolgithubprojects/comments/1t3a0rz/)** (2026-05, score 247)
- **[Tiny pets for GitHub README](https://reddit.com/r/coolgithubprojects/comments/1ssca2e/)** (2026-04, score 87)
- **[CLI that turns git history → Victorian 报纸](https://reddit.com/r/coolgithubprojects/comments/1sq55ev/)** (2026-04, score 82)
- **[rgitui — GPU-accelerated Rust git client](https://reddit.com/r/coolgithubprojects/comments/1sfob0k/)** (2026-04, score 111)
- **[Beautiful Git cheatsheet — 92 commands](https://reddit.com/r/coolgithubprojects/comments/1szgghh/)** (2026-04, score 165)
- **[oh-my-git — 互动式 Git 学习游戏](https://reddit.com/r/coolgithubprojects/comments/vm32ir/)** (2022-06, score 83)

## 5. Spotify / 音乐工具 (反复出现的小品类)

- **[Antra — 从 Spotify/Apple Music/Amazon Music 下载无损音频](https://reddit.com/r/coolgithubprojects/comments/1spe3iv/)** (2026-04, score 177)
- **[Playlist → 本地 FLAC 库 (桌面 app)](https://reddit.com/r/coolgithubprojects/comments/1si0ebr/)** (2026-04, score 198)
- **[Spytify — 录 Spotify 不带广告, 自动打标签](https://reddit.com/r/coolgithubprojects/comments/p2b05e/)** (2021-08, score 115)
- **[Psst — Rust 写的 Spotify 客户端 (原生 GUI)](https://reddit.com/r/coolgithubprojects/comments/kp2vge/)** (2021-01, score 91)
- **[Vibecoded YouTube-music desktop player](https://reddit.com/r/coolgithubprojects/comments/1t1z6jx/)** (2026-05, score 128) — 反 YouTube 广告

## 6. 隐私 / 安全 / 反追踪

- **[Vytal — 展示 VPN+隐身模式都防不住的 fingerprint](https://reddit.com/r/coolgithubprojects/comments/pyag65/)** (2021-09, score 152) — 教育意义十足
- **[Awesome Privacy](https://reddit.com/r/coolgithubprojects/comments/vytm4o/)** (2022-07, score 122)
- **[Awesome Personal Security Checklist](https://reddit.com/r/coolgithubprojects/comments/fe44z6/)** (2020-03, score 82)
- **[Logout4Shell — 用 Log4Shell 漏洞反向给服务器打补丁](https://reddit.com/r/coolgithubprojects/comments/rgfxyy/)** (2021-12, score 102) — 反向利用漏洞救命, 经典安全脑洞
- **[Universal Bypass — 跳过链接缩短服务](https://reddit.com/r/coolgithubprojects/comments/fmfsnr/)** (2020-03, score 73)
- **[Sherlock — 75+ 社交网络上找用户名](https://reddit.com/r/coolgithubprojects/comments/a9dty4/)** (2018-12, score 73)
- **[Osintgram — Instagram OSINT 工具](https://reddit.com/r/coolgithubprojects/comments/mgi608/)** (2021-03, score 75)
- **[NeuralHash Collider — 生成 Apple NeuralHash 碰撞](https://reddit.com/r/coolgithubprojects/comments/p7536b/)** (2021-08, score 77) — 当年挑战 Apple CSAM 检测的政治时刻
- **[Wristkey — Wear OS 的离线 Google Authenticator](https://reddit.com/r/coolgithubprojects/comments/nog4zo/)** (2021-05, score 76)
- **[Hereditas — 你消失时把密码留给亲人](https://reddit.com/r/coolgithubprojects/comments/fnl7vt/)** (2020-03, score 72)
- **[Infection Monkey — 数据中心穿透测试蠕虫](https://reddit.com/r/coolgithubprojects/comments/cp8trt/)** (2019-08, score 84)

## 7. 脑洞 / 玩梗 (这个 sub 的灵魂)

- **[ButtFish — 通过屁眼用摩尔斯码传国际象棋着法](https://reddit.com/r/coolgithubprojects/comments/xs193z/)** (2022-09, score 182) — 标题就赢了
- **[Volkswagen — 检测到 CI 环境就让测试通过](https://reddit.com/r/coolgithubprojects/comments/3o276q/)** (2015-10, score 99) — "排放门"的程序员版黑色幽默
- **[FOAAS — Fuck Off As A Service (RESTful)](https://reddit.com/r/coolgithubprojects/comments/p4rhw8/)** (2021-08, score 149) — 把"滚开"做成 SaaS
- **[Bullshit.js — 把营销话翻译成大白话](https://reddit.com/r/coolgithubprojects/comments/nmwe7u/)** (2021-05, score 148)
- **[TrumpScript — 让 Python 再次伟大](https://reddit.com/r/coolgithubprojects/comments/41l9qt/)** (2016-01, score 126) — Python 主题语法的政治脑洞
- **[I-use-arch-btw — 图灵完备的 "I use Arch btw" 语言](https://reddit.com/r/coolgithubprojects/comments/chc4mc/)** (2019-07, score 72)
- **[fattest-cat — 找旧金山动物收容所最胖的猫](https://reddit.com/r/coolgithubprojects/comments/5x4edy/)** (2017-03, score 92)
- **[vim-disapprove-deep-indentation — Vim 插件: ಠ_ಠ 表达对深嵌套代码的不满](https://reddit.com/r/coolgithubprojects/comments/5xpb2j/)** (2017-03, score 82)
- **[Echo 用 x86 汇编重写, 体积小 96.9%](https://reddit.com/r/coolgithubprojects/comments/42hbkw/)** (2016-01, score 108)
- **[Auto-like-my-gf-insta-pic — 自动给女友 ins 点赞](https://reddit.com/r/coolgithubprojects/comments/7l91r1/)** (2017-12, score 122) — 经典懒鬼自动化
- **[Hacker Scripts — 一个程序员的"真实"自动化故事](https://reddit.com/r/coolgithubprojects/comments/3txnbm/)** (2015-11, score 74) — 把生活全自动化的传奇剧本
- **[NFTBlocker — 自动屏蔽 Twitter NFT 头像](https://reddit.com/r/coolgithubprojects/comments/s8ts6y/)** (2022-01, score 98)
- **[NFTshills — 给 NFT 站台的名人黑名单](https://reddit.com/r/coolgithubprojects/comments/sm6rxt/)** (2022-02, score 113)
- **[Comcast — 模拟糟糕网络测试 app](https://reddit.com/r/coolgithubprojects/comments/2z5ioi/)** (2015-03, score 73) — 名字最妙
- **[Chrome Dino 跑在 URL 栏 (带多人)](https://reddit.com/r/coolgithubprojects/comments/1t19fob/)** (2026-05, score 122)
- **[fake-DOCX from PDF — 让 PDF 看起来像可编辑 docx](https://reddit.com/r/coolgithubprojects/comments/plzh07/)** (2021-09, score 135)
- **[system-bus-radio — 没硬件的电脑用系统总线发射无线电](https://reddit.com/r/coolgithubprojects/comments/48j5cz/)** (2016-03, score 121)

## 8. OS / 低层 / 编译器

- **[12 岁小孩从零写了个 OS](https://reddit.com/r/coolgithubprojects/comments/1t7u5eq/)** (2026-05, score 107) — 评论区 79 条
- **[MS-DOS v1.25 / v2.0 源码 (微软自己开源)](https://reddit.com/r/coolgithubprojects/comments/9k0y3u/)** (2018-09, score 131) — Assembly 代码
- **[Apollo 11 制导计算机源码](https://reddit.com/r/coolgithubprojects/comments/4rpamz/)** (2016-07, score 72)
- **[Tesla 终于发布 Model S/X 的 Linux 源码](https://reddit.com/r/coolgithubprojects/comments/8npz51/)** (2018-06, score 95)
- **[C 编译器从零写, 意外比 TCC 快](https://reddit.com/r/coolgithubprojects/comments/1skyrud/)** (2026-04, score 82)
- **[MarvinOS — 业余 x86 OS, 含 GRUB/GDT/中断/VGA/键盘/timer](https://reddit.com/r/coolgithubprojects/comments/b9s1bp/)** (2019-04, score 122)
- **[os-tutorial — 从零造 OS 的教程](https://reddit.com/r/coolgithubprojects/comments/9hok2o/)** (2018-09, score 114)
- **[TabFS — 浏览器 tab 当文件系统挂载](https://reddit.com/r/coolgithubprojects/comments/kok49w/)** (2021-01, score 102) — 用 FUSE 把 tab 当目录, 神秘脑洞
- **[Docker-OSX — Docker 里跑 macOS (近原生 OSX-KVM)](https://reddit.com/r/coolgithubprojects/comments/h9hdb6/)** (2020-06, score 86)
- **[Ventoy — 多 ISO 启动 USB](https://reddit.com/r/coolgithubprojects/comments/k1sbt4/)** (2020-11, score 124)
- **[Hidviz — USB HID 设备逆向工具](https://reddit.com/r/coolgithubprojects/comments/e4vrk3/)** (2019-12, score 88)

## 9. Build-Your-Own / Awesome (元学习资源)

榜单上最经久不衰的, 但要警惕 awesome-list 套娃。挑出独特的:

- **[build-your-own-x](https://reddit.com/r/coolgithubprojects/comments/my6kgr/)** (2021-04, score 148) — 从头实现各种技术的教程合集, 经典
- **[Cosmos — 你能遇到的每个算法/数据结构的代码库](https://reddit.com/r/coolgithubprojects/comments/bnei5f/)** (2019-05, score 120) — OpenGenus 的项目, 多次登顶
- **[what-to-code — 给没灵感的程序员的项目点子清单](https://reddit.com/r/coolgithubprojects/comments/4x79po/)** (2016-08, score 139)
- **[WTF Python — 让人惊讶的 Python 怪行为](https://reddit.com/r/coolgithubprojects/comments/a3zlit/)** (2018-12, score 81)
- **[Awesome Falsehood — 程序员相信的各种错误命题](https://reddit.com/r/coolgithubprojects/comments/8fqzan/)** (2018-04, score 83) — "名字不只是字符串"系列
- **[Awesome Hacking](https://reddit.com/r/coolgithubprojects/comments/5k9iox/)** (2016-12, score 93)
- **[uncurled — Daniel Stenberg 三十年 OSS 维护心得](https://reddit.com/r/coolgithubprojects/comments/xvdk9h/)** (2022-10, score 75)
- **[awful-oss-incidents — 维护者负担/资金不足导致的安全事件分类](https://reddit.com/r/coolgithubprojects/comments/xchpxd/)** (2022-09, score 76) — 元元话题, 但有研究价值
- **[What happens when you type google.com — 从硬件层往上讲清楚](https://reddit.com/r/coolgithubprojects/comments/62rjek/)** (2017-04, score 101) — 经典面试题的开源解答

## 10. 实用工具 (做一件事且做得好)

- **[Deskreen — 把任何带浏览器的设备变成第二屏](https://reddit.com/r/coolgithubprojects/comments/l4n9yi/)** (2021-01, score 152)
- **[Tesseract.js — 100+ 语言纯 JS OCR](https://reddit.com/r/coolgithubprojects/comments/eend25/)** (2019-12, score 94)
- **[BackgroundRemover — 命令行抠图/抠视频](https://reddit.com/r/coolgithubprojects/comments/p5ww17/)** (2021-08, score 77)
- **[Handwrite — 从手写样本生成字体](https://reddit.com/r/coolgithubprojects/comments/lf72j8/)** (2021-02, score 94)
- **[Soundsync — 任意音源到家里任意音响](https://reddit.com/r/coolgithubprojects/comments/hitfuc/)** (2020-06, score 105)
- **[Gnirehtet — Android USB 反向 tether (借电脑网络)](https://reddit.com/r/coolgithubprojects/comments/qahwfh/)** (2021-10, score 80)
- **[Flying Carpet — 跨平台 ad-hoc WiFi 加密传文件](https://reddit.com/r/coolgithubprojects/comments/7pppcl/)** (2018-01, score 76)
- **[tmpmail — 终端里收一次性邮件](https://reddit.com/r/coolgithubprojects/comments/irx9gs/)** (2020-09, score 102)
- **[fake-SMS — 临时手机号过 SMS 验证](https://reddit.com/r/coolgithubprojects/comments/lmpgbj/)** (2021-02, score 97)
- **[Port killer (TS)](https://reddit.com/r/coolgithubprojects/comments/1siqalg/)** (2026-04, score 84) — "port already in use" 终结者
- **[Mouzi — 自动整理下载文件夹 (Rust)](https://reddit.com/r/coolgithubprojects/comments/1tcbzrg/)** (2026-05, score 127)
- **[Bento — Bento 盒子风格的极简新标签页](https://reddit.com/r/coolgithubprojects/comments/ooiig6/)** (2021-07, score 76)
- **[Bonjourr — iOS 风格的轻量新标签页](https://reddit.com/r/coolgithubprojects/comments/uq3pgb/)** (2022-05, score 174)
- **[Battery-Safe — 提醒你何时插拔电源保护电池](https://reddit.com/r/coolgithubprojects/comments/hz0npp/)** (2020-07, score 73)
- **[Sloth — macOS 上所有进程的打开文件可视化 (lsof 的 GUI)](https://reddit.com/r/coolgithubprojects/comments/pzv8xd/)** (2021-10, score 92)
- **[MeetingBar — macOS 状态栏会议提醒](https://reddit.com/r/coolgithubprojects/comments/iuo5tt/)** (2020-09, score 79)
- **[Clipmon — 自由的剪贴板管理器](https://reddit.com/r/coolgithubprojects/comments/1t2evti/)** (2026-05, score 74)

## 11. 浏览器扩展 (有创意的)

- **[Reddit comments on any YouTube/webpage](https://reddit.com/r/coolgithubprojects/comments/nve864/)** (2021-06, score 289) — 浏览任何页面时看 Reddit 上对这页的讨论
- **[HN + Reddit discussions for current page](https://reddit.com/r/coolgithubprojects/comments/vi76a2/)** (2022-06, score 132) — 同上, HN 版
- **[google-photos-plus — 更高画质下载 Google Photos](https://reddit.com/r/coolgithubprojects/comments/bhx3tw/)** (2019-04, score 128)
- **[Hide YouTube Shorts + home feed (open-source Unhook)](https://reddit.com/r/coolgithubprojects/comments/1tjv3yh/)** (2026-05, score 111)
- **[VPN location spoofer](https://reddit.com/r/coolgithubprojects/comments/vacnl3/)** (2022-06, score 134)
- **[BrowserBoost — 多功能合一的隐私浏览器扩展](https://reddit.com/r/coolgithubprojects/comments/18p8xsg/)** (2023-12, score 115)
- **[AI 在 StackOverflow 上自动答题](https://reddit.com/r/coolgithubprojects/comments/10zhf5b/)** (2023-02, score 117)
- **[Blockman — VSCode 高亮嵌套代码块](https://reddit.com/r/coolgithubprojects/comments/oeg6tb/)** (2021-07, score 252)

## 12. 视觉 / 创意 / 玩具

- **[Real-time color ASCII rendering in Python (NumPy)](https://reddit.com/r/coolgithubprojects/comments/u1fd0u/)** (2022-04, score 251)
- **[Mini Tokyo 3D — 东京公共交通实时 3D 地图](https://reddit.com/r/coolgithubprojects/comments/dgcy3v/)** (2019-10, score 73)
- **[Layered wallpaper engine for Linux](https://reddit.com/r/coolgithubprojects/comments/xhm6hx/)** (2022-09, score 95)
- **[Parallax wallpaper (Linux + Windows)](https://reddit.com/r/coolgithubprojects/comments/xmwriu/)** (2022-09, score 129)
- **[Live Earth Wallpapers — 实时卫星图当壁纸](https://reddit.com/r/coolgithubprojects/comments/ymtvrk/)** (2022-11, score 88)
- **[Lego image/video generator](https://reddit.com/r/coolgithubprojects/comments/ng7vms/)** (2021-05, score 92)
- **[Google Maps at 88mph — 抓 Google Maps 历史卫星图做 GIF](https://reddit.com/r/coolgithubprojects/comments/p0bh9s/)** (2021-08, score 104)
- **[Python script: 真实城市 → Minecraft](https://reddit.com/r/coolgithubprojects/comments/xtn0a7/)** (2022-10, score 104)
- **[r/place 的开源版](https://reddit.com/r/coolgithubprojects/comments/u71nlk/)** (2022-04, score 105)
- **[F3D — 极简跨平台 3D viewer](https://reddit.com/r/coolgithubprojects/comments/12tvg5t/)** (2023-04, score 86)
- **[Mandelbrot fractal renderer (Go)](https://reddit.com/r/coolgithubprojects/comments/rdl87p/)** (2021-12, score 77)
- **[blobs.app — 漂亮的 blob 形状生成器](https://reddit.com/r/coolgithubprojects/comments/m8j4il/)** (2021-03, score 78)
- **[pattern.css — 纯 CSS 背景花纹库](https://reddit.com/r/coolgithubprojects/comments/g757bh/)** (2020-04, score 78)
- **[Persistence — 质量能量守恒的人工生命模拟](https://reddit.com/r/coolgithubprojects/comments/1rnvf2y/)** (2026-03, score 102)
- **[Take video call from inside the Matrix](https://reddit.com/r/coolgithubprojects/comments/xuw6iy/)** (2022-10, score 161)

## 13. 政治 / 社会议题 / 时代标记

这些不一定都"好"但能看出时代氛围:

- **[Whitehouse Reality Check (反 "alternative facts")](https://reddit.com/r/coolgithubprojects/comments/5qenfp/)** (2017-01, score 164) — 川普 1.0 时代的 fact-check 站
- **[github-do-not-ban-us — GitHub 封禁伊朗用户后的抗议](https://reddit.com/r/coolgithubprojects/comments/ci6xqp/)** (2019-07, score 126)
- **[Apollo dev 公布 Reddit App 后端代码反驳 Reddit 指控](https://reddit.com/r/coolgithubprojects/comments/144y8jl/)** (2023-06, score 248) — 2023 Reddit API 撕逼大事件的证据
- **[provaxx — 反疫苗假新闻的社区驱动 fact-check](https://reddit.com/r/coolgithubprojects/comments/b79qj8/)** (2019-03, score 134)
- **[Real-time Iran conflict dashboard + AI briefs](https://reddit.com/r/coolgithubprojects/comments/1rnluwc/)** (2026-03, score 91)
- **[SenateTrades — 跟踪美国参议员股票交易](https://reddit.com/r/coolgithubprojects/comments/q29isb/)** (2021-10, score 90)
- **[Trump Twitter Archive 2 (FactCheck.org 用)](https://reddit.com/r/coolgithubprojects/comments/jp4lha/)** (2020-11, score 75)
- **[Tool to help homeless find local social services](https://reddit.com/r/coolgithubprojects/comments/zwubgq/)** (2022-12, score 84)
- **[Achoo — 用 Pi 追踪儿子哮喘吸入器, 预测后通知校医](https://reddit.com/r/coolgithubprojects/comments/72jokk/)** (2017-09, score 155) — 实际有用的 IoT/ML 应用案例

## 14. 不归类但值得点开

- **[Open Source Palantir on Git](https://reddit.com/r/coolgithubprojects/comments/1tezfl7/)** (2026-05, score 563) — 这是榜眼, 没仔细看是什么, 但分数说明值得
- **[GBA remote play — Raspberry Pi 串流游戏到 Game Boy Advance](https://reddit.com/r/coolgithubprojects/comments/oinljh/)** (2021-07, score 96) — 神级硬件 hack
- **[Cosmos Browser — 通过 SMS 上网, 不需要 WiFi/流量](https://reddit.com/r/coolgithubprojects/comments/2g5v49/)** (2014-09, score 84)
- **[HabitRPG — 提高生产力的 RPG (Habitica 前身)](https://reddit.com/r/coolgithubprojects/comments/240ogz/)** (2014-04, score 100) — 第一周的早期帖子
- **[CodeCrafters' build-your-own-x](https://reddit.com/r/coolgithubprojects/comments/z59zqc/)** (2022-11, score 133) — codecrafters.io 的免费版
- **[Excel formula visualizer](https://reddit.com/r/coolgithubprojects/comments/zi81cj/)** (2022-12, score 101)

---

## 我的个人推荐 (TL;DR 老板时间紧就只点这些)

按"打开后真的研究了你能学到东西"的角度:

1. **Memoir (git for AI memory)** — 跟 fleet/Claude Code memory 思路同源, 必看
2. **LLM contract layer (tool boundary enforcement)** — agent 规则强制, 真问题真方案
3. **Cate (infinite canvas IDE)** — Figma 式编程界面, 看看未来 IDE 形态可能性
4. **Logout4Shell** — 反向利用漏洞救服务器, 安全圈经典脑洞
5. **TabFS** — 用 FUSE 把浏览器 tab 挂载成文件系统, 系统思维的好例子
6. **system-bus-radio** — 在没有发射器的电脑上发无线电, 物理 hack 教科书
7. **build-your-own-x** — 老牌但常青, 任何时候点开都能挖到自己感兴趣的"从零造 X"
8. **Awesome Falsehood** — 知道自己以为对的其实错的, 工程师必读
9. **What happens when you type google.com** — 系统知识体系的极佳整理
10. **Achoo (asthma + Pi + ML + school nurse)** — IoT/ML 不是噱头, 这是真改善生活的例子
