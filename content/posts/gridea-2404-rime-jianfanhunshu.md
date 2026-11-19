---
title: 讓Rime支持简繁混輸
date: '2024-04-30T10:15:42+08:00'
url: /post/2404-rime-jianfanhunshu/
tags:
- RIME
- 工具
draft: false
legacy_key: gridea-2404-rime-jianfanhunshu
legacy_host: www.czyouge.xyz
original_url: https://www.czyouge.xyz/post/2404-rime-jianfanhunshu/
description: 我一直觉得混合使用简繁体是一種很有趣的表现形式；最近发现了一個現成的方案，让 Rime 输入法可以實現简繁混合輸入。 該方案来自 CSDN，但我们无需經歷同樣的操作过程，使用其結果詞庫即可：https://download.csdn.net...
---

我一直觉得混合使用简繁体是一種很有趣的表现形式；最近发现了一個現成的方案，让 Rime 输入法可以實現简繁混合輸入。

該方案来自 [CSDN](https://blog.csdn.net/yulinxx/article/details/124006694)，但我们无需經歷同樣的操作过程，使用其結果詞庫即可：<https://download.csdn.net/download/yulinxx/85230494>

使用很简单，解压后，放至 RIME 的用戶文件夾, 然后部署即可使用。

![](https://i.imgur.com/DakiAYN.png)

我个人仅使用了其中的部分词库，毕竟我不使用五笔輸入法。這裏做个記錄，以备之后有需要時回顧。

- 將 clover 開頭的 2 個文件和 THUOCL 开头的 11 个文件复制到用户文件夹。
- 在将这些词库导入到主词库，即在对应 yaml 文件中的 `import_tables:` 下加入如下条目：
  ```
  - clover.base
  - clover.phrase
  - THUOCL_animal
  - THUOCL_caijing
  - THUOCL_car
  - THUOCL_chengyu
  - THUOCL_diming
  - THUOCL_food
  - THUOCL_IT
  - THUOCL_law
  - THUOCL_lishimingren
  - THUOCL_medical
  - THUOCL_poem
  ```
- 注释掉 `double_pinyin_flypy.schema.yaml` 中的

  ```  
  - name: simplification
    states: [ 漢字, 汉字 ]
  filters:
    - simplifier
        - uniquifier
  ```

 如果後面需要重新简繁分開输入，可以清除對上述條目的註釋。
