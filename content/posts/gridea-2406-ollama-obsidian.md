---
title: 本地部署LLM并集成到Obsidian
date: '2024-06-30T00:00:00+08:00'
url: /post/2406-ollama-obsidian/
tags:
- AI
- 技术
- LLM
- Obsidian
- Ollama
draft: false
legacy_key: gridea-2406-ollama-obsidian
legacy_host: www.czyouge.xyz
original_url: https://www.czyouge.xyz/post/2406-ollama-obsidian/
cover: https://i.imgur.com/ej4tvXN.png
description: ollama 是一个非常好用的本地部署 LLM 的工具，适合任何人使用，下载安装即可。 安装 LLM 我安装了两个大模型：8B 版本的 Llama
  3 和 27B 版本的 Gemma 2。为此，分别运行： ollama run llam...
---

[ollama](https://github.com/ollama/ollama) 是一个非常好用的本地部署 LLM 的工具，适合任何人使用，下载安装即可。

<!-- more -->

![](https://i.imgur.com/ej4tvXN.png)


## 安装 LLM

我安装了两个大模型：8B 版本的 Llama 3 和 27B 版本的 Gemma 2。为此，分别运行：

`ollama run llama3` 和 `ollama run gemma2:27b`

之后，我们可以需要一个方便使用的交互界面。我选择了 [Open WebUI](https://github.com/open-webui/open-webui)，使用 docker 安装：

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

如果想使用英伟达 GPU 来驱动 Open WebUI，可以：

```
docker run -d -p 3000:8080 --gpus all --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda
```

之后只需在浏览器打开 http://localhost:3000/ 即可使用，界面与 ChatGPT 相当类似：

![](https://i.imgur.com/hsC6sJc.png)

## 集成到 Obsidian

首先，在 Obsidian 的社区插件市场下载并启用 Ollama 插件，然后配置好你想使用的指令和模型。配置完成后记得重启一次 Obsidian，如此才能生效。

![](https://i.imgur.com/z3xA6jM.png)

之后，在你需要使用 LLM 的文档中直接点击 `Ctrl+P` 或选中文本后 `Ctrl+P` 唤起命令工具，搜索你的命令名称，如上图中的「汉语总结」，调用即可。

![](https://i.imgur.com/9yAVvBh.gif)
