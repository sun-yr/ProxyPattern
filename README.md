# 项目说明

本项目是本人日常使用Pattern的总结及备份。

## FoxyProxy

通过Pattern默认导出`patterns.json`。需要的话直接导入即可。

`python pattern_to_wildcard.py`可选参数：
- `-i <input filename>` 读入patterns的json文件
- `-o <input filename>` 需要保存的URL文件

默认读入当前路径的`patterns.json`。

> [FoxyProxy下载](http://getfoxyproxy.org/downloads.html) |  [Mozilla Addons 地址](https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/)

## SwitchySharp

在SwitchySharp选项中切换到第二个标签页“切换规则”，启用在线规则列表，将以下地址填入：

    https://raw.githubusercontent.com/cnDelbert/ProxyPattern/master/SwitchySharp/switchyrules.txt

> [SwitchyProxy下载](https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm)
