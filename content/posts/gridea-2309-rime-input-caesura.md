---
title: RIME输入法顿号直接上屏
date: '2023-09-19T20:00:00+08:00'
url: /post/2309-rime-input-caesura/
tags:
- RIME
- 工具
draft: false
legacy_key: gridea-2309-rime-input-caesura
legacy_host: www.czyouge.xyz
original_url: https://www.czyouge.xyz/post/2309-rime-input-caesura/
description: 使用小狼毫输入法（RIME）时，按键 \ 会出现三个候选项，但除了 、 之外其它两个完全用不上，这就很影响效率了。 我按照简书上这个方案解决了问题。
  我使用的是小鹤双拼。 首先进入用户文件夹，新建一个 double_pinyin_fly...
---

使用小狼毫输入法（RIME）时，按键 `\` 会出现三个候选项，但除了 `、` 之外其它两个完全用不上，这就很影响效率了。

![](https://czyouge.github.io/post-images/1695125600079.png)

我按照[简书上这个方案](https://www.jianshu.com/p/d7358c8bd9a4)解决了问题。

<!-- more -->

我使用的是小鹤双拼。

首先进入用户文件夹，新建一个 `double_pinyin_flypy.custom.yaml` 文件，然后写入：

```
patch:
  punctuator/full_shape:
    '\' : '、'
    '/' : '/'
    # "`": {commit: "·"}
  punctuator/half_shape:
    '\' : '、'
    '/' : '/'
    # "`": {commit: "·"}
```

保存，然后重新部署即可。
