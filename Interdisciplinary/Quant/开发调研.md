# 交易平台

+ 开发者FMZ：[web.cn](https://www.fmz.cn/) | [web.com](https://www.fmz.com/)
+ [RiceQuant](https://github.com/ricequant)：
	+ [core](https://github.com/ricequant/rqalpha)

# 交易系统

| 模块 | 模块说明                                 |
| ---- | ---------------------------------------- |
| 行情 | 获取市场信息和处理（对接币安欧易的API）  |
| API  | 暴露给用户的接口（获得信息和交互）       |
| 策略 | 处理行情，反馈用户交互（即包括执行模块） |
| 资管 |                                          |
| 回测 |                                          |

# 开源框架/交易库

+ [CCXT](https://github.com/ccxt/ccxt)：加密货币交易库，提供交易平台接口
+ [TA-Lib](https://github.com/TA-Lib/ta-lib-python)：基于Cython，量化数据金融分析库

| name(address)                                            | Star,Fork   | 语言    | 更新状态 | 说明     | 是否支持数字货币 | 是否支持期货 |
| -------------------------------------------------------- | ----------- | ------- | -------- | -------- | ---------------- | ------------ |
| [vn.py/VeighNa](https://github.com/vnpy)                 | 20.3k, 7.8k | Python  | 频繁     |          | 是               | 是           |
| [wondertrader](https://github.com/wondertrader)          | 1.3k, 300   | **C++** | 频繁     |          | 多品类           | 多品类       |
| [Cryptoquant](https://github.com/studyquant/cryptoquant) | 101, 26     | Python  | 偶尔     | 个人卖课 | 是               |              |

# 回测模块

+ 市面上常用的用于回测的方法：
	+ 模拟
	+ 向量化回测：通过向量批量计算而已
	+ 事件驱动回测：优雅的模拟？

## 开源回测模块/框架

| name(address)                                                                                      | Star,Fork           | 语言   | 更新状况         | 说明                          |
| -------------------------------------------------------------------------------------------------- | ------------------- | ------ | ---------------- | ----------------------------- |
| [vnpy的CTA回测模块](https://github.com/vnpy/vnpy_ctabacktester)                                    | 33, 38              | Cython | 频繁             |                               |
| [zipline](https://github.com/quantopian/zipline)                                                   | 15k, 4.6k           | Python | 最后更新于3年    | 事件驱动                      |
| [backtrader](https://github.com/mementum/backtrader) [doc](https://www.backtrader.com/)            | 10k, 3k             | Python | 最后更新于2年前  |                               |
| [PyAlgoTrade](https://github.com/gbeced/pyalgotrade) -> [basana](https://github.com/gbeced/basana) | 3.9k, 1.3k -> 14, 2 | Python | 不再更新 -> 频繁 | 异步+事件驱动，专注于数字货币 |
| [QSTrader](https://github.com/mhallsmoore/qstrader)                                                | 2.4k, 790           | Python | 最后更新于2年前  | schedule-driven               |
| [pysystemtrade](https://github.com/robcarver17/pysystemtrade)                                      | 1.9k, 624           | Python | 最近             | 个人项目                      |
| [AIOQuant](https://github.com/paulran/aioquant)                                                    | 361, 325            | Python | 最后更新于4年    | 异步+事件驱动                 |
| [Quantiacs](https://github.com/quantiacs)                                                          |                     |        |                  | 更像是公司，Github只是托管    |

# MISC

+ Python画图库：https://github.com/pyecharts/pyecharts
+ 一个包含博客文章的网站：https://backtest-rookies.com/
+ 比特币交易机器人：https://github.com/askmike/gekko
+ 一个功能很多的相关项目：https://github.com/yutiansut/QUANTAXIS
+ 一个简单的回测程序：https://github.com/kerwinyc/kbt_
+ 一个由个人总结的量化相关学习项目：https://github.com/Chandlercjy/OnePy
