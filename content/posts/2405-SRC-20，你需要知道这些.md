---
title: SRC-20，你需要知道这些
date: '2024-05-25T09:53:42+08:00'
url: /post/2405-SRC-20/
tags:
- 比特币
- 区块链
- SRC-20
draft: false
legacy_key: gridea-2405-SRC-20
legacy_host: www.czyouge.xyz
original_url: https://www.czyouge.xyz/post/2405-SRC-20/
cover: /post-images/2405-SRC-20.jpeg
description: 比特币的市值毫无疑问是加密货币的 No.1，但也存在自己的缺点，比如交易速度慢、成本高。不过，这些缺点并未妨碍开发者社区前赴后继地为扩大其生态而努力，并接连创造了
  Ordinals、Runes、Stamps、Atomicals 等协议，并进...
---

比特币的市值毫无疑问是加密货币的 No.1，但也存在自己的缺点，比如交易速度慢、成本高。不过，这些缺点并未妨碍开发者社区前赴后继地为扩大其生态而努力，并接连创造了 Ordinals、Runes、Stamps、Atomicals 等协议，并进而出现了 BRC-20、ARC-20、Runes 以及本文要介绍的 SRC-20 代币标准。

但在深入介绍 SRC-20 之前，我会首先做一些语言学上的探讨，解释一下 SRC-20 名称以及一些相关术语的由来或含义。之后我会详细说明 SRC-20 标准的细节以及其上生态的发展情况。

<!-- more -->

**例行说明：本文并非投资建议，请审慎判断。**

## SRC-20 名从何来？

SRC-20 是 Stamp Request for Comments 20 的缩写，直译成中文为「邮票征求意见 20」。

这个名称实际上源自于 BRC-20，即 Bitcoin Request for Comments 20/比特币征求意见 20。

而 BRC-20 的名字又是继承自 ERC-20，即 Ethereum Request for Comments 20/以太坊征求意见 20。

