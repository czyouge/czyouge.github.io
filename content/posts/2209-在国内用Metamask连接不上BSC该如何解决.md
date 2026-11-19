---
title: 在国内用Metamask连接不上BSC该如何解决
date: '2022-09-30T10:00:00+08:00'
url: /post/2209-bnb-bsc-metamask/
tags:
- 区块链
- 技术
- 数字货币
draft: false
legacy_key: gridea-2209-bnb-bsc-metamask
legacy_host: www.czyouge.xyz
original_url: https://www.czyouge.xyz/post/2209-bnb-bsc-metamask/
description: 前段时间，我发现我在 Metamask 上配置的 BNB Smart Chain（BSC）钱包连接不上了，但 Binance Wallet
  却能继续使用。但因为很少用，也没在意。昨天偶然想起，研究了下，找到了原因。这个问题估计很多中国人会...
---

前段时间，我发现我在 Metamask 上配置的  BNB Smart Chain（BSC）钱包连接不上了，但 Binance Wallet 却能继续使用。但因为很少用，也没在意。昨天偶然想起，研究了下，找到了原因。这个问题估计很多中国人会遇到，所以在这里分享一下。

<!-- more -->

## 问题在哪里？

大多数人在 Metamask 配置 BSC 钱包都会参考这一套方案：

- 网络名称（ Network Name）：Smart Chain
- 新的RPC URL（ New RPC URL）：https://bsc-dataseed.binance.org/
- 智能链ID（ChainID）：56
- 符号（Symbol）：BNB
- 区块浏览器URL（Block Explorer URL）：https://bscscan.com

而且[币安官网](https://academy.binance.com/zh/articles/connecting-metamask-to-binance-smart-chain)也是这么说的。但现在的问题是在中国国内，我们没法直接连接 binance.org 了——至少我使用的运营商没办法。具体原因不明，但我试过 `ping binance.org`，结果每一次都是不同的 IP 地址而且结果无一例外都是 `请求超时`。

也就是说，我的 Metamask 根本没办法连接到上面配置的 RPC URL！

## 解决方法

问题找到了，方案就来了。

虽然上面的官方教程没有提到，但其实我们可以更换 RPC URL。

访问 <https://www.bnbchainlist.org/>，我们可以找到 BNB Smart Chain Mainnet 的 RPC URL 列表：

![](https://czyouge.github.io/post-images/1664505542261.png)

选择一个当前网络能成功连接的服务器地址（选 Score 栏为绿色且延迟低的），替换掉原有配置中的 RPC URL 即可。

如此，便能继续在 Metamask 上使用 BSC 了。

❈❈❈❈❈❈❈❈❈

备注：RPC 的意思是 remote procedure call，即远程过程调用。
