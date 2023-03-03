https://www.runoob.com/git/git-basic-operations.html

这里介绍用法，下载请自行STFW
## Intro
>Git是一种版本管理工具，GitHub是一个代码托管平台。

## Git

+ 工作区worksapce：仓库所在的目录，是独立于各个分支的。
+ 暂存区Stage/索引Index：数据暂时存放的区域，类似于工作区写入版本库前的缓存区，也是独立于各个分支的。
	>个人感觉两个概念略有区别，所以是git所管理的文件，一个管理的文件可以将修改记录在暂存区、也可以选择不记录，但是它仍然被git管理，在索引中
+ 版本库repositorty：存放所有已经提交到本地仓库的代码版本  
	+ 版本结构：树结构，树中每个节点代表一个代码版本
	+ HEAD：指向当前节点的最新节点
![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Missing-Semester/git区.png)  
### Config
```bash
git config --global user.name xxx  # 设置全局用户名
git config --global user.email xxx@xxx  # 设置全局邮箱地址
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
+ `git restore file`：将file的修改撤回到暂存区的版本——这里是暂存区和工作区、不是版本库和工作区
	+ `git restore .`：注意暂存区中最开始的时候应该和版本库当前分支前是一样的，如果被所有文件都撤回到暂存区版本，相当于取消这次的修改
		>但是注意到只有add的file才能管理，也就是说我这次修改不仅修改了内容还创建了文件，此时如果想取消这次修改对于创建的文件只能手动删除
+ `git diff <file>`：查看工作区的file相对于缓存区都修改了那些内容
+ `git commit -m "remarks"`：将暂存区的内容提交到当前分支
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

+ 关于分支：
	+ `git branch [branch]`创建分支
	+ `git checkout [branch]`切换分支
	`git checkout -b [branch]`创建并切换分支
	+ `git branch`：查看分支
	+ `git merge [branch]`：将分支合并到当前分支上

+ 分支：默认创建主分支`master`
  + `git branch branch_name`：创建新分支
  + `git checkout branch_name`：切换到`branch_name`分支
    + `git checkout -b branch_name`：创建并切换到`branch_name`这个分支
  + `git branch`：查看所有分支和当前所处分支
  + `git merge branch_name`：将分支`branch_name`合并到当前分支上

## Github
>资料：
>+ 《GotGitHub》[电子书地址](http://www.worldhello.net/gotgithub/)

### Config
STFW
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

+ how to pull request：
	1. fork
	2. clone
	3. 创建新分支（分支名称尽可能简单且能反应我们的工作）
		```bash
		git checkout -b [Branch Name]
		```
	4. work: add -> commit 
	5. `git push 远程分支 你的分支`
		`git remote`查看远程分支
	6. github上点击提交