---
title: Notepad++中英混排的换行问题
date: '2025-11-12T17:41:23+08:00'
url: /post/Notepad++-zhong-ying-hun-pai-de-huan-xing-wen-ti.html
tags:
- 技术
draft: false
legacy_key: gmeek-p11
legacy_host: blog.czyouge.xyz
original_url: https://blog.czyouge.xyz/post/Notepad%2B%2B-zhong-ying-hun-pai-de-huan-xing-wen-ti.html
description: Notepad++ 是我日常工作的重要利器。
discussion_url: https://github.com/czyouge/blog/issues/11
---

Notepad++ 是我日常工作的重要利器。不过原生的并不够用，比如在启用自动换行之后会出现中英混排换行显示问题：如果同一行拥有英文+中文，而同时中文内容又比较长的话，Notepad++就会把这句中文当作一个英文单词来处理，从而使得中文被自动分到了下一行，造成阅读与修改的不便。

# 解决方案

1. 安装一个新插件：插件 → 插件管理 → NppExec；
2. Notepad++ 会自动安装并重启；
3. 进入该插件，选择`Execute NppExec Script`，然后保存：

```
sci_sendmsg SCI_SETWRAPMODE SC_WRAP_CHAR  
npp_console 0
```

4. 之后再次进入该插件，选择 `Advanced Options`，在 `Execute this script when Notepad++ starts` 中选择之前保存的脚本，再点击 `OK` 即可。

# 解释

上述代码的作用是是**强制 Notepad++ 以「按字符换行」模式（character wrap mode）显示文本**，从而解决「中英文混排时中文被错误识别为单个英文单词、导致换行异常」的问题。

- `sci_sendmsg SCI_SETWRAPMODE SC_WRAP_CHAR`: `SCI_SETWRAPMODE` 是 Notepad++ 内部所使用的编辑组件 Scintilla 的一个消息命令，用于设置自动换行的方式。参数 `SC_WRAP_CHAR` 表示按「字符」而不是「单词」换行。默认情况下，Notepad++ 使用的是 `SC_WRAP_WORD`（按单词换行），这对于英文很合适，但连续的中文会被当作一个整体「单词」，因此导致整段中文被挤到下一行。改成 `SC_WRAP_CHAR` 后，Notepad++ 会逐字符判断是否需要换行，就能正常断开中文行。
- `npp_console 0`: 关闭 NppExec 的命令输出窗口，让脚本执行时不弹出控制台。
- 把这段脚本设置为「启动时自动执行」，即可让 Notepad++ 每次打开时都启用按字符换行模式，永久修复中英文混排的换行问题。

# 参考链接
- <https://blog.clso.fun/posts/178.html>
- <https://sourceforge.net/p/notepad-plus/discussion/331754/thread/7a813af6/>
