# Intro
> git是版本管理工具，github是代码托管平台。



# Git
+ 工作区：仓库的目录。工作区是独立于各个分支的。
+ 暂存区：数据暂时存放的区域，类似于工作区写入版本库前的缓存区。暂存区是独立于各个分支的。
+ 版本库：存放所有已经提交到本地仓库的代码版本
+ 版本结构：树结构，树中每个节点代表一个代码版本。  
![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Missing-Semester/Git区.png)


1. 初始化：

   ```bash
   git config --global user.name xxx  # 设置全局用户名
   git config --global user.email xxx@xxx  # 设置全局邮箱地址
   ```

   信息记录在`~/.gitconfig`文件中

   > 这部通常是在github上创建好项目后，它会知道具体参数
   >
   
2. 把文件夹创建成一个仓库：进入目录，然后`git init`即把当前目录配置成git仓库，信息记录在隐藏`.git`文件夹中

   > 其中有个HEAD为版本树上的一个结点指针

+ 通过`get status`：查看仓库当前状态

1. 当前本地目录相当于工作区

2. `git add XXX`：将XXX文件添加到暂存区（也是加到仓库索引目录）

   + `git add .`：将所有待加入暂存区的文件加入暂存区
   + 对于”删除文件“这种操作，同样可以将”对应“文件再加入缓存区，此时加入的是对这个文件的删除操作
   + `git reset .`：撤销上一次提交暂存区的操作
   
   + `git resotore --stated <file>`：将暂存区的文件从暂存区撤出：还要管理
   
   + `git rm --cached XX`：将文件从仓库索引目录中删除——不再管理
   
   + `git restore <file>`：将文件的修改撤回到暂存区的版本
   + `git diff XX`：查看XX文件相对于缓存区修改了哪些内容
   
3. `git commit -m "备注信息或者说节点名"`：将暂存区的内容提交到当前分支（情况暂存区）
   + 如果暂存区只有部分仓库所有目录中的部分文件，commit后就只修改这部分

+ `git log`：查看当前分支的所有版本
  + 参数`--pretty=online`一行显示

+ `git reflog`：查看HEAD指针的移动历史（包括被回滚的版本）

1. `git reset --hard HEAD^`或`git reset --hard HEAD~`：将代码库（工作区）回滚到上一个版本

   + `git reset --hard HEAD^^`：往上回滚两次，以此类推

   + `git reset --hard HEAD~100`：往上回滚100个版本

   + `git reset --hard 版本号`：回滚到某一特定版本

     > 版本号：`git log`和`git reflog`均可查看版本的版本号：哈希值的前六位

+ 上云origin：

  > 平台基本回给出提示命令

  0. 在托管平台上的偏好设置中添加SSH密钥为自己的ssh公钥

  1. `git remote add origin git@git.acwing.com:zweix/homework.git`：将本地仓库关联到远程仓库

  2. `git push`：将当前分支推送到远程仓库

     `git push origin branch_name`：将本地的某个分支推送到远程仓库

     > 如果是第一次push需要添加`-u`参数

  3. 克隆：`git clone 在托管平台上找到clone按钮`

+ 分支：默认创建主分支`master`

  + `git branch branch_name`：创建新分支
  + `git checkout branch_name`：切换到`branch_name`分支
    + `git checkout -b branch_name`：创建并切换到`branch_name`这个分支
  + `git branch`：查看所有分支和当前所处分支
  + `git merge branch_name`：将分支`branch_name`合并到当前分支上

  ---

  + `git push --set-upstream origin branch_name`：设置本地的`branch_name`分支对应远程仓库的`branch_name`分支

    > `--set-upstream`参数可不需要

  + `git branch --set-upstream-to=origin/branch_name1 branch_name2`：将远程的`branch_name1`分支与本地的`branch_name2`分支对应

  ---

  + `git branch -d branch_name`：删除本地仓库的`branch_name`分支
  + `git push -d origin branch_name`：删除远程仓库的`branch_name`分支

  ---

  + `git pull`：将远程仓库的当前分支与本地仓库的当前分支合并
  + `git pull origin branch_name`：将远程仓库的`branch_name`分支与本地仓库的当前分支合并

  ---

  + `git checkout -t origin/branch_name`：将远程的`branch_name`分支拉取到本地

+ `stash`：存储没有持久化的修改
  
  + `git stash`：将工作区和暂存区中尚未提交的修改存入栈中
  + `git stash apply`：将栈顶存储的修改恢复到当前分支，但不删除栈顶元素
  + `git stash drop`：删除栈顶存储的修改
  + `git stash pop`：将栈顶存储的修改恢复到当前分支，同时删除栈顶元素
  + `git stash list`：查看栈中所有
