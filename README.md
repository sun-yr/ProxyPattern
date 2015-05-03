# Introduction

This project is a repo which hold the proxy scripts and rules。

## FoxyProxy

Export patterns  to the file [`patterns.json`](./FoxyProxy/patterns.json)。

`python pattern_to_wildcard.py` has 2 optional options：
- `-i <input filename>` #load the json file exported from FoxyProxy
- `-o <input filename>` #the output file

`python pattern_to_wildcard.py` will load the `patterns.json` in the same directory.

- [FoxyProxy](http://getfoxyproxy.org/downloads.html) from official site.
- FoxyProxy from [Mozilla Addons](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/).

## SwitchySharp\*\*

在SwitchySharp选项中切换到第二个标签页“切换规则”，启用在线规则列表，将以下地址填入：

    https://raw.githubusercontent.com/cnDelbert/ProxyPattern/master/SwitchySharp/switchyrules.txt

> [SwitchyProxy下载](https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm)

>\*\* SwitchyProxy has been deprecated. USE [Proxy SwitchyOmega](https://github.com/FelisCatus/SwitchyOmega/) instead.

## Proxy SwitchyOmega

- From [Chrome Web Store](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif)
- From Project [release page](https://github.com/FelisCatus/SwitchyOmega/releases)

Delete the default `proxy` and create your own proxy rules.