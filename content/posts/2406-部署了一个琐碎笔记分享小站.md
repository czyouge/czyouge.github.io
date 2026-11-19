---
title: 部署了一个琐碎笔记分享小站
date: '2024-06-01T09:42:55+08:00'
url: /post/2406-quartz/
tags:
- Quartz
- 工具
draft: false
legacy_key: gridea-2406-quartz
legacy_host: www.czyouge.xyz
original_url: https://www.czyouge.xyz/post/2406-quartz/
description: 尝试用 Quartz 和 Github Pages 部署了一个用于分享琐碎笔记的小站，虽然对于要分享些什么，我还毫无计划…… 地址：notes.czyouge.xyz
  我参考的教程包括： YouTube 视频：How to publis...
---

尝试用 Quartz 和 Github Pages 部署了一个用于分享琐碎笔记的小站，虽然对于要分享些什么，我还毫无计划……

地址：[notes.czyouge.xyz](https://notes.czyouge.xyz/)

<!-- more -->

我参考的教程包括：

- YouTube 视频：How to publish your notes for free with Quartz

<iframe width="560" height="315" src="https://www.youtube.com/embed/6s6DT1yN4dw?si=QRPMzBzeeYuTFxNG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

- [How to publish Obsidian notes with Quartz on GitHub Pages](https://notes.nicolevanderhoeven.com/How+to+publish+Obsidian+notes+with+Quartz+on+GitHub+Pages)

最后，从[官网](https://quartz.jzhao.xyz/authoring-content)引用一些 Quartz 原生支持的 frontmatter 格式，以备查询：

- `title`: Title of the page. If it isn’t provided, Quartz will use the name of the file as the title.
- `description`: Description of the page used for link previews.
- `aliases`: Other names for this note. This is a list of strings.
- `tags`: Tags for this note.
- `draft`: Whether to publish the page or not. This is one way to make [pages private](https://quartz.jzhao.xyz/features/private-pages) in Quartz.
- `date`: A string representing the day the note was published. Normally uses `YYYY-MM-DD` format.
