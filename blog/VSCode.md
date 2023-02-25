### 开发Python

+ 依赖环境：通过Scoop下载Python（Python3）
+ 插件推荐：Python和Python Extension Pack（它们有依赖的插件，所以会下载很多）
+ 开发流程：使用poetry做环境管理，教程可[见](https://github.com/zweix123/CS-notes/blob/master/Programing-Language/Python/poetry.md)
+ misc：
	+ 格式化：`python format provide` -> `black`（默认autopep8，个人喜好）
		>如何让这样的配置跟随项目？这里提供一个思路，vscode有两种settings，一种是关于软件本身的，另一个是关于工作区的，项目目录下的`.vscode/settings.json`文件

### 开发C和C++
>借鉴资料：
>+ 一个在win上使用clang的[教程](https://windowsmacos-vscode-c-llvm-clang-clangd-lldb.readthedocs.io/index.html)
>+ 一个在linux上的亲爹级[教程](https://www.bilibili.com/video/BV1YG4y1v7uB)
>	+ 补充解释：
>		+ `.clang-fromt`文件：用于代码格式化

实际上上面提到的linux下的教程在win10也可以用，下面给出如何配置环境使之可以在win下使用
1. 依赖环境：通过Scoop下载了gcc、g++、gdb、make和cmake
2. 安装插件：C/C++和C/C++ Extension Pack（它们有依赖的插件，所以会下载很多）

---

+ 如果你没有使用Make去管理项目，可能出现不能include的问题，[解决方案](https://blog.csdn.net/qq_44078824/article/details/119904218)

### 开发Java
[Manual](https://scoop-docs.vercel.app/docs/guides/Java.html)

### 编辑MarkDown
见我的关于Markdown编辑器的[讨论](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/Markdown.md)

+ 插件：
	+ 渲染：Markdown Preview Enhanced：`Ctrl + k -> v`
	+ 编辑：Markdown All in One
		+ 提供补全
		+ 生成目录（我已经开发批量生成Markdown目录的工具（[项目地址](https://github.com/zweix123/md-admin)））