---
title: 如何给 RIME 配置多行输入？
date: '2026-07-04T17:23:23+08:00'
url: /post/ru-he-gei- RIME -pei-zhi-duo-xing-shu-ru-？.html
tags:
- 技术
- Vibe Coding
- 工具
draft: false
legacy_key: gmeek-p18
legacy_host: blog.czyouge.xyz
original_url: https://blog.czyouge.xyz/post/ru-he-gei-%20RIME%20-pei-zhi-duo-xing-shu-ru-%EF%BC%9F.html
canonical_url: https://www.czyouge.xyz/post/ru-he-gei-%20RIME%20-pei-zhi-duo-xing-shu-ru-%EF%BC%9F.html
description: RIME 最大的魅力之一，就是几乎所有功能都可以自定义。
discussion_url: https://github.com/czyouge/blog/issues/18
---

RIME 最大的魅力之一，就是几乎所有功能都可以自定义。但当我想给 RIME 添加一个**多行文本模板**时，却发现一个令人意外的问题：**词库根本不支持多行内容。**

例如，我希望输入：

```text
sig
```

候选词直接变成：

```text
第一行
第二行
第三行
```

甚至更复杂一点：

```text
prompt
```

展开为：

```text
你是一名 AI 助手。

要求：

1. 回答准确。
2. 回答简洁。
3. 使用 Markdown。
```

然而，无论是在 `.dict.yaml` 中使用 YAML 的多行字符串，还是尝试 `\n`、`\u000A` 等转义字符，都无法实现真正的多行输入。

最终，我选择使用 **librime-lua** 实现这一功能。下面记录一下整个配置过程，以及踩过的坑。

# 为什么词库做不到？

RIME 的词库（`.dict.yaml`）本质上是一张表，每一条记录对应一行：

```text
编码    候选词    权重
```

也就是说，一条记录不能包含真正的换行符。

例如下面这种写法：

```yaml
sig    第一行
第二行
第三行
```

词库会直接解析失败。

即使写成：

```yaml
sig    第一行\n第二行
```

最终输入出来的也只是：

```text
第一行\n第二行
```

而不是：

```text
第一行
第二行
```

因此，如果希望提交真正的多行文本，就必须借助 Lua。

# 编写 Lua Translator

首先，在 RIME 用户目录下新建：

```text
lua/multiline.lua
```

内容如下：

```lua
local M = {}

local templates = {
    sig = [[
第一行
第二行
第三行
]],

    prompt = [[
你是一名 AI 助手。

要求：

1. 回答准确。
2. 回答简洁。
3. 使用 Markdown。
]],

    addr = [[
张三
北京市朝阳区
XX 路 XX 号
100000
]],
}

function M.func(input, seg, env)
    local text = templates[input]

    if text then
        yield(Candidate(
            "multiline",
            seg.start,
            seg._end,
            text,
            "〔模板〕"
        ))
    end
end

return M
```

这里维护了一个 Lua 表，当输入 `sig`、`prompt` 等编码时，就返回对应的多行文本。


# 加载 Lua 模块

然后编辑 `rime.lua`，增加一行：

```lua
multiline = require("multiline")
```


# 修改 Schema

然后在对应输入方案的 `*.custom.yaml` 中加入：

```yaml
patch:
  engine/translators/+:
    - lua_translator@multiline
```

重新部署即可。

之后输入：

```text
sig
```

候选词就会变成：

```text
第一行
第二行
第三行
```

# 可以继续优化

上面的实现只是最简单的版本。

如果模板越来越多，把所有内容都写在 Lua 里会比较麻烦。

更推荐的做法是：

```text
Rime/
├── lua/
│   └── multiline.lua
└── multiline.txt
```

把所有模板都放在 `multiline.txt` 中，Lua 启动时自动读取。

这样新增模板只需要修改文本文件，而无需编辑 Lua 代码，维护起来会方便得多。