[ERC](https://github.com/ethereum/ERCs) 是向以太坊提交改进提案（[EIP](https://eips.ethereum.org/)/Ethereum Improvement Proposals）的方式之一，其目标是为以太坊**应用层**设定标准并提供高质量文档。（另外还有针对以太坊共识协议、网络连接机制、接口等网络架构方面的提案类型。）20 这样的数字则是最早在以太坊 GitHub 软件库提交的问题（issue）编号。20 号提案的目标是为以太坊设定一个发行代币的标准。这里是原始的第 20 号问题链接：https://github.com/ethereum/EIPs/issues/20 。

![](https://czyouge.github.io/post-images/1716947678639.png)

总之，[ERC-20](https://eips.ethereum.org/EIPS/eip-20) 为以太坊上的（同质化）代币定义了一个标准。目前以太坊上的大多数代币都基于此标准，比如 SHIB、UNI、PEPE 以及各种部署在以太坊上的稳定币。

毫无疑问，ERC-20 是一个非常成功的标准，以至于其它区块链往往在此基础上建立自己的代币标准，于是乎「RC-20」这个固定组合就被继承了过去。为了让「20」这个编号名符其实，其它区块链上的代币标准提案甚至会刻意保留第 20 号提案，比如 Tron 项目的 20 号提案就保留给了 TRC-20。

![](https://czyouge.github.io/post-images/1716947691572.png)

后面的 BRC、ARC、SRC 等有类似的操作，它们的 20 号提案都定义了其上的（同质化）代币标准。

至于 SRC-20 中的 S，是 Stamp（邮票）的缩写，这是因为其基于 Bitcoin Stamps 协议，见下文。

## SRC-20 的历史

SRC-20 的历史要追溯到染色币（colored coins）这一概念。简单来说，染色币就是为特定的币附带上额外的信息，使其区别于其它的普通币。从 2012 年开始，有不少团队在比特币网络上尝试过构建染色币，但都没能得到广泛应用，直到 2023 年 1 月，Ordinals 协议问世。

Ordinal 的意思是序数，比如第 1、第 2、第 42 这样的有顺序的数。Ordinals 的做法就是为比特币网络上的每个聪（sat/satoshi）赋予一个序号（即 [Ordinal theory](https://docs.ordinals.com/)，也因此某些聪变得比其它聪更稀有）。再基于一定标准，可以将数据嵌入到有序号的聪对应的 UTXO 中，这被称为铭文（Inscription）。

举个例子说明一下。打开 Ordinals 浏览工具 https://ordiscan.com，然后随便输入一个铭文序号：69420，找到第 69420 号铭文：

![](https://czyouge.github.io/post-images/1716955711799.png)

可以看到，这个铭文使用的 sat 是 1,311,843,664,028,113 号 sat，附带的信息中包含一张 svg 图像。

很明显，这是一个 NFT。这也是 Ordinals 最早的设计用途：在比特币网络上发行 NFT。但之后人们发现，如果能设定一定标准，也能让这个 NFT 变成代币。他们找到的解决方案便是 BRC-20，即将 JSON 格式的数据附加给聪，而这个数据中定义了代币的属性与交易。同样举个例子：

> ```json
> {"p":"brc-20","op":"transfer","tick":"ordi","amt":"52"}
> ```

这个铭文数据很清晰地说明：将 52 枚名为 ordi 的 brc-20 代币 transfer（转账）给……

看起来很不错！BRC-20 似乎就是人们一直期待的解决方案——我们可以在比特币上发行新代币了！

但事实并非如此，从理论上讲，Ordinals 是可能被清除掉的。

Ordinals 是基于 Ordinal theory 理论对单个聪进行实例化，然而这些被原子化的聪却有可能被错误地支付出去。这是因为它们本质上与特定的 UTXO 关联密切，而比特币协议本身无法区分出这种关联。Ordinal theory 是一种按自身规则运行的所谓「元协议」，但其底层却是 UTXO 的传输。而 Ordinals 中嵌入的数据（资产）却使用了一种账户式余额模式，其规则既独立于特定的 UTXO 运作。

针对这一缺点，[Mike In Space](https://github.com/mikeinspace) 对 Ordinals 进行了改进，创造了 Bitcoin Stamps 协议

。其中，主要的改进点是将数据存储到交易输出内，而不是 OP_RETURN 信息中。

也就是说：Ordinals 是使用 UTXO 来确定所有权，而 Stamps 则是使用 UTXO 来存储数据，这样后者便能将数据永远保存在比特币链上。

SRC-20 便是基于 Stamps 协议来发行同质化代币的标准，类似于 BRC-20 之于 Ordinals。SCR-20 的定义方式与 BRC-20 也基本一样，如下图是 KEVIN 币的一笔交易：

![](https://czyouge.github.io/post-images/1716955731281.png)

## SRC-20 的优劣之处

相比于 BRC-20，SRC-20 的主要优点是其数据存储在 UTXO 中，因此不可能被剪除；但这也带来了一些缺点：可存储的数据量上限低、交易成本较高。下面是 SRC-20 与 BRC-20 的主要差异（改编自 [cointelegraph](https://cointelegraph.com/learn/what-is-the-src-20-token-standard)）：

|           | SRC-20 标准                                      | BRC-20 标准                                |
| --------- | ------------------------------------------------ | ------------------------------------------ |
| 剪枝      | SCR-20 代币保存在 UTXO 中，无法被剪枝            | 节点可通过移除见证数据量来剪除 BRC-20 代币 |
| 签名类型  | 多重签名                                         | 单个签名                                   |
| 交易成本  | 构建的交易比 BRC-20 的大                         | 通过 SegWit 让 BRC-20 交易成本更低         |
| Token销毁 | 如果与代币绑定的 UTXO 被支付出去，便可以销毁代币 | 见证数据无法修改                           |

## SCR-20 生态

Stamps 生态之前有过短暂的热潮，但整体也仅仅处于起步状态，甚至于社区常用的 UniSat 钱包的 UI 界面依然不支持 Stamps 和 SRC-20，即便 SRC-20 社区依然主要使用该钱包进行交易。

![](https://czyouge.github.io/post-images/1716955741174.png)

Stamps 和 SRC-20 未来会发展成什么样还很难说，毕竟现在比特币社区也有一些人对 SRC-20 采用的将数据写入 UTXO 的做法很不满。他们认为这种做法会向比特币网络填入大量垃圾数据，导致网络臃肿并妨碍普通用户的使用体验。

下图是 X 平台用户 [@Inaritoo](https://x.com/Inaritoo/status/1785936652440940918) 总结的 Stamps 生态图景，其中本文关注的 SRC-20 代币位于左上角：

![](https://czyouge.github.io/post-images/1716955749780.jpg)

接下来我们简单介绍几个比较热门的 SRC-20 代币：

- STAMP：算是 Stamps 的同名代币，也是目前交易量和市值最高的 SRC-20 代币，当前市值约 880 BTC。
- KEVIN：首个部署成功的 SRC-20 代币，诞生时间为 2023-05-03 1:17:37 PM，当前市值约 165 BTC。
- LUFFY：路飞币，目前最成功的 SRC-20 迷因币，当前市值约 800 BTC。
- STMAP：StampMap，一个类似 Reddit Place 像素画的项目，算是首个有实际用途的 SRC-20 代币，，当前市值约 12 BTC。

![](https://czyouge.github.io/post-images/1716955755938.png)

*交易总额排名前 6 的 SRC-20 代币*

## 相关网站

- 官网：https://stampchain.io
- 项目库：https://github.com/mikeinspace/stamps
- 主要交易网站：OpenStamp：https://openstamp.io/ ；Stampscan：https://www.stampscan.xyz/
