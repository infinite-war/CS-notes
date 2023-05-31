## Intro
>Git是一种版本管理工具，GitHub是一个代码托管平台。

+ 相关资料：
	+ [Pro Git book](https://git-scm.com/book/en/v2)
	+ [Git User Manual](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/user-manual.html)
	+ [可视化](http://onlywei.github.io/explain-git-with-d3/)

## Git

+ 工作区worksapce：仓库所在的目录，是独立于各个分支的。
+ 暂存区Stage/索引Index：数据暂时存放的区域，类似于工作区写入版本库前的缓存区，也是独立于各个分支的。
	>个人感觉两个概念略有区别，所以是git所管理的文件，一个管理的文件可以将修改记录在暂存区、也可以选择不记录，但是它仍然被git管理，在索引中
+ 版本库repositorty：存放所有已经提交到本地仓库的代码版本  
	+ 版本结构：树结构，树中每个节点代表一个代码版本
	+ HEAD：指向当前节点的最新节点
![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/git区.png)  
### Config
```bash
git config --global user.name xxx  # 设置全局用户名
git config --global user.email xxx@xxx  # 设置全局邮箱地址

git config --global core.editor vim  # your favorite editor
git config --global color.ui true

git config --global http.proxy ""  # 如果使用没遇到问题就不用
```
+ 配置文件位置：
	+ win：`C:\User\$User\.gitconfig`
	+ linux：`~/.gitconfig`

### Use
+ Init: 进入项目目录下：
	```bash
	git init
	```
	+ 信息维护在项目目录下的隐藏文件夹`.git`中
>下面提到的修改包括创建、删除和修改

工作区和暂存区
+ `git status`：查看工作区状态，维护文件是否修改、是否提交到暂存区
+ `git add file`：将`file`文件（的修改）添加到暂存区
	>add命令不仅有将文件的修改放入暂存区，还有将新的文件放入git的索引中

	`git add .`：添加所有
+ `git reset .`：撤销上一次提交暂存区的操作
+ `git restore --stated file`：将file（的修改）从暂存区撤出，但是仍然在索引区
+ `git rm --cached file`：将file从索引中删除——不再管理
	>然后将该文件放在`.gitignore`中保证不再维护。
+ `git restore file`：将file的修改撤回到暂存区的版本——这里是暂存区和工作区、不是版本库和工作区
	+ `git restore .`：注意暂存区中最开始的时候应该和版本库当前分支前是一样的，如果被所有文件都撤回到暂存区版本，相当于取消这次的修改
		>但是注意到只有add的file才能管理，也就是说我这次修改不仅修改了内容还创建了文件，此时如果想取消这次修改对于创建的文件只能手动删除
+ `git diff <file>`：查看工作区的file相对于缓存区都修改了那些内容
+ `git commit -m "remarks"`：将暂存区的内容提交到当前分支  
	`git commit`将进入文本编辑器，`Ctrl + C` -> `Y`提交
---
版本库
+ 版本号：哈希值的前六位，下面支出可查看的命令
+ `git log`：查看当前分支的所有版本
	+ 参数`--pretty=online`
+ `git reflog`：查看HEAD指针的移动历史（包括回滚动作）
+ `git reset --hard HEAD^`/`git reset --hard HEAD~`：将工作区的代码回滚到上一个版本
	+ `git reset --hard HEAD^^`：回滚两次、以此类推
	+ `git reset --hard HEAD~100`：往上回滚100个版本
	+ `git reset --hard 版本号`：回滚到特定版本

	可以同于合并最近的几个commit

+ 关于分支：
	+ `git branch [branch]`创建分支
	+ `git checkout [branch]`切换分支
	`git checkout -b [branch]`创建并切换分支
	+ `git branch`：查看分支
	+ `git merge [branch]`：将分支合并到当前分支上

## Github
>资料：
>+ 《GotGitHub》[电子书地址](http://www.worldhello.net/gotgithub/)

### Config

### Use

+ Init：创建一个新项目时有足够的提示

+ `git push`：推送，将本地版本库放到云端
+ `git pull`：拉回，将云端版本库放到本地
+ `git clone ...`：将某个项目down到本地
	+ `GitHub`提供了不同的clone url，个人项目使用ssh，即通过之前绑定的公钥来修改

+ 指定分支克隆：
	```bash
	git clone --branch <branchname> <remote-repo-url>
	git clone -b <branchname> <remote-repo-url>
	```

### Pages
考虑这样的场景，我的项目的有些成果可以静态网页的形式展示，能够缩短路径让客户最快的看到我们产品的效果。但是大张旗鼓的在服务器搭建一个Web服务也不合适，因为大概率服务器属于你的时间要远小于项目属于你的时间。这时GitHub Pages就派生用场了。下面给出一个方案。

打开项目 -> Settings -> Pages(在右边) -> (在Branch下选择)master + docs -> Save -> 然后把一个index.html放到项目的docs目录下即可通过`https://用户名.github.io/项目名/`访问

## 实战

### 如何为一个开源项目做贡献

一个在Github上Public的项目是开源的，每个人都可以查看代码，也能为项目贡献代码。那么怎么贡献代码呢？

>+ issue：任何人都可以向项目提问题，当然任何人也都可以解答
>	+ 项目作者可以限定提问格式
>	+ good first issue，简单的issue，适合项目新手第一次上手项目

建议在PR之前先提issue，然后对应的PR是为了解决这个issue，下面将如何PR

+ Pull Request：
	1. fork这个项目到你的仓库
		>我们在开发的同时还有其他贡献者，项目可能同时在开发，我们应该提交到最新的版本：同步[fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)

	2. clone：克隆到本地进行开发
	3. 创建新的分支（分支命令应尽可能简单且能反应我们的工作）
		```bash
		git checkout -b [branch name]
		```
		>实际上每开始一部分都应该开一个新分支

	修改代码

	4. `add` -> `commit -s`：message应该逻辑清晰（还记得如果不使用`-m`参数会进入一个编辑器嘛？在里面用Markdown写）
		>参数`-s`表示在提交信息中加入Signed-off-by签名，表明作者已经同意以某种方式授权提交代码
	
	5. `git push 远程分支 你的分支`
		>`git remote`：查看远程分支

	6. 在GitHub上点击Pull Request

	会有人对你的pr进行review，可能需要修改 

	修改后的commit需要这样`git commit -s -amend`
	+ 参数`-amend`表示修改上一次提交，而不是创建一次新的提交

	之后的push需要加上参数`-f`

### 修改过去版本中的记录
>这个行为是危险的

我有一个个人项目，它诞生于我对git使用很不规范的时期，有很多无用的commit，其中真的影响使用的是，我发现git clone的速度非常的慢，虽然项目中确实有挺多的静态文件，但是直觉上感觉不应该这么慢。我在之前的某个commit中把大量的测试用图片交了上去，猜测这部分在.git目录中的记录体积很大。考虑如何删除。

1. 创建并进入新分支：` git checkout -b remove-images`
	>`git branch -a `查看分支
	
2. 列出所有commit` git log --oneline`，有每次commit的hash code和message  
	`git show --name-only <commit-hash>`查看某次commit的提交情况  

	通过上面两个命令找到提交大量图片的commit和commit内容
	>`git show --name-only <commit-hash> | grep ".jpg\|.png\|.gif" | vim -` -> `:w tar-images.txt`

3. 使用脚本`git-delete.sh`：
	```bash
	#!/bin/bash
	
	while read filename; do
		# Run git filter-branch command for each filename
		git filter-branch --force --index-filter "git rm --cached --ignore-unmatch $filename" --prune-empty --tag-name-filter cat -- --all
	done < tar-images.txt
	```

	这个脚本会运行很长时间

4. 删除辅助文件，将当前分支推送到github上
	1. `git push -u origin remove-images`将当前分支推送上去（github该项目有两个分支）
	2. `git checkout master` -> `git merge remove-images`准备何如分支（github上显示pr通知，去通过pr）
	3. `git reset --hard remove-images` -> ` git push --delete origin remove-images`删除本地和github上的新分支

果然快很多。

### 多分支维护
指的是这样的情况，我当前的版本还需要小修小补，但是还有新的开发任务，且新旧任务没有任何交叉。

1. 新开一个分支：`git branch 新分支名`
+ 
	+ 查看分支：`git branch`
	+ 切换分支：`git checkout 分支名`

2. 将新分支维护在云端：
	1. 切换分支
	2. push看提示

3. 
	+ 旧分支通过`git commit --emand`维护
	+ 新分支正常维护

4. 合入：
	1. 切换到master分支
	2. `git merge 新工作分支名`

### 查看过去版本的效果

首先，最安全的一个方案是开一个新的分支

1. 项目写着写个挂了，而且已经commit，当然可以通过`git reset HEAD~1`回到上一个commit，这是在出错的commit里的代码都是未commit的。  
2. 但是想看看上一个版本的效果是啥，新的commit里修改的文件太多了，直接`git checkout .`，于是把新commit的修改“取消”掉了，此时再编译运行就是之前正确的版本。  
3. 心里有谱了，想看看新版本的修改都发生了啥——我草，我给`chectout`都删除了，之前白写了？  

4. 不会的，可以通过`git reflog`查看HEAD指针的变化情况，我们发现了我们的reset，同一行有对应的哈希值，只需要`git reset 哈希值`就可以返回到第一步之前

+ 这个`git reflog`肯定是存储在`.git`目录中，那么我们这样会在开发过程中的来回移动`HEAD`会造成`.git`目录变大嘛？（比较这部分体积对项目本身是没有意义的）  
	是不会的，这个命令是“本地HEAD指针”变化
	+ 不会存储在`.git`目录中，不会push到github中的项目中
	+ 如果本地的文件删除，即使git clone也不会得到这部分信息，这部分信息只能保存在本地
 