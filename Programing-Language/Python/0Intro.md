## Config

### pip 代理
+ 参考资料：
	+ [一个把来龙去脉解释清楚的文章](https://codeantenna.com/a/pAOz55u5Px)

我个人在win上的Python通过Scoop下载，在Linux上我用的Ubuntu，自带Python，所以一直没有遇到关于代理的问题，直到我在win数据中心上搭建服务需要手动安装Python时，

目前的解决方案是：
```bash
pip config set global.proxy http://127.0.0.1:7890
```
在服务器我使用的代理工具是`Clash for Windows`，配置文件照猫画虎的。

## 软件源
+ 命令：
	+ 临时换源：`pip install module_name -i ...`
	+ 永久换源：
		```bash
		pip config --global set global.index-url .../simple/
		pip config --global set install.trusted-host ...
		```
		+ 取消换源（或者直接修改配置pip的ini）：
			```bash
			pip config unset global.index-url
			pip config unset install.trusted-host
			````

+ 常用源：
```
https://pypi.tuna.tsinghua.edu.cn/simple  # 清华源
https://mirrors.aliyun.com/pypi/simple/  # 阿里源
http://mirrors.cloud.tencent.com/pypi/simple  # 腾讯源
http://pypi.douban.com/simple/  # 豆瓣源
```

## Use

## std

Python2和Python3是没有向后兼容的，这里造成了一些混乱，比如某些语境下`python`指的就是最新版的Python，但是有些语境下则是默认Python2、只有`python3`才指的是Python3。  
所以建议使用命令`python3`，如果没有则将（是Python3）的`python` copy 一个`python3`，还有诸如`pip`这样的命令，也建议加上`python3 -m pip`的前缀
>对于诸如`poetry`或者`thefuck`这样的应用则不用这样，因为他们都是由pip下载的，如果在piip时指的python版本，那么他们的版本肯定是对的。

+ `Pythonic`

+ Ubuntu脚本：
	```python
	#! /usr/bin/python3
	#-*- coding: utf-8 -*-
	```

### Tool

+ `ipython`
+ `jupyter`