## Install

+ 使用安装包：推荐使用vnpy官网安装包，如果担心和自己常用的Python环境冲突就把自己的环境删掉（狗头）
	+ 缺点：
		+ 只能用于win
		+ 要安装一个完整的Python环境
+ 手动构建：在Ubuntu上只能选择手动构建，但是提醒您的是vnpy的构建方式对机器原生的系统是侵入式的，无论是win还是Ubuntu都要抱着自己的环境被污染的准备
+ [我的项目](https://github.com/zweix123/znpy)：为了解决vnpy的部署对原生环境的破坏，我考虑将vnpy构建在由Poetrty维护的虚拟环境中，所以您可以在我的基础上进行构建，我已经完成了最困难的部分
	+ 最困难的部分：
		>官方提供了`requirements.txt`文件，那么还有什么困难呢？原因在下面两点。

		1. `ta-lib`的依赖是一般机器所没有的，这里建议使用手动下载`whl`文件的方式安装
		2. `PySide6`很容易在由Poetry维护的虚拟环境中出现依赖冲突，这里我的解决方法可以参考项目中的`pyproject.toml`文件

# Develop

+ 我会讨论的部分：
	+ 基础设施：RestClient，WebSocketClient、数据库、数据服务
	+ App：策略模块、回测模块
	+ Gateway：OKEX、Binance
		>交易的最底层要落实到对应平台的API上，发送HTTPS GET请求Python确实可以，但是这样直接简单的发送请求的话代码是不易维护，于是有各种各样的封装/抽象层，vnpy gateway即为vnpy对这些平台API的封装。

## UI

+ 选择从UI入口是因为，没有为什么，个人觉得合适。
+ 这部分倒不需要必须有Qt基础，但是最好有图形化编程的基础，有很多写法很“图形化”，另外Qt有独特的概念：信号和槽
	+ 信号就像这样`signal: QtCore.Signal = QtCore.Signal(参数)`，每个信号可以绑定一个槽`signal.connect(槽函数)`，如果信号调用`emit`方法即会调用对应的槽  
		其中信号的参数即为通信的方式，在emit中放入，要求绑定的槽函数有一样的参数

代码在`vnpy/trader/ui/`目录下，先看`qt.py`再看`mainwindow.py`，文件`widget.py`中的都是辅助性窗口，看到哪里再跳转过去。

+ `qt.py`：定义、配置并返回了一个QApplication作为后台程序，`create_app`函数参数并非窗口标题，而是用于windows进程管理的
+ `mainwindows.py`：定义、配置并返回了一个QWidget作为主窗口，这里的`windows_title`才是窗口标题
	+ 标题`windows_title`，其作用不仅是窗口title，还是软件配置的保存路径，可以去`TRADER_DIR`所在的文件`vnpy/trader/setting.py`中，返回它的函数是先判断项目路径下有无名为`.vntrader`的目录，没有则在用户根目录`~`创建。所以这个变量即为用户根目录，和其对应的`TEMP_DIR`即为软件配置文件所在目录  
		`windows_title`还有一个作用，看下面的代码
		```python
		settings: QtCore.QSettings = QtCore.QSettings(self.window_title, name)
		```
		关于`QtCore.QSettings`的具体功能我不清楚，但是观测结果是这是对文件`~/.config/${windows_title}/name`进行读写，代码中作为name的有`custom.conf`和`default.conf`
		>这也是vnpy狗血的地方，在Linux中`TRADER_DIR`是一个路径，这个路径作为一个字符串的子串，然后按这个子串去创建目录则会连续嵌套创建多个。

	+ 在`init_menu`方法中有些值得讨论的地方（从`__init__`到`init_ui`到`init_menu`）
		+ 在“连接”（原代码叫“系统”）中，如何获得`gateway_names`暂时跳过，我们看对每个gateway是怎么处理的。



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
	+ 事件处理器：即`HandlerType: callable = Callable[[Event], None]`，就是一个函数，参数为事件，在某类事件出现时用参数为对应事件的事件处理器处理来处理表示订阅
	+ 事件驱动引擎`EventEngine`
		+ 事件注册：代码中最后两个方法，把一个事件处理器注册进引擎中，表示注册的事件处理器的参数的事件类型被订阅
		+ 事件队列：类的一个属性，是一个线程安全的队列，有个线程不断的从队列中出去事件，并用注册了该事件类型的事件处理器去处理该事件。
			+ 外界可以不断的往里`put`事件

### main engine
我们来到了vnpy的核心，在`vnpy/trader/`目录下

+ `event.py`：很简短，各常量是事件引擎中的事件的类型
+ `setting.py`：很简短，关于UI的初始化配置。
	+ 值得一提的是，你看这里通过`load_json`函数对配置进行了更新，这个更新是更新的对应键，所以如果最开始没有这个配置文件就什么也不会更新合理，那么这些配置什么时候保存到本地的呢？我们进入这个load_json函数，我们发现如果它遇到一个不存在的函数则会创建一个空的同名json文件并返回空的dict，这时这个配置文件被创建了，那么什么时候这个配置文件真的发挥作用呢？因为我们发现按照Update的逻辑，空了配置文件也不会对内存中的配置dict有影响。是在`mainwindows.py`的这里
		```python
		action: QtGui.QAction = QtWidgets.QAction("配置", self)
		action.triggered.connect(self.edit_global_setting)
		bar.addAction(action)
		```
		这里的`self.edit_global_setting`方法会创建一个`GlobalDialog()`对象，在这里的`update_setting`方法有一个`save_json`函数
+ app基类在`app.py`的`BaseApp(ABC)`，所有app都派生自该基类  
	gateway基类在`gateway.py`的`BaseGateway(ABC)`，所有gateway都派生自该基类
+ `engine.py`：核心，事件驱动引擎作为基础设施，而这里是主引擎`mainengne`，用来管理各个模块和网关以及某些app中内部的事件驱动引擎。
	+ 这里有个属性就是事件驱动引擎，这里受限于Python的语言特点，它不应该理解为一个包含在mainengine里的engine，而是指针，指向mainengine使用的engine
	+ 这里有个`BaseEngine`基类，它的意思是各个模块是由该基类派生，我们看它的定义有一个engine和mainengine，这里的理解和上面一样，指向该模块“归属于”哪个mainengine，用的是哪个event engine
		>所以从这里看`BaseEngine`中的`Engine`这个命名是有歧义的

	+ 这个代码中还有派生自`BaseEngine`的三个类：`LogEngine`、`OmsEngine`、`EmailEngine`
		+ OmsEngine是重点，我们发现有大量的事件和事件对应的事件处理器在这里被注册进事件驱动引擎的。
			>这个类的意义就是专门用来添加方法的，不然这么多的内容注册放在MainEngine中会很乱。

		+ LogEngine是用来初始化一个`logging`模块的，它的处理仍然使用的主体的EventEngine
		+ EmailEngine则有独立的线程，专门处理
			>这个线程并未使用事件驱动，就是来一个任务干一个，只有一种任务

下面会分别结合一个gateway和app来解释vnpy整体上是怎么工作的。

## Infrastructure

关于协程的基本知识可以查看我的[笔记](https://github.com/zweix123/CS-notes/blob/master/Programing-Language/Python/Concurrency.md#%E5%8D%8F%E7%A8%8B)，这里讲一些vnpy对相关api的使用。

启动是这样的语句
```python
"""启动客户端的事件循环"""
try:
	self.loop = get_running_loop()
except RuntimeError:
	self.loop = new_event_loop()

start_event_loop(self.loop)
```
这里就是找到一个正在运行的event loop，如果找不到则创建一个，然后用这个event loop去运行`start_event_loop`这个函数，那么这个函数是什么呢？
```python
def start_event_loop(loop: AbstractEventLoop) -> None:
    """启动事件循环"""
    # 如果事件循环未运行，则创建后台线程来运行
    if not loop.is_running():
        thread = Thread(target=run_event_loop, args=(loop,))
        thread.daemon = True
        thread.start()
```
我们发现这个协程是丢给一个线程去运行的，具体是让一个线程去运行`run_event_loop`这个函数，那么这又是什么函数呢？
```python
def run_event_loop(loop: AbstractEventLoop) -> None:
    """运行事件循环"""
    set_event_loop(loop)
    loop.run_forever()
```
这里就明朗了，vnpy将拿到/创建的event loop作为当前的event loop并让它一直运行，而这个运行也是在子线程中。
>说道这里说明在拿到event loop的语句里，基本就是通过catch exception创建，所以这里语义上是需要这个异常的，且预测这个异常应该抛出。

这里我们的当前线程就是不断的将任务给到运行在子线程的event loop了，怎么做的呢？
```python
fut: Future = run_coroutine_threadsafe(coro, self.loop)
return fut.result()
```
这里的`coro`是一个coroutine object，通过api run_coroutine_threadsafe交给event loop去运行，然后拿到结果。

### vnpy_rest

有了上面的解释，这份代码就好理解了。

其中`Request`和`Reponse`这两个类就是数据传输对象

对于`RestClient`，其中的`request`方法即是发送一个request，得到reponse；`add_request`则是通过回调函数去处理request的reponse。

### vnpy_websocket

和vnpy_rest非常类似。

+ `send_packet(dict)`发包：包括编码和发包
+ `unpack_data(str)`解包：没有收包，只有编码

+ `start`会在子线程的event loop中运行这样一个函数`_run`，这里，返回的建立连接，处理收到的信息和断开连接，共有三个回调函数
	+ `on_packet(dict)`对收到的信息的处理（dict已经被解包）
	+ `on_connected()`连接回调
	+ `on_disconnected()`断开回调

	这三个函数由子类实现继而实现对应功能

## Gateway

这里的复杂性体现在子类实现大量的基类要求的那些函数，而整体逻辑上不难。

值得一提的是关于websocket相关派生类的回调，它是做了一个字符串到函数的映射，在`on_packet`的回调用通过字符串找到对应的函数去处理对应的数据。

### vnpy_okex
>目前(2023.4.18)，vnpy官网的版本还有bug，可以使用我的版本。

## App

关于主引擎对各个app的调用在main engine中已经讨论，可以看各个app目录的`__init__.py`文件中派生自`BaseApp`的类的这两个属性`engine_class`和`widget_name`，分别指app使用的引擎类和窗口名，有意思的是引擎类执行一个具体的类，而窗口名只是对应的窗口的类的名字，这和主引擎、主窗口引入它们的方式有关。

这里的引擎，使用的也是主引擎使用的事件驱动引擎（整个程序都使用的是唯一的一个事件驱动引擎（至少主要部分是这样）），所以这里的引擎的性质也和main engine类似，是event engine和外界的接口。

### vnpy_ctastrategy

相信您对这个模块最好奇的地方一定在于，为什么我们派生自`CtaTemplate`的类中定义的各个方法可以按照规定去执行。

+ 策略的载入：

	窗口的构造会调用cta engine的`init_engine`，在这个方法中，会调用`load_strategy_class`方法，是在这里载入的各个模块类（这个载入过程也比较复杂）

+ 策略的初始化、启动和停止：

	在窗口类中有三个方法：`init_strategy`、`start_strategy`、`stop_strategy`，参数即为“策略对象名”，在这里通过`call_strategy_func`调用策略的具体方法

+ 策略的运行：

	在策略的启动方法（`start_strategy`）最后有一句`self.put_strategy_event(strategy)`这个方法的是向事件驱动引擎放一个事件类型为`EVENT_CTA_STRATEGY`的事件，联想到event egnine的性质，我们想办法找到这个事件类型是什么时候被注册进去的，是在窗口类的`register_event()`方法中，但是它是先给一个“信号”绑定了一个“槽”，然后为上面的事件类型注册的事件处理器是这个信号的`emit`。这里是关于Qt的设计，这部分就可以理解为，信号会将信号的参数作为槽函数的参数去调用槽，所以这里仅仅是相当于一个转换，本质就是调用信号绑定的`process_strategy_event`函数。在这个函数中，引入了这个类`StrategyManager`，在这个函数中的其余或者相关语法都是关于前端展示的，想要看具体的逻辑还要。。。很好，断了。

