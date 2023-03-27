- [Win机器开发机配置指南](#win机器开发机配置指南)
- [前言](#前言)
	- [0.初始设置](#0初始设置)
- [必装软件](#必装软件)
	- [1.浏览器Chrome](#1浏览器chrome)
	- [2.解压缩7z](#2解压缩7z)
	- [3.科学上网Clash](#3科学上网clash)
	- [4.笔记软件Obsidian](#4笔记软件obsidian)
	- [5.命令行](#5命令行)
		- [前置知识](#前置知识)
		- [5.1.PowerShell7](#51powershell7)
		- [5.2.oh-my-posh](#52oh-my-posh)
		- [5.3.Windows Terminal](#53windows-terminal)
	- [6.包管理器Scoop](#6包管理器scoop)
		- [7.Git](#7git)
	- [8.编辑器:VSCode](#8编辑器vscode)
- [工具软件](#工具软件)
	- [基于命令行的编辑器](#基于命令行的编辑器)
	- [截图Snipaste](#截图snipaste)
	- [思维导图Xmind8](#思维导图xmind8)
	- [幻灯片jyyslide-md](#幻灯片jyyslide-md)
	- [论文LaTeX](#论文latex)
	- [UML图PlantUML](#uml图plantuml)
	- [虚拟机VMware Workstation Pro](#虚拟机vmware-workstation-pro)
	- [硬件扩展](#硬件扩展)

# Win机器开发机配置指南
>[姊妹篇：Linux开发机配置指南](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/LinuxConfigGuide.md)

+ 精华：
	+ [命令行](#5%E5%91%BD%E4%BB%A4%E8%A1%8C)：为Windows配置一个相当优雅的命令行环境，让你在win中有近似linux的命令行体验
	+ [包管理器Scoop](#6包管理器scoop)：十分建议您千万不要错过这样一款包管理器，它极大的改善了我的开发环境

# 前言
本教程有一定门槛，不强求，只给有缘人。

>作此文章的发心：
>1. 作为重置系统的记录，在下次重置或者初始化一个win机器时提供可供参考的记录。
>2. 观察到有人对计算机的软件和文件的管理相当粗放，我想在这里提供一个我使用win机器的习惯和经验。
>3. 部分软件的配置确实值得记录，如果网上已经有足够优秀的教程，我会提供链接；否则，我会尽量按照Manual提供一个有全局观的教程。
>4. 推荐软件

+ 须知：
	+ STFW：有些名词会导致递归学习没有解释，有些问题教程颇多，这里只提供索引，请读者"Search The Friendly Web"。
	+ STFM：软件的下载通常有大量教程，但是软件更新迭代很快，不同环境、不同软件版本，流程就很可能不一样，我尽量依照Manual。
	+ 具体配置更多的是符合我个人的习惯、请读者自行“去芜存菁”。

+ 环境：我的Windows机器的规格是：`Windows 10`

+ 关于数据的管理：  
	我并没有将软件和文档分成两个盘，实际上我在学生时代创造的值得存储的数据不到30G，所以我直接在D盘创建一个专门的目录并在其下管理我的数据，这样的好处是在进行数据备份和转移时，只需要维护这个目录即可。

+ 关于软件的管理：尽量安装在非C盘的盘，因为C盘是系统盘，如果满了影响系统的正常运行，而现在非C盘也都是固态硬盘、没有速度问题
	>软件倾向于默认安装在C盘的原因：
	>+ 以前C盘是固态硬盘，其他盘则未必，故将软件安装在C盘可以更快
	>+ 软件作者不能保证用户一定具有除了C盘以外的某块盘。  

	+ 通过安装包安装软件时通常会有对应的步骤提示（或者是一个拉起的选项卡）选择路径
	+ 诸如WeChat、QQ、TIM或者是软件管家这样的软件通常涉及到文件的存储，需要在“设置”中手动修改
	+ 有些安装包直接安装软件并在桌面创建快捷方式，可以通过查看快捷方式的指向来确定其存储位置，不建议直接横移文件夹修改

## 0.初始设置

+ 第一次开机：win10会以对话式的方法进行初始化配置，仔细阅读其描述按照自己的理解选择即可。
	>其中有个选项是“是否连接WiFi”，如果是新电脑，连接后通常不能进行退换（虽然本篇文章并没有检查新机的教程）

	+ 用户名尽量用英文
	+ 系统可能会默认下载一些软件，比如视频或音乐软件，这些通常下载在C盘，我通常都是卸载然后如果需要再重新安装
	+ 简约风格，扫描一下桌面把不需要的东西去掉。

+ 导入备份：数据目录

+ 语言配置（个人习惯）：
	+ 输入法：默认
	+ 拼音设置：双拼且不自动扩展到全拼
	+ 中英切换：只保留`Ctrl + Space`

+ 文件的查看：
	+ 打开文件扩展名
	+ 打开隐藏的项目

+ 电源设置：
	>睡眠：风扇转 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;：此时电脑仍供电给内存，CPU以较低频率运行  
	>休眠：风扇不转，信息保留：计算机将内存中的内容写入进磁盘中，并断电。下次开机时可以恢复到之前的工作状态。  
	>关机：信息不保留 
	
	|          | 电池   | 通电   |
	| -------- | ------ | ------ |
	| 电源按钮 | 休眠   | 休眠   |
	| 关盖     | 不使用 | 不使用 |

+ 修改机器的语言：控制面板 -> 时钟和区域 -> 区域 -> 管理 -> 更改系统区域设置 -> 打开Beta版
	>这步非常重要，Windows为了向后兼容性使用特殊的编码，在解释或编译代码时经常出现乱码，这个一定要打开。

---

+ 不能进入`C:\Program Files\WindowsApps`：[教程](https://jingyan.baidu.com/article/1876c852de26a0c80b1376c5.html)

+ 升级到专业版或企业版，这样的场景比如连接到win的服务器就需要使用win的remote功能，这种功能家庭版没有，如何升级请STFW
	+ 资料：[1](https://blog.csdn.net/qq_32682301/article/details/116003700)

# 必装软件

## 1.浏览器Chrome
六大浏览器之一，插件丰富，登录谷歌账号同步信息和配置
>win默认使用Microsoft Edge浏览器也改为Chromium内核，可直接同步Chrome数据，但它每个选项卡被win认为是一个窗口，我个人不使用

+ Chrome默认安装C盘：不处理，软件位置右键快捷方式查看
+ 谷歌需要人工验证：使用插件Header Editor（[教程](https://blog.azurezeng.com/recaptcha-use-in-china/)）
	```
	https://azurezeng.github.io/static/HE-GoogleRedirect.json
	```
+ 插件推荐：
	+ YouTube双语字幕
		+ 字幕位置有点碍眼
	+ 划词翻译
		+ 可单开网页处理英文PDF
		+ `Ctrl + Shift + 2`打开悬浮翻译框
		+ 可将整个网页转换成双语模式
	+ 油猴脚本
		+ 这里推荐一款我开发的关于哔哩哔哩的脚本，[地址](https://github.com/zweix123/BilibiliProgressBar)
	+ crxMouse Chrome手势：后退、顶部、底部，对文件图片链接的打开

## 2.解压缩7z
一款简单的解压缩软件

## 3.科学上网Clash
懂得都懂
>记得软件安装包和梯子的备份

+ 配置：
	+ 开机自启动
	+ `F2`作为开关System Proxy的快捷键

## 4.笔记软件Obsidian
>为什么选择这款软件作为我的Markdown编辑器见我的关于Markdown编辑器的[讨论](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/Markdown.md)

+ Obsidian默认安装C盘：不处理，软件位置右键快捷方式查看
	>这个软件的核心其实是配置（项目目录下`.obsidian`文件夹），而配置文件是在对应的项目下的，可以不占C盘空间

+ 插件推荐：
	+ Obsidian Git（需要下载Git）多机同步必备
	 >我的配置：`Ctrl + Alt + s -> backup(commit and push)、Ctrl + Alt + L -> pull`  
		>会有冲突（主要是和QQ）使用`Ctrl + Alt + C -> commit, Ctrl + Alt + H -> push`
		>>该插件提供定时操作，个人习惯没有使用，上面的快捷键设计是统筹的结果

	+ Advanced Tabled：Makedown表格相关补全  
		这里我是这样考虑，该插件为操作表格提供了大量的自定义，但是抽象程度低意味着复杂，索性它提供了图形化的处理，鉴于表格本就不多，所以没有设置快捷键。

---

+ 快捷键推荐：
	+  `Ctrl + E + space`使用`+`或者`-`控制系统字体大小

+ 问题处理：
	+ `项目根目录/.obsidian/workspace.json`的修改相当频繁，不及时push和pull比较麻烦  
		比如对于报错：
		```
		error: Your local changes to the following files would be overwritten by merge:
				.obsidian/workspace.json
		Please commit your changes or stash them before you merge.
		Aborting
		```
		可通过下面命令解决  
		```powershell
		git checkout .\.obsidian\workspace.json  # win
		```
		```bash
		git checkout ./.obsidian/workspace.json  # linux
		```

## 5.命令行

### 前置知识

+ 什么是命令行？  
	命令行、终端、工作台、Shell在很多语境下都是语义重叠的  
	+ 命令行通常是最大范围的语义
	+ 终端很多时候和命令行重叠，有时特指Window Terminal或者Terminal，下面会指关于颜色的部分
	+ 工作台：请不用使用这个名词
	+ Shell有时单指执行命令的程序，linux中bash是一种shell，win中的cmd是一种shell

+ win中怎么打开一个命令行？
	+ 快捷键`Ctrl + R`键入`cmd`弹出一个窗口即为一个命令行程序，其中的Shell是cmd
	+ 键入`powershell`弹出一个shell使用windows powershell的命令行程序

---

+ 为什么要配置命令行？
	+ 功能上
		+ win上的命令行并不优秀（至少cmd是这样的），比如查看当前目录文件的命令`ls`，cmd是不支持的
		+ 有些扩展功能比如历史命令补全是非常好用、非常提高生产力的，很有必要添加这种功能
	+ 样式上
		+ 真的会好看很多

+ 配置思路：（这里提供全局的观念，下面会有具体配置步骤）
	+ 功能上：
		+ 更换Shell为`PowerShell7`（注意这不是Windows PowerShell），它支持Linux的相关命令
			>ps7（PowerShell7的简称）有很多独特的功能，比如独特的命令、独特的管道

		+ 使用程序oh-my-posh提供功能上的增强，主要是历史命令补全
		+ 使用Windows Terminual提供类似Tmux的功能
	+ 样式上：（这方面是审美和习惯方面的，我会提供我的配置，但是不一定符合您的胃口）
		+ 信息的输出，比如用户名、主机名、当前路径、Git状态，甚至时间、电量，这里使用oh-my-posh对这些信息进行排布和染色，即主题
		+ 底层的配置，比如字体、字体大小、颜色定义，这里通过Windows Terminual

		>关于颜色，颜色是个连续的概念，但是命令行程序只需要几种颜色，这里由”终端“确定某种颜色比如Red到底是什么样的（颜色是个离散的概念呦），然后上层程序比如Shell通过设置好的Red进行染色，比如将用户名染色成Red。除了Shell之外比如Vim同样是在命令行上运行的程序，所以这里的对Red的设定也会影响到它。

+ 我的[配置](https://github.com/zweix123/posh-config)，项目README中有使用方法（需要在下载完下面三个软件后再导入配置）

### 5.1.PowerShell7

+ 安装：[Manual](https://learn.microsoft.com/zh-cn/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.3)（官方推荐winget）
+ 更新：`winget update Microsoft.PowerShell`
+ 使用：快捷键`win + r`键入`pwsh`打开一个命令行程序
+ pwsh在打开后会运行`$PROFILE`这个脚本（直接在命令行中输入这个命令即可查看脚本位置）
	+ 所以可以把这个文件当做Linux的.bashrc文件

+ Powershell7的ls对输出的目录的美化需要下载额外模块：（下载比较慢）
	```powershell
	# Install-Module PSColor     # 我个人的配置已经将该模块换为DirColors, 其实PSColor更好看，但是输出多一个换行，我不能接受
	Install-Module DirColors     #  
	# Install-Module PSReadLine  # 画蛇添足的东西，后不再使用
	```

### 5.2.oh-my-posh

+ 安装：[Manual](https://ohmyposh.dev/docs/installation/windows)（官方推荐使用winget）
+ 使用：还记得pwsh在打开后运行一个脚本嘛？我们只要把调用oh-my-posh的相关命令放在那里就可以用了，这里比较重要的是**主题**的选择

### 5.3.Windows Terminal
>win10需要下载，win11自带

+ 安装：使用国内网在Microsoft Store直接搜索下载（这也是Manual推荐的）
+ 使用：
	+ 快捷键`win + r`键入`pwsh`打开一个Windows Terminal
		>报错：报错VCRUNTIME140_1.dll缺失：在C盘搜寻文件，将其复制到`C:\Windows\System\`即可

	+ 在文件资源管理器中右键在终端打开

+ 配置（涉及字体种类、字体大小、字体粗细、窗口大小、窗口打开位置、打开后模式、快捷键、配色方案等等）
	+ 下载字体（[下载链接](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/Meslo.zip)）这里用的是Manual推荐的`MesloLGM NF`字体，通过链接下载并解压发现并没有对应名称的文件夹，而是一种`.ttf`文件  
		打开观察（主要关注安装按钮和字体命令字段（关于字体文件名中的部分含义：`Regular`常规、`Italic`斜体、`Bold`加粗  ））
		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/字体打开.png" style="zoom:50%;" div align=center />  
		我们把字体名称`MesloLGM NF`的所有形态都下载  

## 6.包管理器Scoop
**Scoop非常强大，几乎任何你想下载的命令行程序或者依赖软件都可以去search一下，几乎都有！**  
比如C/C++（`gcc`、`g++`、`gdb`、`make`、`cmake`）、Python（Python和某些库的依赖）、Java、LaTeX还有各种软件。

首先考虑第一性原理的问题，我们为什么需要这样的包管理器？  
在Windows中正常使用软件通常的流程是去官网下载对应机器和系统的安装包，运行安装包安装，安装过程中会选择诸如下载路径之类的设置。在开发过程中常用的比如Git或者Python这种，下载过程中还要设置更多的选项。同时想要通过命令行使用它们还要将其设置为“环境变量”。但是在实际使用的过程中，基本只会在命令行中或者以命令的形式使用，那么下载过程中下载的诸如添加桌面快捷键、添加右键菜单栏这样的功能是画蛇添足、没有必要的。
>其实win下还有其他包管理器比如winget和chocolatey，上面终端相关就是用winget下载的，看个人习惯

+ Scoop的优点就是能统一且清楚的管理下载的软件并自动为其配置环境变量
+ Scoop的“缺点”：
	+ 不能自动配置win注册表
	+ 不能自动添加右键菜单栏  

	这里为什么加双引号呢？因为Windows是一个图形化的操作系统，命令行很高效、图形化也有独特的魅力。上面的缺点有很多问题，比如Scoop可以下载VSCode，但是不能自动设置使用VSCode默认打开`.py`文件、`.c`文件，而且不会自动添加到右键菜单栏，想用VSCode打开一个文件夹的场景大概率不是用命令行去`code`，而是图形化的找到这个文件然后右键打开；再比如`7zip`，在图形化界面下的使用流程肯定是右键压缩包解压而不是使用命令；但是这些都是在对标之前的下载流程，我们选择Scoop的原因恰恰是它不会这样，所以善用Scoop这些不是缺点。

+ 资料：
	+ [项目](https://github.com/ScoopInstaller/scoop)
	+ [官网](https://scoop.sh/#/)
	+ [文档](https://github.com/ScoopInstaller/Scoop/wiki)

+ 安装：
	```powershell
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser # 设置PowerShell执行策略
	irm get.scoop.sh -outfile 'install.ps1'                              # 下载安装脚本
	.\install.ps1 -ScoopDir 'D:\Scoop'                                   # 执行安装, --ScoopDir参数指定Scoop安装路径
	```

+ 文件结构：
	```
	Scoop
	  | ---apps      # 下载的软件安装位置
	  | ---buckets   # 桶(可以理解为软件源)
	  | ---cache     # 下载的安装包
	  | ---persist   # 用户数据
	  `----shims     # 命令位置
	```

+ 配置：
	+ 利用`aria2`来加速下载，**极大**的提高安装成功率
		```powershell
		scoop install aria2  # 安装
		scoop config aria2-enabled false  # 如果使用代理可能需要这样的配置
		# 线程相关
		
		scoop config aria2-retry-wait 4
		scoop config aria2-split 16
		scoop config aria2-max-connection-per-server 16
		scoop config aria2-min-split-size 4M
		```
	+ 添加仓库（软件源），默认只有`main bucket`
		```powershell
		scoop bucket add extras  # 官方维护的extras bucket  # 需要先下载git(在教程的下面)
		```

+ 相关命令：  
	```powershell  
	scoop --help  # 查看帮助
	scoop list    # 查看已经下载的软件
	
	scoop search 命令     # 查看有无命令
	scoop install 命令    # 下载命令
	scoop uninstall 命令  # 删除命令
	
	scoop update  # 更新scoop、软件源和各个软件
	
	scoop bucket add 桶名 [桶地址]  # 添加桶	
	```

+ voidtools：Everything是Windows平台上一个即快即轻量的文件检索工具，相当于Linux中的`find`的替代品，我们也以此为例演示Scoop的使用
	```bash
	scoop search Everything
	# 我们发现有三个，选择下载cli版本
	scoop install everything-cli
	# 我们看标准输入有Creating shim for 'es'.
	# 现在试试使用命令es
	```

### 7.Git

+ 安装：`scoop install git`
+ 配置：[我的教程](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/Git.md#config)
+ 配置SSH：[我的教程](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/SSH.md#intro)
+ Github配置：`Setting -> SSH and GPG keys -> New SSH key -> 拷贝公钥`（配置公钥用于自己通过SSH链接去`push`）

## 8.编辑器:VSCode
VSCode本身是编辑器，在插件的支持下扩展出丰富的功能（<strike>极具可玩性</strike>）

+ install：STFW Manual
+ uninstall：
	+ 软件安装位置
	+ `C:\Users\$用户名\.vscode\`：全局配置
	+ `C:\Users\$用户名\AppData\Roaming\Code\`

+ configs：内容多且散，而且无关平台，我将其放在这个[教程](https://github.com/zweix123/CS-notes/blob/master/blog/VSCode.md)

# 工具软件

## 基于命令行的编辑器

VSCode本是一个轻量型的编辑器，轻量型意味着可以快速的打开，但随着我们给它装了大量的插件，它开始变得臃肿，此时如果有轻度的编辑，再使用它就不再流畅了（无论是命令行打开还是图形化打开），我们需要一个更轻量型的编辑器。  
得益于强大的包管理器Scoop和我调教好的终端，我们可以有近似Linux的命令行体验，所以我选择vi系列作为这个轻度编辑器。
>这部分对我个人来说也是必须的，但未必适用于其他开发者，VSCode足以在可接受的成本内满足要求，所以没有将该软件放在必装软件中

+ 安装：亲爹Scoop
+ 配置和使用：我的[文章](https://github.com/zweix123/CS-notes/blob/master/Linux/Editor.md)
	>实际上vim是一个可玩性很高的编辑器，这里引用的文章不仅有vim的基本用法，可能还会有我倒腾vim的记录。

## 图片悬停Snipaste
优秀的截图软件，很好用，开源，解压即用。

+ `F1`截屏
	>个人习惯将该快捷键改为`Prtsc`（Prtsc失效）
+ 截屏后`Ctrl + T`可将截屏悬浮在屏幕上
+ `F3`可以将剪切板的内容转化成图片悬浮在屏幕上

## 思维导图Xmind8
现在的思维导图软件市场并没有一个统一的文件格式，相当于如果我们选择了一个软件几乎不可能迁移到其他软件，我现在的工作流尽可能避免使用思维导图。但是思维导图提供了一个如此独特的树形的组织信息方式，而转为手写的话速度上又很受限。至于选择哪个软件还是小马过河，这里提供Xmind8的特点，请读者自己选择
>**注意**：这里提到的Xmind是8（直接搜索`xmind8`即可），这个软件好像在2022有了更大更新，个人使用新版本不好用
>>而且Xmind8较于最新版还能自定义位置

+ 常用快捷键：`Enter`创建同级节点、`Tab`创建子节点、`Space`编辑当前节点
+ 优点：
	+ 阳间的快捷键
	+ 简约（节点大小紧贴文字）
	+ 可设置成节点任意位置
	+ 大小放缩区间小
	+ 切屏不自动停止编辑
+ 缺点：
	+ 节点限制，并不是数量限制，而是过多的节点会非常卡
		>不过这是我早期的巨大文件才出现的情况，后来女朋友用这个记笔记我看规模也很大，但是并没有很卡

## 幻灯片jyyslide-md
见我的[讨论](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/slide.md)

## 论文LaTeX
见我的[讨论](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/LaTeX.md)

## UML图PlantUML
见我的[教程](https://github.com/zweix123/CS-notes/blob/master/Software-Engineering/UML.md)

## 虚拟机VMware Workstation Pro

## 硬件扩展
见我的[讨论](https://github.com/zweix123/CS-notes/blob/master/blog/Multi-computer%20Cooperation.md)