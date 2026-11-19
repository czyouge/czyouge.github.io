---
title: Typora将文章图片上传至微信公众号素材库
date: '2024-10-01T21:02:17+08:00'
url: /post/2410-Typora2weixin/
tags:
- Typora
- ChatGPT
- AI
draft: false
legacy_key: gridea-2410-Typora2weixin
legacy_host: www.czyouge.xyz
original_url: https://www.czyouge.xyz/post/2410-Typora2weixin/
cover: /post-images/2410-Typora2weixin.png
description: 我参考了这篇文章《利用微信公众号的图片上传接口，创造属于自己的图床功能！》，但它却有两个问题： 图片不是上传到素材库，而是另一个图片库（虽然无法在素材库管理，但可以用于发图文消息，一般来说也足够使用）；
  上传的图片名称包含了完整的路径名，...
---

我参考了这篇文章《[利用微信公众号的图片上传接口，创造属于自己的图床功能！](https://www.51cto.com/article/750173.html)》，但它却有两个问题：

1. 图片不是上传到素材库，而是另一个图片库（虽然无法在素材库管理，但可以用于发图文消息，一般来说也足够使用）；
2. 上传的图片名称包含了完整的路径名，于是会出现类似这样的文件名：`C:\\\\Users\\\\username\\\\AppData\\\\Local\\\\Temp\\\\Typora\\\\typora-icon.png` 。冗长而臃肿。

在 ChatGPT 的帮助下，问题 1 很容易就得到了解决，但问题 2 却很困难。之后我用 Python 简单试了下上传到素材库，发现图像文件名称能成功保持不变。于是我突发奇想，让 ChatGPT 将上面的 Go 程序改写成了 Python 版本，问题 2 就这样得到了解决。原因嘛，我也不清楚。

<!-- more -->

这里分享下我得到的 Python 版本：

```
import requests

import json

import sys

  

# 常量定义

APP_ID = "你的APP_IDID"

APP_SECRET = "你的APP_SECRET"

  

ACCESS_TOKEN_URL = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APP_ID}&secret={APP_SECRET}"

UPLOAD_PERMANENT_IMAGE_URL = "https://api.weixin.qq.com/cgi-bin/material/add_material?access_token="

  

# 获取 access_token

response = requests.get(ACCESS_TOKEN_URL)

if response.status_code == 200:

    res = response.json()

    access_token = res.get("access_token")

else:

    print(f"Failed to get access token: {response.text}")

    sys.exit(1)

  

# 确保 access_token 存在

if access_token:

    urls = []

    # 获取命令行参数并上传图片

    for v in sys.argv[1:]:

        files = {

            'media': open(v, 'rb'),

        }

        data = {

            'type': 'image',

        }

  

        # 发送图片上传请求

        upload_response = requests.post(f"{UPLOAD_PERMANENT_IMAGE_URL}{access_token}&type=image", files=files, data=data)

  

        if upload_response.status_code == 200:

            res_url = upload_response.json()

            url = res_url.get("url")

            if url:

                urls.append(url)

        else:

            print(f"Failed to upload image {v}: {upload_response.text}")

  

    # 输出上传成功的 URL

    if urls:

        print("Upload Success:")

        for url in urls:

            print(url)

else:

    print(f"Failed to retrieve access token: {response.text}")  
```
  
其它步骤与原文差不多，只不过需要使用对应的 Python 操作。

设置完成后，在 Typora 中写作时便可以自动将图片上传到微信公众号的素材库了。
