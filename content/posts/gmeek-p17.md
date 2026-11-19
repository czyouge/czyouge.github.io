---
title: 如何给小米手表刷国际版固件
date: '2025-12-24T22:31:24+08:00'
url: /post/ru-he-gei-xiao-mi-shou-biao-shua-guo-ji-ban-gu-jian.html
tags:
- 技术
draft: false
legacy_key: gmeek-p17
legacy_host: blog.czyouge.xyz
original_url: https://blog.czyouge.xyz/post/ru-he-gei-xiao-mi-shou-biao-shua-guo-ji-ban-gu-jian.html
description: 原来，小米/红米的手环/手表是可以刷机，更换国际版固件的。
discussion_url: https://github.com/czyouge/blog/issues/17
---

原来，小米/红米的手环/手表是可以刷机，更换国际版固件的。

这有什么好处呢？

1. 小米健康应用的国际版页面更加简洁，没有乱七八糟的付费表盘。
2. 中国区版本只能将数据同步到微信或支付宝，而国际版支持 Health Connect、 Strava 等。

坏处？

1. 这是国际版固件，与中国区数据不互通。如果你是小米生态用户，这就会让你的手表孤立在外——没有小爱，也无法通过手表控制你的智能家居，除非你全部都使用海外帐号（也不见得可行）。
2. 刷回中国版本的成本较高。

如何操作？搜索网络后，我发现了需要付费的方案，来自 Reddit [m0tral](https://www.reddit.com/user/m0tral/)。但他的说明比较松散，我在这里整理下详细过程：

1. 加入他的 Telegram 群：<https://t.me/mi_watch_int>
2. 下载一个 Mi Fitness Mod apk [# MiFitness mod v1.41](https://miwatch.conversmod.ru/micolor/app/latest_v141)，也就是修改版的小米健康。接下来当然是卸载手机上原有的小米健康，并安装这个修改版。
3. 登录，连接设备。（这时候的登录帐号需要是国内帐号，否则无法连接手表）
4. 进入「设备」选项，安装你想要的固件表盘，有全球版、欧洲版之类的。这一步是需要付费的，通过 PayPal 与一个 Telegram bot 交易，价格通常几欧元。
5. 等待激活信息。
6. 回到小米健康表盘，安装购买的表盘。成功后会显示`Installation complete`。这时候千万不要重启手表。
7. 进入小米健康，在设备中选择「更多→更新」，并下载更新。这个过程耗时较久，需要十几分钟。
8. 更新完成后，给手表执行一次重置（reset）。
9. 重启后的手表就已经是国际版固件了。
10. 这时候，就可以卸载这个修改版 app 并安装小米官方版本了（可选）。然后需要将手机上小米健康应用的区域改为其它国家，并重新连接手表。这相当于一个新帐号，与之前中国区的数据不互通。
11. 操作完成。你的小米手表获得了国际版固件，后面用小米官方的健康app更新即可。

注意事项：我在实践中遇到了一个问题：在第 7 步执行「更多→更新」时发现当前固件已显示为最新版本。遇到这种情况时，可以给 @mi_watch_bot 发送指令 `/latestapp` 获取一个新版本的 Mi Fitness Mod。安装后应该就能看到更新。
