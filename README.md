# 虫子游戈的博客

这是唯一需要日常维护的 Hugo 源码。文章以本地 Markdown 文件保存，GitHub Actions 负责生成并发布网页。

## 从哪里开始

- **写文章**：`content/posts/`。
- **改独立页面**：`content/pages/`，例如 `about.md`、`friends.md`。
- **放图片**：`static/post-images/`，正文使用 `/post-images/图片名.png` 引用。

`static/` 是本地素材目录，发布后的网址不包含 `static`。例如本地 `static/post-images/example.png` 在模板中写作 `{{ "post-images/example.png" | relURL }}`，在 Markdown 中写作 `/post-images/example.png`。

网站头像仍读取 `static/blog/avatar.png`，模板会自动生成带内容指纹的根目录图片地址。不要手动改回 `/blog/avatar.png`：GitHub Pages 会把 `/blog/` 路径重定向到旧项目站。替换原图后重新发布即可，图片地址会自动更新。
- **本地预览**：双击根目录的 **预览博客.cmd**，浏览器打开 <http://localhost:1313/>。关闭该命令窗口即可停止预览。
- **新建文章**：双击 **新建文章.cmd**，输入标题和永久地址标识；或直接复制现有 Markdown 文件修改。
- **首次上线**：见 [上线与回退说明](docs/上线与回退.md)。

你的电脑已有 Python。便携版 Hugo 放在本地 `.tools/` 中，不需要修改系统环境；换电脑后第一次预览会从 Hugo 官方下载固定版本并验证校验和。程序不上传到仓库。

## 一篇文章的样子

```yaml
---
title: 我的一篇新文章
date: 2026-11-19T12:00:00+08:00
url: /post/my-new-story/
tags: [随想]
draft: true
---

从这里开始写正文。

![图片说明](/post-images/example.png)
```

`title` 是显示标题，可以随时改。`url` 是永久地址，文章发布后不要更改。`draft: true` 表示不生成正式网页；准备发布时改为 `false`。未来日期的文章在日期到达后的下一次构建时才会出现；这里没有定时发文服务。

`content/` 内的文件提交到公开 GitHub 仓库后，源码本身可被阅读，即使文章标成草稿。尚不准备上传的文字放 `local-drafts/`，该文件夹已被 Git 忽略。本次找到的未上线本地推荐页也保存在这里。

本地预览包含 `content/` 中的草稿，关闭 Google Analytics，不计入正式访问数据。

## 日常发布

在 GitHub Desktop 中添加这个本地仓库（E:\Blog\hugo-blog），使用 `master` 分支。此后修改文章、填写提交说明、点击 **Commit to master**，再点击 **Push origin**，主站会自动构建发布。只需维护这一个仓库。

正式入口只有 **https://www.czyouge.xyz/**。原来第二个博客的 17 篇文章也已经迁入主站，保留原来的 `.html` 路径。按你的决定，第二个仓库不再定时同步或维护文章，只保留备份和旧域名的静态跳转入口。日常只编辑、提交本仓库即可。

## 独立页面

在 `content/pages/` 新建 `hello.md`：

```yaml
---
title: 一个新页面
url: /hello/
---

页面正文。
```

如果想放到顶部导航，在 `hugo.toml` 中添加一条 `[[menus.main]]`，设置 `name`、`url` 和显示顺序 `weight`。

## 旧内容的约定

- 文章文件统一按 `年月-标题.md` 命名，例如 `2504-中英混排工具.md`。年月取自文章发布日期；新建文章脚本也会自动添加年月。文件名用于本地排序，网页地址由 `url` 字段固定。
- 已发布内容共 138 个：137 篇文章及一个不显示在文章列表中的作品页。
- 原有日期、标签、文章地址、图片路径和可检测的旧标题锚点已保留。
- `original_url` 记录历史地址；若有 `canonical_url`，它是当前主站地址。不要随意更改已经发布的永久路径。
- `legacy_key` 关联旧标题锚点。通常保持不动；如果重排旧文章小节，请同步调整 `data/legacy_headings.json`。
- 旧站独立的排版工具保留在 `/tools/typesetting/`。
- 两个 RSS 订阅入口 `/rss.xml`、`/atom.xml` 都保留。
- 统一使用现有 GA4 标识 `G-0Z3PHKTB0H`。未添加新的统计平台，未迁移或删除 Google 中已有数据。旧主站的 `UA-` 标识不再注入。
- 原有 GitHub Issues 保留；文章底部提供原讨论入口。

## 目录职责

| 目录或文件 | 用途 |
|---|---|
| `content/` | 日常编辑的 Markdown 正文和标签页面 |
| `static/` | 图片、脚本、样式、独立工具等原样发布的文件 |
| `layouts/` | 网站页面模板 |
| `hugo.toml` | 标题、菜单、统计和构建配置 |
| `data/legacy_urls.json` | 旧网址清单，发布时自动检查 |
| `data/legacy_headings.json` | 旧文章小节锚点 |
| `docs/` | 迁移记录、上线与回退说明 |
| `public/` | 自动生成的网页，不要编辑，也不上传源码仓库 |
| `local-drafts/` | 只保存在本机的未上传草稿 |

## 技术检查

```powershell
python scripts/build.py
```

GitHub Actions 会运行同样的检查，出现缺失的旧路径、旧锚点、本地资源或损坏的 RSS 时，停止发布。
