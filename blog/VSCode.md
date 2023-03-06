+ 快捷键（个人习惯使用）：
	+ `Ctrl + ,`：打开配置选项  
		`Ctrl + p`：搜索文件  
		`Ctrl + Shift + p`：全局配置
	+ 格式化：手动使用快捷键`Shift + Alt + F`

## 编辑器设置
>参考[视频](https://www.bilibili.com/video/BV1YG4y1v7uB/)

+ *设置同步*，本机的sync now是将本地配置上传，然后每次启动VSCode都会从云端down下来配置
+ 关闭受限模式：
	打开设置，键入`trust`  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/blog/vscode受限模式关闭.png" style="zoom:59%;" div align=center />
+ 主题（背景颜色、字体颜色等等）：插件`One Dark Pro`和插件`Atom One Dark Theme`
+ 文件图标：插件`vscode-icons`
+ 字体：
	+ 编辑器字体：打开设置，键入`Editor Font Family`  
		>需要插件`FiraCode font - Professional Font for Developers`

		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/blog/编辑器字体.png" style="zoom:60%;" div align=center />

	+ 终端字体：打开设置，键入`Terminal Font Family`  
		>需要你已经按照Shell的配置下载了对应字体

		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/blog/终端字体.png" style="zoom:57.5%;" div align=center />
		
+ 括号连线：打开设置，键入`bracket`，找到对应位置选择true  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/blog/branket.png" style="zoom:60%;" div align=center />
+ 柔顺：  
	打开设置，键入`smooth`，选择下面三个选项  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/blog/smooth.png" style="zoom:79%;" div align=center />  
	打开设置，键入`cursor` ，将下面设置为smooth  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/blog/cursor smooth.png" style="zoom:75%;" div align=center />  
+ 补全建议：打开设置，键入`preview`，选择下面的选项  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/blog/suggest perview.png" style="zoom:64%;" div align=center />

### 插件推荐

+ 插件推荐：
	+ `Remote-SSH`：远程开发必备（据说有漏洞，不过我不在乎）
		关于插件有lsp的概念，即后台是跑了一个解析代码的程序的，所以ssh到远程机器，需要在那里也下载插件和配置
	+ `Docker`：Docker开发必备，使用体验和remote类似

## 打造成IDE

### 开发Python

+ 依赖环境：通过Scoop下载Python（Python3）
+ 插件推荐：Python和Python Extension Pack（它们有依赖的插件，所以会下载很多）
+ 开发流程：使用poetry做环境管理，教程可[见](https://github.com/zweix123/CS-notes/blob/master/Programing-Language/Python/poetry.md)
---
+ 代码格式化：`python format provide` -> `black`（默认autopep8，个人喜好）
	+ 格式化配置跟随项目：在项目根目录创建`.vscode/settings.json`
		```json
		
		```

### 开发C和C++
+ win + clangd：[教程](https://windowsmacos-vscode-c-llvm-clang-clangd-lldb.readthedocs.io/index.html)
+ linux + 官方插件：[教程](https://www.bilibili.com/video/BV1YG4y1v7uB)
---
上面提到的linux下的教程在win10也可以用，下面给出如何配置环境使之可以在win下使用
1. 依赖环境：通过Scoop下载了gcc、g++、gdb、make和cmake
2. 安装插件：C/C++和C/C++ Extension Pack（它们有依赖的插件，所以会下载很多）
---
+ 如果你没有使用Make去管理项目，可能出现不能include的问题，[解决方案](https://blog.csdn.net/qq_44078824/article/details/119904218)
---
#### clangd
>LSP, Language Server Protocol

### 开发Java
[Manual](https://scoop-docs.vercel.app/docs/guides/Java.html)

### 开发Golang

微软[教程](https://learn.microsoft.com/zh-cn/azure/developer/go/configure-visual-studio-code)已经足够亲爹
+ how to debug: [tutor](https://www.digitalocean.com/community/tutorials/debugging-go-code-with-visual-studio-code)

### 编辑MarkDown
见我的关于Markdown编辑器的[讨论](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/Markdown.md)

+ 插件：
	+ 渲染：Markdown Preview Enhanced：`Ctrl + k -> v`
	+ 编辑：Markdown All in One
		+ 提供补全
		+ 生成目录（我已经开发批量生成Markdown目录的工具（[项目地址](https://github.com/zweix123/md-admin)））

## 编辑LaTeX