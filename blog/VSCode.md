调教一套快捷键收益是不错的

+ 推荐结合我的开发机配置指南食用更佳：
	+ [Windows](Missing-Semester/WindowsConfigGuide.md)
	+ [Linux](Missing-Semester/LinuxConfigGuide.md)
+ 巨硬的VS Code [Manual](https://code.visualstudio.com/docs)

## Use

+ Settings：VSCode的配置分三个层级：默认->用户->工作区，同一项配置后者覆盖前者。
	+ `Ctrl + ,`打开user setting UI
	+ 命令`open settings`

+ `code`
	```bash
	code filepath  # 打开文件
	code folderpath  # 打开目录(推荐)
	code .  # 打开当前目录
	code -r xxx  # 在当前窗口打开文件或目录
	```

+ 编辑器内命令：`Ctrl + p`：打开VSCode Comman Center
	+ 键入文件名打开文件
		+ 或者使用`Ctrl + Shift + E`打开资源管理器，然后使用方向键选择
	+ 键入前缀 `>` 使用VSCode命令（或者直接快捷键 `Ctrl + Shift + p`）
		+ 大小写转换
		+ 函数折叠
	+ 键入键入`@`在当前文件按名称查找（或者直接快捷键`Ctrl + Shift + O`）
		>怎么在多个文件按名称查找呢？`Ctrl + Shift + f`

+ Basic Editing：略
	+ multi-cursor：
		+ `Alt + 鼠标`
		+ （选中） -> `Ctrl + d`
		+ `Shift + Alt + 方向键`

+ 常用快捷键：
	+ `Ctrl + ~`/`Ctrl + num`切换terminal和workspace
	+ `Ctrl + \`左右分屏

+ 常用命令：
	+ 格式化：手动，快捷键`Shift + Alt + f`，效果依赖于插件

+ 其他功能：
	+ 名称跳转：`Ctrl + 点击名称`，首先跳转实现，再跳转定义，再弹出使用，效果依赖于插件
		+ 如果是跳转，`Alt + Right`返回当前跳转之前（go back）
			>注意这里反常识的是方向键右键，这和我的改键有关

	+ 在写xv6时，每次编译会产生大量的文件，让资源管理视图很乱，但是每次都删除这些文件每次编译又太慢了，想到能不能按照类型排序？使用参数`explorer.sortOrder`

## .vscode目录

+ Reference：Manual
	+ https://code.visualstudio.com/docs/editor/debugging#_launch-configurations
	+ https://code.visualstudio.com/docs/editor/tasks#_custom-tasks

+ `extensions.json`（[manual](https://code.visualstudio.com/docs/editor/extension-marketplace#_workspace-recommended-extensions)）
+ `setting.json`（[manual](https://code.visualstudio.com/docs/getstarted/settings#_workspace-settingsjson-location)）：工作区相关配置
+ `task.json`（[manual](https://code.visualstudio.com/Docs/editor/tasks)）
+ `launch.json`（[manual](https://code.visualstudio.com/docs/editor/debugging)）

## Config

+ *设置同步*，本机的sync now是将本地配置上传，然后每次启动VSCode都会从云端down下来配置
+ 关闭受限模式：
	打开设置，键入`trust`  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/blog/vscode受限模式关闭.png" style="zoom:59%;" div align=center />

+ 主题（背景颜色、字体颜色等等）：插件`One Dark Pro`和插件`Atom One Dark Theme`
	>One Dark主题的优点：养眼
	>>我真的使用过很多主题，但是用过One Dark后总感觉其他主题更刺眼，我将还要终端、vim也统一成One Dark风格

+ 文件图标：插件`vscode-icons`

+ 字体：
	+ 编辑器字体：打开设置，键入`Editor Font Family`  
		>需要插件`FiraCode font - Professional Font for Developers`

		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/blog/编辑器字体.png" style="zoom:60%;" div align=center />

	+ 终端字体：打开设置，键入`Terminal Font Family`  
		>需要你已经按照Shell的配置下载了对应字体

		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/blog/终端字体.png" style="zoom:57.5%;" div align=center />
		
+ 括号连线：打开设置，键入`bracket`，找到对应位置选择true  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/blog/branket.png" style="zoom:60%;" div align=center />

+ 柔顺：  
	打开设置，键入`smooth`，选择下面三个选项  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/blog/smooth.png" style="zoom:79%;" div align=center />  
	打开设置，键入`cursor` ，将下面设置为smooth  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/blog/cursor smooth.png" style="zoom:75%;" div align=center />  

+ 补全建议：打开设置，键入`preview`，选择下面的选项  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/blog/suggest perview.png" style="zoom:64%;" div align=center />

## Plugin
一些细小的插件（比如上面的配置中字体是需要下载插件的）不在这里汇总，对于各个语言的插件在下面各小节。

+ 远程开发（远程开发可能是VSCode对jb家的主要优势了）
	+ `Remote-SSH`：远程开发必备（据说有漏洞，不过我不在乎）
	+ `Docker`：Docker开发必备，使用体验和Remote类似
	对于代码补全有LSP的概念，总之有些插件想要远程发挥总也也要在远程install一份

## Code

+ VSCode交与JB家的IDE值得说的优点就是远程开发功能了，我们假设你本机是win，无论是那么当你需要Linux环境（无论时WSL、服务器还是虚拟机）时，都推荐使用SSH（服务器肯定是SSH，WSL我个人没有用过，虚拟机虽然相当于完整机器但是仍然建议通过SSH过去开发），而VSCode的Remote插件可以达到一个很自然的开发流程和体验。

### Python

+ 依赖环境：通过Scoop下载Python（Python3）
+ 插件推荐：Python和Python Extension Pack（它们有依赖的插件，所以会下载很多）
+ 配置：对于Python的开发，我通常把配置放在工作区，settings如下：
	```json
	{
		"python.formatting.provider": "black",
		"python.linting.mypyEnabled": true,
	}
	```
	格式化和静态检查

	+ 格式化：使用`black`，手动
		+ 跳过格式化标记：
			+ 单行：`# fmt: skip`
			+ 多行：`# fmt: off`和`# fmt: on`

	+ 静态检查：需要保存文件
		+ 忽略某行的静态检查：`# type: ignore`
		+ 对于普通类型的静态检查：`# type: 类型`

>另一种配置
```json
{
	"python.formatting.provider": "autopep8",
	"python.linting.flake8Enabled": true,
	"python.linting.flake8Args": [
		"--exclude=venv,build,__pycache__,__init__.py,ib,talib,uic",
		"--ignore=E501,W503"
	]
}
```

+ 对第三方库的引入补全：https://blog.csdn.net/weixin_38165206/article/details/102903066
+ 块执行：选择代码后使用快捷键`Shift + ehter`会将这部分代码发送到Python Shell中
+ 使用`#%%`可类似Jupyter分块
	>Jupyter状态下有很多快捷键


### C/C++

+ Reference
	+ [Clang in Windows](https://windowsmacos-vscode-c-llvm-clang-clangd-lldb.readthedocs.io/index.html)
	+ [Gcc in Linux（视频）](https://www.bilibili.com/video/BV1YG4y1v7uB)

+ Windows：
	1. 依赖环境：通过Scoop下载了gcc、g++、gdb、make和cmake
	2. 安装插件：C/C++和C/C++ Extension Pack（它们有依赖的插件，所以会下载很多）

+ 如果你没有使用Make去管理项目，可能出现不能include的问题，[解决方案](https://blog.csdn.net/qq_44078824/article/details/119904218)

+ 调试：CodeLLDB, 短时间不会写C++代码了，Mark一下吧。

### Golang

微软[教程](https://learn.microsoft.com/zh-cn/azure/developer/go/configure-visual-studio-code)已经足够亲爹

+ how to debug: [tutor](https://www.digitalocean.com/community/tutorials/debugging-go-code-with-visual-studio-code)

### Web

+ 插件：
	+ `Auto Rename Tag`：补全
	+ `Live Server`：启动服务渲染页面

### Java

+ JDK：
	+ Windows：use scoop, refer to [the site](https://github.com/ScoopInstaller/Java/wiki)

+ 插件：
	+ `Java Extension Pack`：包含大量其他必须插件

+ TODO：
	+ 项目依赖管理
		>我用编译选项`-cp`手动管理的依赖，但是在编辑器层面不能识别，会报错

## MarkDown
见我的关于Markdown编辑器的[讨论](Missing-Semester/Markdown.md)

+ 插件：
	+ 渲染：Markdown Preview Enhanced：`Ctrl + k v`
	+ 编辑：Markdown All in One
		+ 提供补全
		+ 生成目录

## LaTeX
