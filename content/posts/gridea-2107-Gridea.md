---
title: 用Gridea搭建博客竟如此简单
date: '2021-07-20T22:21:53+08:00'
url: /post/2107-Gridea/
tags:
- Gridea
draft: false
legacy_key: gridea-2107-Gridea
legacy_host: www.czyouge.xyz
original_url: https://www.czyouge.xyz/post/2107-Gridea/
cover: /post-images/Gridea.png
description: 我曾在大学时试过用 WordPress 搭建博客，但其复杂程度超过了我的掌控能力，后来也反反复复多次使用过 GitHub Jekyll，但总觉得不好用，坚持不了几天。到后来，我就更愿意使用现成的博客服务平台了，比如新浪博客、网易
  Lofte...
---

我曾在大学时试过用 WordPress 搭建博客，但其复杂程度超过了我的掌控能力，后来也反反复复多次使用过 GitHub Jekyll，但总觉得不好用，坚持不了几天。到后来，我就更愿意使用现成的博客服务平台了，比如新浪博客、网易 Lofter、简书等，但国内博客平台存在严重的审查问题，所以也始终不称意。然后我就开始用 Blogger，体验很差，但好在没了审查，所以也就忍受了几年。但如此却将我自己的故事挡在了墙外，常会让我感到遗憾。尽管我尝试使用 ZeroNet 来发布文章，但这个分布式网络可以说是一个鬼城，并没有几个真正严肃的真实用户。

