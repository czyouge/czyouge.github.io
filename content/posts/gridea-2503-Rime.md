---
title: 如何将特定繁体字词加入Rime输入法候选项
date: '2025-03-04T20:38:03+08:00'
url: /post/2503-Rime/
tags:
- RIME
draft: false
legacy_key: gridea-2503-Rime
legacy_host: www.czyouge.xyz
original_url: https://www.czyouge.xyz/post/2503-Rime/
cover: /post-images/2503-Rime.png
description: 我之前成功实现了让 Rime 输入法支持简繁混合输入，但实际用下来发现只是徒增烦恼，因为这样会打乱原本手熟的排序，极大地增加输入的时间和精力成本，于是输入法又变成了纯简体版本。
  但最近，因为工作，需要输入「昇」这个特定的繁体字，而简体字版本...
---

我之前成功实现了[让 Rime 输入法支持简繁混合输入](https://www.czyouge.xyz/post/2404-rime-jianfanhunshu/)，但实际用下来发现只是徒增烦恼，因为这样会打乱原本手熟的排序，极大地增加输入的时间和精力成本，于是输入法又变成了纯简体版本。

但最近，因为工作，需要输入「昇」这个特定的繁体字，而简体字版本的 Rime 是无法直接输入这个字的——即使把「昇」加入到自定义词表中也无法实现。

研究了 2 个晚上，终于在 Claude 的帮助下找到了解决方案。

<!-- more -->

实际上，Claude 给出了不少方案，但实测下来目前只有这一个能行。

该方案基于 Lua 脚本。

第一步，在 `用户文件夹/Lua` 中新建一个 Lua 脚本，比如 `namex.lua`。脚本内容如下：

```
-- 特殊字符处理
local special_chars = {
  ["升"] = "昇",
  ["龙"] = "龍"
  -- 可以添加更多特殊单字对
}

-- 特殊词组处理
local special_words = {
  ["升腾"] = "昇腾"
  -- 可以添加更多特殊词组对
}

local function filter(input, env)
  -- 记录已经处理过的特殊字符
  local handled = {}
  
  -- 第一遍：正常输出所有候选项并标记特殊字符/词组
  for cand in input:iter() do
    yield(cand)
    
    -- 检查单字
    if special_chars[cand.text] then
      handled[cand.text] = true
      
      -- 如果找到了特殊字符，立即在后面添加对应的繁体字符
      if not handled[special_chars[cand.text]] then
        local fan_text = special_chars[cand.text]
        local new_cand = Candidate("char", cand.start, cand._end, fan_text, "")
        new_cand.quality = cand.quality - 1  -- 稍微降低权重
        yield(new_cand)
        handled[fan_text] = true
      end
    end
    
    -- 检查词组
    if special_words[cand.text] then
      handled[cand.text] = true
      
      -- 如果找到了特殊词组，立即在后面添加对应的繁体词组
      if not handled[special_words[cand.text]] then
        local fan_text = special_words[cand.text]
        local new_cand = Candidate("word", cand.start, cand._end, fan_text, "")
        new_cand.quality = cand.quality - 1  -- 稍微降低权重
        yield(new_cand)
        handled[fan_text] = true
      end
    end
  end
end

return filter
```

如果想要新增繁体字或词组，可以在上面对应位置补充。

或者，也可以使用这个更简单的脚本：

```
-- 特殊字符处理
local special_pairs = {
  ["升"] = "昇"
  -- 可以添加更多特殊字符对
}

local function filter(input, env)
  -- 记录已经处理过的特殊字符
  local handled = {}
  
  -- 第一遍：正常输出所有候选项并标记特殊字符
  for cand in input:iter() do
    yield(cand)
    
    -- 检查是否存在特殊字符对
    if special_pairs[cand.text] then
      handled[cand.text] = true
    elseif special_pairs[cand.text] then
      handled[cand.text] = true
    end
    
    -- 如果找到了特殊字符，立即在后面添加对应的繁体/简体字符
    if special_pairs[cand.text] and not handled[special_pairs[cand.text]] then
      local fan_text = special_pairs[cand.text]
      local comment = "繁体"
      local new_cand = Candidate("char", cand.start, cand._end, fan_text, comment)
      new_cand.quality = cand.quality - 1  -- 稍微降低权重
      yield(new_cand)
      handled[fan_text] = true
    end
  end
end

return filter
```

第二步，在 `rime.lua` 文件中新增一行：

```
namex_filter = require("namex")
```

第三步，在 `你的输入方案.custom.yaml` 文件中新增：

```
engine/+:
  filters/+:
    - lua_filter@namex_filter
```

完工。重新部署即可。

 ![](https://czyouge.github.io/post-images/1741091924354.png)
