+ 项目[地址](https://github.com/opencurve/curve)
	+ [中文README](https://github.com/opencurve/curve/blob/master/README_cn.md)

+ 提供两种服务：
	+ BS, block system：curvebs
	+ FS, file system：curvefs

# Use

## CurveAdm
用于deploy curve

+ 项目[地址](https://github.com/opencurve/curveadm)
	+ [wiki](https://github.com/opencurve/curveadm/wiki)


@郑尉欣 你指定的peer地址是mds服务的，不是chunkserver服务的，peer地址是要对应copyset的3个副本其中一个
1. 先了解下curvebs各个组件的功能，基本概念（物理池、逻辑池、copyset、peer、leader、follower等）
2. 这个问题跟部署的镜像无关，你跟程义沟通不在一个频道上，不需要make build image
chunkserver地址一般是8200开始的端口号，6700是mds服务端口号
部署集群，照着curveadm的wiki文档搞一下就行了，最简单的就是部署playground环境，一条命令搞定
wiki部署集群照着文档如果部署不起来，那得晚上抽时间继续学习下，有问题及时沟通交流，前提是先把curvebs的基本架构和相关基础概念熟悉的差不多，学习计划里的文档，不看肯定是不行的
@郑尉欣 这条命令的意思是，把一个3副本挂了两个副本的copyset的leader，强制指定为存活的那个副本所在的chunkserver（ip：端口），让集群还能在严重故障场景下继续降级运行
Example 
curve_ops_tool reset-peer -logicalPoolId=1 -copysetId=10001 -peer=127.0.0.1:8080:0 -new_conf=127.0.0.1:8080:0 -max_retry=3 -timeout_ms=100

执行这个命令之前，你要先确保里面的参数在你的集群里是真实存在的，并且是互相对应的，比如copysetid 10001在logicpool 1里面是真正存在的，因为这个只是一个example，参数都是随意写的示例，你要在你的集群里面查询出来才能设置上去正确的参数，peer和new conf这俩参数也是一样的道理，不能随意写一个就跑起来
root@curvebs-chunkserver-ad6b27ed7d3d:/curvebs/chunkserver# curve_ops_tool check-copyset -logicalPoolId=1 -copysetId=11
Copyset is healthy!
root@curvebs-chunkserver-ad6b27ed7d3d:/curvebs/chunkserver# curve_ops_tool check-copyset -logicalPoolId=1 -copysetId=11 --detail
Copyset is healthy!

[4294967307]
peer_id: 10.246.159.82:8200:0
state: FOLLOWER
readonly: 0
term: 4
conf_index: 3
peers: 10.246.159.82:8200:0 10.246.159.82:8201:0 10.246.159.82:8202:0
leader: 10.246.159.82:8202:0
这个命令可以查到copyset的peers信息
curve_ops_tool reset-peer -logicalPoolId=1 -copysetId=10001 -peer=127.0.0.1:8080:0 -new_conf=127.0.0.1:8080:0 -max_retry=3 -timeout_ms=100
这里的peer参数是你要reset的那个peer，new conf是要设置上去的新leader peer，这些命令的用途如果不理解，翻代码是比较慢的，可以找人问问看，会比较快，但是前提是你要先能理解这里面的一些基本概念，什么是logicpool，什么是copyset、leader、peer，这些有一部分是raft的基本概念，有一部分又是curve的基本概念，都要提前熟悉好才行****

### Args

+ hosts
+ topology

### All-in-one
[tutor](https://github.com/opencurve/curve/blob/master/README_cn.md#curvebs-%E5%BF%AB%E9%80%9F%E4%BD%93%E9%AA%8C)

## tool
>旧工具：[code](https://github.com/opencurve/curve/tree/master/src/tools)、[use-guide](https://github.com/opencurve/curve/blob/master/docs/cn/curve_ops_tool.md)  

+ 新工具：[code](https://github.com/opencurve/curve/tree/master/tools-v2)、[develop-guide](https://github.com/opencurve/curve/blob/master/tools-v2/docs/zh/develop.md)
+ 新工具开发进度：较于旧工具的[差别](https://github.com/opencurve/curve/tree/master/tools-v2#curve-bs)

# Develop
## Compile
[guide](https://github.com/opencurve/curve/blob/869d29972bf677fef4f745c1d14be419376f1bce/docs/cn/build_and_run.md)

## playground
[guide](https://github.com/opencurve/curve/blob/master/tools-v2/docs/zh/develop.md#%E9%83%A8%E7%BD%B2-curve-%E9%9B%86%E7%BE%A4)

+ 锅：
	+ 执行`curveadm playground`部署playground报错，应使用`sudo $(which curveadm) playground run --kind curvebs`



----


观测结果，
chunkserver中三人一组
在curveadm stop其中两个后，最后一个的身份，不必，leader or follow，通过reset-perr可以让他变成leader，而且当其他stop的服务start后，这个reser的peer依然是leader

、、、




curve_ops_tool reset-peer -logicalPoolId=1 -copysetId=1 -peer=10.246.159.82:8200:0 -new_conf=10.246.159.82:8201:0 10.246.159.82:8201:0 10.246.159.82:8201:0 -max_retry=3 -timeout_ms=100


curve_ops_tool check-copyset -logicalPoolId=1 -copysetId=1


./curve bs update peer  10.246.159.82:8202:0 --logicalpoolid=1 --copysetid=1 --rpcretrytimes=1 --rpctimeout=10s