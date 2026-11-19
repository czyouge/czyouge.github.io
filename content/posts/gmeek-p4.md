---
title: 如何在手机上本地运行LLM
date: '2025-05-11T22:26:25+08:00'
url: /post/ru-he-zai-shou-ji-shang-ben-di-yun-xing-LLM.html
tags:
- 技术
- AI
draft: false
legacy_key: gmeek-p4
legacy_host: blog.czyouge.xyz
original_url: https://blog.czyouge.xyz/post/ru-he-zai-shou-ji-shang-ben-di-yun-xing-LLM.html
canonical_url: https://www.czyouge.xyz/post/ru-he-zai-shou-ji-shang-ben-di-yun-xing-LLM.html
description: '> 基本无用的技能又增加了。'
discussion_url: https://github.com/czyouge/blog/issues/4
---

> 基本无用的技能又增加了。

借助 Termux 和 llama-cpp，可以在安卓手机上本地运行 LLM。下面我将记录我研究多个博客以及咨询 ChatGPT 后得到的操作过程，但其中某些步骤是不必要的，我没有能力分辨，就一并记录下来了。以便后续回顾。

首先，下载并安装 [Termux](https://termux.dev/en/)。

> Termux 是一款 Android 终端模拟器和 Linux 环境应用，无需 root 权限或设置即可直接运行。系统会自动安装精简的基础系统，其他软件包则可通过 APT 软件包管理器获取。

安装完成后可以运行一次 `pkg upgrade` 以更新软件包。

之后，需要安装所需要的环境软件包，运行：

```
pkg install cmake clang make git python-pip llama-cpp
```

Termux 还会自动安装一些依赖：

![](https://i.imgur.com/474jzXW.jpeg)

接下来，安装 llama.cpp，这需要一定时间:

```
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build
cmake --build build --config Release
```

接下来，继续安装一些所需的软件包：

```
pip install transformers accelerate sentencepiece
```

这里我遇到一个报错：pip 安装后端依赖的子进程没有成功运行。但该报错没有影响到后续步骤，所以我也没有深究。

接下来，下载安装一个 LLM 模型，这里我们以 unsloth 做的 Qwen 3 0.6B 的一个量化版为例，运行：

```
cd llama.cpp
llama-cli -hf unsloth/Qwen3-0.6B-GGUF:Q8_0
```

 操作成功之后，便可以与这个在手机上本地运行的 Qwen 3 聊天了。

 
![](https://i.imgur.com/3TrGlLX.jpeg)


 这个 0.6B 的模型在我的一加7T上跑起来速度还是很快的，就是回答质量堪忧。
