

# 容器docker

每个docker可以管理多个image镜像，每个image都可以生成多个container容器（这些容器里的环境都是一样的），每个容器都相当于一个完整的云服务器

1. 下载
2. 配置：docker很多命令需要sudo，为了避免每次使用docker命令都需要加上sudo权限，可将当前用户加入安装中自动创建的docker用户组中
	```bash
	sudo usermod -aG docker $USER
	# 重启终端
	```


+ 镜像（images）：

  + `docker images`：列出本地所有镜像

  + 从docker官网拉去一个镜像：`docker pull ubuntu:20.04`：拉取一个镜像

    > 镜像有两部分构成：`type:version`

  + `docker image rm ubuntu:20.04` \ `docker rmi ubuntu:20.04`：删除镜像ubuntu:20.04

  + 迁移镜像：

    1. 压缩：`docker save -o ubuntu_20_04.tar ubuntu:20.04`：将镜像ubuntu:20.04导出到本地文件ubuntu_20_04.tar中

       > 该文件通常权限是不可读，要手动加一个可读权限`chmod +r ubuntu_20_04`

    2. 迁移到其他服务器：`docker load -i ubuntu_20_04.tar`：将镜像ubuntu:20.04从本地文件ubuntu_20_04.tar中加载出来

       将该压缩文件传到对应的服务器即可下载

+ 容器（container）：

  + `docker ps -a`：查看本地的所有容器

    + `docker ps`：查看各容器状态

  + `docker [container] create -it ubuntu:20.04`：利用镜像ubuntu:20.04创建一个容器。

    `docker [container] commit CONTAINER IMAGE_NAME:TAG`：创建某个`container`的镜像

  + `docker [container] start CONTAINER`：启动容器  
    `docker [container] stop CONTAINER`：停止容器  
    `docker [container] restart CONTAINER`：重启容器  
    `docker [contaienr] run -itd ubuntu:20.04`：创建并启动一个容器  

    > 这里的参数`-itd`：如果没有d是创建、启动并进入

    `docker [container] attach CONTAINER`：进入容器

    + 先按`Ctrl-p`，再按`Ctrl-q`可以挂起容器

      > `Ctrl + d`是直接关掉容器

    `docker [container] rm CONTAINER`：删除容器（需要容器停止）

    + `docker container prune`：删除所有已停止的容器

  + `docker [container] exec CONTAINER COMMAND`：在容器中执行命令

  + 迁移容器：并没有迁移容器，而是浅出容器的镜像

    + `docker export -o xxx.tar CONTAINER`：将容器CONTAINER导出到本地文件xxx.tar中

    + `docker import xxx.tar image_name:tag`：将本地文件xxx.tar导入成镜像，并将镜像命名为image_name:tag

    > docker export/import与docker save/load的区别：
    >
    > + export/import会丢弃历史记录和元数据信息，仅保存容器当时的快照状态
    > + save/load会保存完整记录，体积更大

  + `docker top CONTAINER`：查看某个容器内的所有进程  
    `docker stats`：查看所有容器的统计信息，包括CPU、内存、存储、网络等信息  
    `docker cp xxx CONTAINER:xxx` 或 `docker cp CONTAINER:xxx xxx`：在本地和容器间复制文件  
    `docker rename CONTAINER1 CONTAINER2`：重命名容器  
    `docker update CONTAINER --memory 500MB`：修改容器限制  

## 案例: 利用acwing的资源搭建docker

1. 在本地将镜像上传到自己租的云端服务器：`scp /var/lib/acwing/docker/images/docker_lesson_1_0.tar server_name:`
2. 在云服务器将镜像加载到本地：`docker load -i docker_lesson_1_0.tar`  
	创建并运行docker_lesson:1.0镜像：`docker run -p 20000:22 --name my_docker_server -itd docker_lesson:1.0 `
3. 进入创建的docker容器：`docker attach my_docker_server`  
	设置密码：`password`
4. 去云平台控制台中修改安全组配置，放行端口20000
+ 则可以通过`ssh root@xxx.xxx.xxx.xxx -p 20000`指定端口ssh
+ 此时配置的docker容器相当于一个完整的云服务器，可以配置其免密登录，注意此时本地的`~/.ssh/config`中要在多加一行`Port 20000`

## 报错处理

+ 报错：
	```
	Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get"http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": dial unix /var/run/docker.sock: connect: permission denied
	```
	解决：
	```bash
	sudo chmod 666 /var/run/docker.sock
	```
