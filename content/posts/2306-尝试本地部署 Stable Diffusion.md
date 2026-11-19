---
title: 尝试本地部署 Stable Diffusion
date: '2023-06-02T18:00:00+08:00'
url: /post/2306-stable-diffusion/
tags:
- 人工智能
- 技术
draft: false
legacy_key: gridea-2306-stable-diffusion
legacy_host: www.czyouge.xyz
original_url: https://www.czyouge.xyz/post/2306-stable-diffusion/
description: 之前试玩了一下 Midjourney，通过 Discord 访问，但很快我就把免费体验次数耗完了，于是跑去淘宝买了一个月的共享账户继续试玩。然而新鲜感两三天就过去了，我就基本很少碰了。这两天又来了点兴趣，试了下本地部署
  Stable Dif...
---

之前试玩了一下 Midjourney，通过 Discord 访问，但很快我就把免费体验次数耗完了，于是跑去淘宝买了一个月的共享账户继续试玩。然而新鲜感两三天就过去了，我就基本很少碰了。这两天又来了点兴趣，试了下本地部署 Stable Diffusion。

我主要参考了这篇文章《[本地部署Stable Diffusion教程，亲测可以安装成功](https://blog.csdn.net/weixin_43905975/article/details/129988104)》by Pancras Wen。

基本上我按照其描述的过程安装的，只遇到一点小问题。

首先是下载 git 和 Python，他这里建议安装 Python 3.10.9，没有说明原因，我也不知道为啥。

<!-- more -->

然后下载 stable-diffusion-webui 软件库：新建一个文件夹，然后通过 git 克隆：

`git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git`

下载完成后，运行 webui-user.bat 批处理文件，让其自动下载安装其余组件。

如果过程中遇到 pip 更新提示，就新开一个 cmd 然后运行绿色的提示命令即可。

这个过程在克隆 taming-transformers 和 CodeFormer 时遇到了问题，出现了 error code 128，[可以参考这里的报告](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/5345)。

对于 taming-transformers，我重新启动 webui-user.bat 批处理成功解决了，但是等了不少时间。

对于 CodeFormer，重开多次 webui-user.bat 也没能解决，于是我换了 git bash 来克隆，完成后再运行 webui-user.bat。

后面就没啥问题，继续下载。

之后我们就能通过浏览器访问 <http://127.0.0.1:7860> 来调用 Stable Diffusion。

还是很方便使用的，各个参数设置都有说明，悬停鼠标便能看到。

试着调用了几次默认设置，感觉效果相当差。

![](https://czyouge.github.io/post-images/1685706224129.png)

*图 1：默认设置的结果，prompt 为「a man is standing in front of a tank with the muzzle pointing at the man」*

为了生成高质量的图像，自然需要合适的设置；其中采样器的选择是非常重要的。这里有一篇指南值得参考：《[Stable Diffusion Samplers: A Comprehensive Guide](https://stable-diffusion-art.com/samplers/)》，其中给出了一些使用建议：

1. 如果想要使用相对新的模型，快速生成，质量好，可以选择：
   - **DPM++ 2M Karras**，执行 20-30 步
   - **UniPC**，执行 20-30 步
2. 如果你想要高质量图像，但不在乎收敛情况，可以选择：
   - **DPM++ SDE Karras**，执行 8-12 步（注意：速度更慢）
   - **DDIM**，执行 10-15 步
3. 如果想要生成的结果稳定，可再现，就不要使用老式采样器，即 Euler a、DPM2 a、DPM++ 2S a、DPM++ 2S a Karras。
4. 如果偏好简单的选择，可以使用 **Euler** 和 **Heun**；Heun 的步数不宜过多，以节省时间。

![](https://czyouge.github.io/post-images/1685706238622.png)

*图 2：UniPC 采样器执行 22 步的结果，prompt 为「a crying Chinese woman with iron chain around the neck」*

我也看了看另外两篇教程，这里索引一下：

- [The Most Complete Guide to Stable Diffusion Parameters](https://blog.openart.ai/2023/02/13/the-most-complete-guide-to-stable-diffusion-parameters/)
- [Stable Diffusion AI: Absolute beginner’s guide (+online demo)](https://stable-diffusion-art.com/beginners-guide/)
