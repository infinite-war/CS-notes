## Install

+ 使用安装包：推荐使用vnpy官网安装包，如果担心和自己常用的Python环境冲突就把自己的环境删掉（狗头）
	+ 缺点：
		+ 只能用于win
		+ 要安装一个完整的Python环境
+ 手动构建：既然选择手动构建，说明您不能忍受使用安装包的缺点，所以使用Poetry做虚拟环境管理来解决第二个问题
	+ 官方提供`requirements.txt`文件，所以直接承接过来即可，但是其中有两个问题
		1. `ta-lib`下载是真的麻烦，这边建议手动下载`whl`文件的方式安装
		2. `PySide6`很容易在虚拟环境中依赖冲突，我这里将Python版本改为`>=3.10,<3.11`解决

# Develop

+ Tips：
	+ 妙用跳转和全局搜索（全局是项目级别的不是文件级别的）
	+ 妙用ChatGPT，对于使用的标准库直接问它是怎么回事就行，不用纠结。

+ 关于vnpy的设计哲学——高度模块化，把每个功能拆分成一个项目，如果需要再引入
	+ 基础设施：数据库、数据服务、RestClient，WebSocketClient
	+ app：策略模块、回测模块
	+ gateway：可以理解为各平台接口，是对各个平台API的封装
		>我接触vnpy是为了在binance和okx上使用，而这两个平台有很多的python api，比如python-binance，python-okx，gatewaty相当于vnpy对对应平台做的Python api

## UI
>想看UI部分倒不一定必须有Qt基础，但是最好有图形化编程的基础。

代码在`vnpy/trader/ui/`目录下，先看`qt.py`再看`mainwindow.py`，而`widget.py`中都是辅助性窗口，看到哪里再跳转过去。

+ `qt.py`是定义并返回了一个QApplication作为窗口的后台程序，`create_app`函数参数并非软件标题，而是是用于windows进程管理的
+ `mainwindows.py`是定义并返回了一个QWidget作为主窗口，这里的`windows_title`才是软件标题，但是它的作用不仅是标题，还是软件配置的保存路径，可以去`TRADER_DIR`所在文件看一下，返回它的函数先判断项目路径下有无`.vntrader`目录，没有则用户根目录下创建。所以这个变量即为用户根目录，和其对应的`TEMP_DIR`即为软件配置文件所在目录。
	+ 在这里`self.windows_title`这个属性还有一个作用
		```python
		settings: QtCore.QSettings = QtCore.QSettings(self.window_title, name)
		```
		关于`QtCore.QSettings`具体的我不清楚，但是观测结果可以知道这是在`~/.config`这个目录下创建/写入/使用/读取/一个名为`self.windows_title`的目录，`name`则指的是这个目录下的一个文件，代码中共提到两个文件`custom.conf`和`default.conf`，这也是这部分狗血的地方，window_title的组成之一是TRADER_DIR就是一个路径，所以这玩意被它划分创建了一个多层目录的配置目录
	+ 在`init_menu`的“连接”（原代码叫“系统”）QMenu，这里有两个重要的函数
		+ `self.connect`：这个专门用于连接某个gateway，里面的类`ConnectDialog`从`filename`中保存/读取该gateway的配置信息，那么这些信息保存在哪里呢？这个属性被`load_json`调用，这个函数调用了`get_file_path`，我们发现这个路径是从`TEMP_DIR`开始的，上面已经讨论过了，这个是软件配置目录
		+ `add_action`：它将一个QMenu和一个函数联系起来，比如这里就是对于点击链接这个QMenu的动作是调用上面的那个函数，继而打开对应的Dialog
	+ 还是在`init_menu`函数中，下面给出主窗口如何调用各种app的窗口
		```python
		app_menu: QtWidgets.QMenu = bar.addMenu("功能")
		all_apps: List[BaseApp] = self.main_engine.get_all_apps()
		for app in all_apps:
			ui_module: ModuleType = import_module(app.app_module + ".ui")
			widget_class: QtWidgets.QWidget = getattr(ui_module, app.widget_name)  # noqa
			func: Callable = partial(self.open_widget, widget_class, app.app_name)  # noqa
			self.add_action(app_menu, app.display_name, app.icon_name, func, True)  # noqa
		```
		这里遍历所有app，通过module找到对应app的ui代码目录路径，最后的ui代码是app.widget_name，所以对于app我们可以通过它的`__init__.py`中类的这个属性得到它启动时是打开哪个QWidget类。

	+ 还是在这个函数中，再往下则是侧边栏的各种功能，通过上面的讲解也能知道每个按钮打开的是哪个窗口，调用的是哪个函数。这里我们向“查询合约”操作深挖，它打开的是`ContractManager`这个类，点击会触发`show_contracts`方法，这个方法中通过主引擎的`get_all_contracts`方法得到信息，到这里我们还没有分析主引擎，先留下个hook
## Engine

### event engine

+ 生产者-消费者模型：中介：缓冲区
	>相信你已经知道了

+ 发布-订阅设计模式：中介：消息代理  
	+ 发布者将消息发送到中介
	+ 中介将消息给到订阅了该**类**消息的订阅者。

+ 事件驱动引擎，引擎即为发布-订阅设计模式中的中介。  
	见代码`vnpy/event/engine.py`（下面的讲解有该模式本身，也有该模式在Python中的实现，也有在vnpy中的实现）
	+ 事件：即类`Event`，两个属性分别表示事件的类型和数据
	+ 事件处理器：即`HandlerType: callable = Callable[[Event], None]`，就是一个函数，参数为事件
	+ 事件驱动引擎`EventEngine`
		+ 事件注册：代码中最后两个方法，把一个事件处理器注册进引擎中
		+ 事件队列：类的一个属性，是一个线程安全的队列，有个线程不断的从队列中出去事件，并用注册了该事件类型的事件处理器去处理该事件。
			+ 外界可以不断的往里`put`事件

### main engine
我们来到了vnpy的核心，在`vnpy/trader/`下

+ `event.py`：很简短，各常量是事件引擎中的事件的类型
+ `setting.py`：很简短，关于UI的初始化配置，但是我找不到它是什么时候被保存的
+ app基类在`app.py`的`BaseApp(ABC)`，所有app都派生自该基类
	gateway基类在`gateway.py`的`BaseGateway(ABC)`，所有gateway都派生自该基类
+ `engine.py`：核心，事件驱动引擎作为基础设施，而这里是主引擎`mainengne`，用来管理各个模块和网关以及某些app中内部的事件驱动引擎。
	+ 这里有个属性就是事件驱动引擎，这里受限于Python的语言特点，它不应该理解为一个包含在mainengine里的engine，而是指针，指向mainengine使用的engine
	+ 这里有个`BaseEngine`基类，它的意思是各个模块是由该基类派生，我们看它的定义有一个engine和mainengine，这里的理解和上面一样，指向该模块“归属于”那个mainengine
		>所以从这里看`BaseEngine`中的`Engine`这个命名是有歧义的

	+ 这个代码中还有派生自`BaseEngine`的三个类：`LogEngine`、`OmsEngine`、`EmailEngine`
		+ OmsEngine是重点，我们发现有大量的事件和事件对应的事件处理在这里被注册进事件驱动引擎的。

其余部分的解析结合下面的部分介绍

## Gateway

我们先来`/vnpy/trader/gateway.py`来看一看大基类`BaseGateway`是怎么个事
+ 在主引擎中
	+ 有属性`self.gateways: Dict[str, BaseGateway] = {}`
	+ 有方法`def add_gateway(self, gateway_class: Type[BaseGateway], gateway_name: str = "") -> BaseGateway:`