今天下午，我偶然在知乎上看到了一篇文章《[完全小白教程：使用Github Pages和Gridea搭建个人博客](https://zhuanlan.zhihu.com/p/165948546)》，发现了 [Gridea](https://gridea.dev/) 这个超简单的博客工具，简单了解了下发现这正是我需要的东西——简简单单就能免费创建一个能受自己控制且（几乎）不被审查的博客。**真的非常简单！**

下面我将分步骤描述我的创建和配置过程，其中包括注册配置 GitHub 代码库、下载配置 Gridea 客户端、选择合适的博客主题、绑定域名、配置谷歌分析、发布文章。

<!-- more -->

## 1 注册配置 GitHub 代码库

首先注册一个 GitHub 账户。如果你不打算使用自己的域名，那么请慎重选择你的「用户名」，因为它会以「用户名.github.io」这一形式作为你的博客地址。

注册完毕后，点击右上角＋，单击 New repository，新建代码库：

![](https://czyouge.github.io/post-images/image-20210720202628904.png)

之后在 Repository name 填写你的「用户名.github.io」，然后创建代码库：

![](https://czyouge.github.io/post-images/image-20210720202928323.png)

此时你会得到一个空的代码库。

点击右上角头像，进入 Settings，找到 Developer Settings，选择 Personal access tokens，然后点击 Generate new token：

![](https://czyouge.github.io/post-images/image-20210720204256133.png)

然后在 Note 处随意填写你的备注，勾选 repo，然后点击下方生成 token：

![](https://czyouge.github.io/post-images/image-20210720204126978.png)

复制这行 `ghp_` 开头的 token。请注意蓝色警告：**退出该页面后将无法看到这串字符**。如果失误丢失了这个 token 也别慌，你可以重复上述步骤再生成一个新的。

![](https://czyouge.github.io/post-images/image-20210720214833020.png)

## 2 下载配置 Gridea 客户端

在 [Gridea 官网](https://gridea.dev/)或[其 GitHub 代码库](https://github.com/getgridea/gridea/releases)下载对应操作系统的客户端并安装。

首先进入「远程」进行配置。平台选择 GitHub Pages，域名选择 https:// 并填写你的「用户名.github.io」，仓库名称也是「用户名.github.io」，分支可填写 master 或 main，用户名便是你的用户名，邮箱可选，令牌则粘贴上面的 token。如果你有自己的域名，就填入 CNAME；如果否则留空。然后点击右下「保存」，并可点击左下角「检测远程连接」。*我个人偶尔会遇到连接不上的情况，可能还是有些 bug。* 如果没问题，便可以将你的初始博客「同步」到 GitHub。

![](https://czyouge.github.io/post-images/image-20210720205218331.png)

同步成功后，等待很短时间，访问你的「用户名.github.io」应该就能看到你的博客了。

初始博客预置了两篇文章，一篇是欢迎文章，一篇是「关于」，两者均可删除或修改。

另外，如果你希望在自己定义的文件夹（比如放在网盘文件夹中同步）管理你的博客，可点击左下角的设置按钮，配置「站点源文件路径」：

![](https://czyouge.github.io/post-images/image-20210720210854812.png)

## 3 选择合适的博客主题

在 Gridea 客户端「主题」窗口，可以选择博客主题。选择之后一定要点击保存，并且要同步成功后才能应用到博客上：

![](https://czyouge.github.io/post-images/image-20210720210338334.png)

Gridea 预置了 4 个主题，但它们可能并不合你的心意。你也可以在[官网主题页面](https://gridea.dev/themes/)下载你感兴趣的主题。然后将下载好的主题解压后放入`站点源文件路径`下的 `themes` 路径中。之后关闭 Gridea 客户端并重启，再重新选择主题即可。

![](https://czyouge.github.io/post-images/image-20210720211529806.png)

当然你也可以修改你的主题，这可通过 Gridea 客户端的「自定义配置」实现，也可通过修改相应主题中的文件或 `config` 文件夹中相应配置文件完成。

## 4 绑定域名

我的域名 czyouge.xyz 是几年前在 Godaddy 购买的，当时挺便宜，现在价格应该也不高。购买完成后进入该域名的 DNS 管理，添加如下图所示的几条记录：

![](https://czyouge.github.io/post-images/image-20210720212007307.png)

其中一条是 CNAME 记录，`name` 填入 www，当然你可以用其它的，比如 blog——这样可通过 `blog.你的域名` 访问你的博客。`value` 填入你的「用户名.github.io」。

另外再添加一条或多条 A 记录，这是为了实现更安全的 HTTPS 访问，A 记录的 IP 地址可选择：

- 185.199.108.153
- 185.199.109.153
- 185.199.110.153
- 185.199.111.153

更多详情可参考[这个知乎回答](https://www.zhihu.com/question/31377141/answer/103056861)。

然后进入你的 GitHub 代码库，选择 Settings：

![](https://czyouge.github.io/post-images/image-20210720212847287.png)

然后选择 Pages，在 Custom domain 填入你的域名并保存（Save），然后等待验证完成，点击 Enforce HTTPS，这是强制启用 HTTPS。这样即使使用 `http://你的域名` 访问，也会强制转向 `https://你的域名`。

![](https://czyouge.github.io/post-images/image-20210720212957155.png)

这个功能很有用，至少 Chrome 浏览器在打开你的博客时不会发出安全报警，比如访问饭否时便会收到这样的报警：

![](https://czyouge.github.io/post-images/image-20210720213551484.png)

## 5 配置谷歌分析

如果你想知道博客的访问数据，可以免费使用谷歌分析来做到这一点。Gridea 也提供了非常简单易用的支持。

首先当然是注册谷歌账户，然后进入 [Google Analytics](https://analytics.google.com/)。点击左下角管理：

![](https://czyouge.github.io/post-images/image-20210720214100101.png)

然后在「账号」栏创建账号，之后你会得到一个 `UA-xxxxxxxxx-x` 格式的跟踪 ID。接下来进入「媒体资源设置」：

![](https://czyouge.github.io/post-images/image-20210720214514791.png)

在「默认网址」设置 https 并填入你的网址：

![](https://czyouge.github.io/post-images/image-20210720214719382.png)

然后进入 Gridea 客户端「主题」→「自定义配置」→「谷歌统计」，填入跟踪 ID：

![](https://czyouge.github.io/post-images/image-20210720215231254.png)

之后可通过[谷歌分析](https://analytics.google.com/)查看博客访问数据报告。

## 6 发布文章

使用 Gridea，我们有两种发布博客文章的方式。

一是使用客户端文章窗口添加文章：

![](https://czyouge.github.io/post-images/image-20210720215627564.png)

但这种方法略显笨重。

第二种方法则是直接将 Markdown 文章放入 `站点源文件路径` 下的 `posts` 文件夹中。使用这种方式有几点需要注意：

- Markdown 文件的名称即为文章的链接 ID。
- 文件内有一些重要的元数据：title 是文章标题，date 是展示的时间，tag 为标签，published 为是否发布（false为保存草稿）、hideInList为是否隐藏（隐藏后不会在文章列表中出现）、isTop为是否置顶，feature 的参数则为文章封面图的链接（可留空）。
- `<!-- more -->` 用于分割摘要和其余正文。
- 另外，如果是在其它位置编辑带图片的 Markdown 文件，请注意图片的相对地址。

![](https://czyouge.github.io/post-images/image-20210720220205046.png)

最后，在任何操作后都记得「**同步**」到 GitHub 代码库哦，这样你的文章才能和读者见面。
