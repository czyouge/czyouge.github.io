---
title: Notepad++实现正则表达式查找并替换
date: '2025-11-05T17:49:56+08:00'
url: /post/Notepad++-shi-xian-zheng-ze-biao-da-shi-cha-zhao-bing-ti-huan.html
tags:
- 技术
draft: false
legacy_key: gmeek-p10
legacy_host: blog.czyouge.xyz
original_url: https://blog.czyouge.xyz/post/Notepad%2B%2B-shi-xian-zheng-ze-biao-da-shi-cha-zhao-bing-ti-huan.html
description: Notepad++ 的宏功能很强大，但很多时候，光是录制宏并不够用。
discussion_url: https://github.com/czyouge/blog/issues/10
---

Notepad++ 的宏功能很强大，但很多时候，光是录制宏并不够用。不过 Notepad++ 支持编辑宏，就方便多了。

比如，我们可以通过编辑宏来实现正则表达式替换。

举个例子，如果要将「论文」、「论文地址」和「论文链接」都替换成「Paper」，可以使用以下宏：


```
<Macro name="替换成Paper" Ctrl="no" Alt="no" Shift="no" Key="0">
<Action type="3" message="1700" wParam="0" lParam="0" sParam="" />
<Action type="3" message="1601" wParam="0" lParam="0" sParam="论文(地址|链接)?" />
<Action type="3" message="1625" wParam="0" lParam="2" sParam="" />
<Action type="3" message="1602" wParam="0" lParam="0" sParam="Paper" />
<Action type="3" message="1702" wParam="0" lParam="770" sParam="" />
<Action type="3" message="1701" wParam="0" lParam="1609" sParam="" />
</Macro>
```

这里的重点是第三行的 `lParam` 参数，其控制着**搜索模式**：

- 0 → 普通文本
- 1 → 宏录制状态（可能带大小写/全字匹配）
- 2 → 正则表达式
