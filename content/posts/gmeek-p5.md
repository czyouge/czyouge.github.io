---
title: 为Gmeek博客整合Google Analytics
date: '2025-05-15T21:29:37+08:00'
url: /post/wei-Gmeek-bo-ke-zheng-he-Google Analytics.html
tags:
- 技术
draft: false
legacy_key: gmeek-p5
legacy_host: blog.czyouge.xyz
original_url: https://blog.czyouge.xyz/post/wei-Gmeek-bo-ke-zheng-he-Google%20Analytics.html
description: '想为 [Gmeek](https://meekdai.com/Gmeek.html) 博客整合 Google Analytics？


  方法很简单。'
discussion_url: https://github.com/czyouge/blog/issues/5
---

想为 [Gmeek](https://meekdai.com/Gmeek.html) 博客整合 Google Analytics？

方法很简单。首先在`管理→数据收集和修改→数据流` 中找到你的「衡量 ID」，然后用其替换掉以下代码中的两处 `G-XXXXXXXXXX`。

```
<script async src='https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX'></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-XXXXXXXXXX');</script>
```

之后，复制已替换的代码，将其粘贴到 `config.json` 文件中的 `"allHead"` 中。

最后，commit 并运行一次 `build Gmeek`。

build 完成后，可以在 Google Analytics 测试一下是否成功。

同样，进入`管理→数据收集和修改→数据流`，然后在下方「Google 代码」中选择「配置代码设置」，进入后选择「管理」，再选择「添加此 Google 代码」，选择「手动添加」。

接下来，在「测试您的网站（可选）：」中输入你的博客地址，点击测试，查看结果。

![](https://i.imgur.com/mgY6Wrd.png)
