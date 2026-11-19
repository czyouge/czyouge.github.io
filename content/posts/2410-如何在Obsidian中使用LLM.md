---
title: 如何在Obsidian中使用LLM
date: '2024-10-03T19:16:50+08:00'
url: /post/2408-Obsidian-LLM/
tags:
- AI
- Obsidian
- 技术
draft: false
legacy_key: gridea-2408-Obsidian-LLM
legacy_host: www.czyouge.xyz
original_url: https://www.czyouge.xyz/post/2408-Obsidian-LLM/
cover: /post-images/2408-Obsidian-LLM.png
description: 转载自机器之心。 工欲善其事，必先利其器。使用好用的工具可以极大地提升我们生产和学习的效果和效率。今天我们要介绍一套基于 Obsdian
  的 AI 工具组合，其中包含部署本地 LLM 的 Ollama 和两个 Obsdian 插件（BMO ...
---

**转载自[机器之心](https://www.jiqizhixin.com/articles/2024-09-03-4)。**

工欲善其事，必先利其器。使用好用的工具可以极大地提升我们生产和学习的效果和效率。今天我们要介绍一套基于 Obsdian 的 AI 工具组合，其中包含部署本地 LLM 的 Ollama 和两个 Obsdian 插件（BMO Chatbot 和 Ollama）。

这套工具不仅能帮助我们分析笔记、做总结、想标题、写代码，还能帮助我们大开脑洞，为我们续写内容和提供建议。

<!-- more -->

# Obsidian 简介

Obsidian 是目前最受欢迎的笔记工具之一，但它的能力远不止此。你不仅能将其用作笔记本，还可以将其作为你的个人知识库和你的文档生产力工具！许多人甚至将其称为自己的「第二大脑」。

它的优势包括：支持 Markdown、具备丰富的插件生态、支持自定义主题风格、支持 Wiki 式的文档链接、内置关系图谱、基本功能完全免费、完全支持本地存储……

这诸多优势帮助 Obsidian 在全球范围内收获了大量用户。你能在网上看到很多人分享使用该工具学习知识、写作论文、创作小说、计划日程乃至管理生活中一切事物的经验，以至于围绕该工具已经形成了颇具规模的利基市场——模板、课程以及预配置好的资料库（vault）都能成为商品。这也从另一个角度佐证了 Obsidian 的非凡能力。

![](https://czyouge.github.io/post-images/1727954268927.png)

（图注）Obsidian 在哔哩哔哩和 YouTube 上都是非常受欢迎的话题

总之，如果你正在寻找一个好用的学习和生产工具，或者说想要为自己构建一个第二大脑，Obsidian 绝对值得一试！

# 为什么要在 Obsidian 中使用 LLM？

无需怀疑，我们现在正处在大模型时代。它们不仅能帮助我们提升效率和生产力，也能帮助我们创新和探索更多可能性。

人们也已经开发出了 LLM 的许多妙用，这里我们简单展示一些你可以在 Obsidian 中实现的用法，助你见微知著，去探索和发现更多有趣或有用的用法。

第一个例子便是笔者在前一段中忘记了「见微知著」这个成语时，无需额外使用搜索引擎或拨打求助电话，只需问询一下旁边待命的聊天机器人，便很快得到了我想要的结果。


![](https://czyouge.github.io/post-images/1727954724009.gif)


这里用到了 BMO Chatbot 这个插件，其能以聊天机器人的形式将 LLM 整合进你的 Obsidian。该插件还能让你基于当前文档进行聊天。如下所示，我们让 LLM 用汉语总结了这篇英语报道并建议了一些标题：


![](https://czyouge.github.io/post-images/1727954731194.gif)


当然，帮你续写故事自然也不在话下。下面我们让 LLM 帮助续写弗雷德里克·布朗那篇著名的世界上最短的小说：

> 地球上最后一个人独自坐在房间里，这时，忽然响起了敲门声……


![](https://czyouge.github.io/post-images/1727954738077.gif)


这里使用了另一个插件 Ollama 和预配置的命令，其提词为：「根据以上内容，续写故事。要求续写200字，人物风格保持一致，同时为后文留下悬念。」

另外，可以明显看到这个插件的运行速度更慢一点。这是因为此处使用了本地安装的 LLM——一个 8B 版本的 llama3.1 模型，其运行速度受限于当前的硬件。

好了，示例就到这里。下面来看如何安装和使用这些插件和 LLM 吧。

# 安装本地 LLM

对我们大多数人来说，本地计算机能够运行的 LLM 的性能自然无法与 OpenAI 等大公司提供的在线服务相比，但本地 LLM 的最大优势是数据的隐私和安全——使用本地 LLM，你的所有运算都在自己的计算机上完成，不必担心你的数据被传输给服务提供商。

当然，如果你并不在意自己的笔记隐私，那么使用在线服务也能很好地完成你的任务，也就完全可以略过这一步骤了。

为方便本地使用 LLM，我们要用到一个名叫 Ollama 的工具。[Ollama](https://github.com/ollama/ollama) 是一个非常好用的本地部署 LLM 的工具，适合任何人使用，下载安装即可，地址：https://github.com/ollama/ollama/releases

之后，进入 Ollama 支持的模型库：https://ollama.com/library ，根据你自身的需求和计算机硬件选择模型，之后运行相应的代码即可。比如如果你想安装一个 8B 参数的经过指令微调和 Q8_0 量化的 Llama 3.1 模型，就运行：`ollama run llama3.1:8b-instruct-q8_0`

![](https://czyouge.github.io/post-images/1727954303764.png)

当然，你也可以安装多个不同规模或针对不同任务（比如编程）微调过的模型，这样可以方便在需求不同时在速度和生成效果之间权衡选择。

# 安装和配置 BMO ChatBot 和 Ollama 插件

这两个插件都已上线 Obsidian 的社区插件市场，搜索、下载并启用即可。

![](https://czyouge.github.io/post-images/1727954320943.png)

## 配置 BMO Chatbot 插件

进入选项，你可以在 General 设置中选择你已经安装的本地模型或配置的在线模型。如下图所示，我这里本地安装了一个 Llama 3.1 和一个 Llama 3，同时配置了 OpenRouter 的 API（可访问大量模型）和一个智谱的在线语言模型 GLM-4-Flash。下面可以设置最大 token 数、温度（0-1 之间，值越大生成的文本越有创意）以及选择是否索引当前笔记。

![](https://czyouge.github.io/post-images/1727954337186.png)

Prompts 中可以通过笔记设置系统提词。

而在更下面的 API Connections 区域，你可以配置在线模型。

![](https://czyouge.github.io/post-images/1727954351855.png)

配置完成之后，便可以通过 Obsidian 右边栏或使用 Ctrl+P/Cmd+P 快捷键使用这些 LLM 了。

除了使用 BMO 聊天机器人，该插件还支持用 LLM 重命名当前文档以及使用选中文本作为提词生成内容。

![](https://czyouge.github.io/post-images/1727954378246.png)

## 配置 Ollama 插件

Ollama 插件仅支持前面通过 Ollama 安装的本地模型，但其优势是可以预配置常用提词命令，之后通过 Ctrl+P/Cmd+P 就能方便调用。

![](https://czyouge.github.io/post-images/1727954392276.png)

下面是一个代码生成示例：

![](https://czyouge.github.io/post-images/1727954428216.gif)

# 结语

Obsidian 结合 LLM 工具能为我们的学习和生产工作带来极大的便利。Obsidian 作为一款强大的笔记工具，不仅支持丰富的插件生态，还能通过本地部署 LLM 来提升我们的效率和创新力。

安装和使用 BMO Chatbot 和 Ollama 插件，让我们能够轻松地将 LLM 融入 Obsidian，从而实现笔记分析、总结、标题生成、内容续写等多种功能。这不仅能让我们节省时间和精力，还能激发我们的创造力。

当然，在使用这些工具的同时，我们也应关注数据隐私和安全问题。本地部署 LLM 能够保证我们的数据不离开个人设备，从而降低数据泄露的风险。

总之，Obsidian+LLM 为我们打开了一扇新的大门，让我们能在信息爆炸的时代更好地利用科技力量，提升自我。
