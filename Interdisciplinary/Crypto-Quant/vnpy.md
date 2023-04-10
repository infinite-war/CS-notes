## Install

+ 使用安装包：推荐使用vnpy官网安装包，往下看你就知道有多少坑了，如果担心和自己常用的Python环境冲突就把自己的环境删掉（狗头）
+ 手动构建：既然选择手动构建，肯定不是win或者嫌弃vnpy的环境污染自己的机器，所以这里使用Poetry作为虚拟环境的管理
	+ 官方提供`requirements.txt`文件，所以直接承接过来即可，但是其中有两个问题
		1. `ta-lib`下载是真的麻烦，这边建议直接使用`whl`文件
		2. `PySide6`很容易在虚拟环境中依赖冲突，我这里将Python版本改为`>=3.10,<3.11`解决

# Develop

## UI

>想看UI部分倒不一定必须有Qt基础，但是最好有图形化基础。

在`vnpy/trader/ui`中，先看`qt.py`再看`mainwindow.py`，`widget.py`中都是辅助性窗口，看到哪里再过去。

+ 关键：理清UI的title是在哪里设计的，相关的两个配置文件（custom.conf, default.conf）是保存在哪里，菜单栏各widget是怎么回事，理解连接信息保存在哪里

## 引擎

### 事件驱动引擎

见代码`vnpy/event/engine.py`
