+ 学习资料：
	+ MIT的[6.824](https://pdos.csail.mit.edu/6.824/schedule.html)
		+ [野生字幕翻译](https://mit-public-courses-cn-translatio.gitbook.io/mit6-824/)（不能确定年份）

+ **ELP不可能定理**：No completely asynchronous consensus protocol can tolerate even a single unannounced process death（来自Fisher、Lynch和Paterson的[论文](https://ilyasergey.net/CS6213/_static/02-consensus/flp.pdf)）

	但是**科学告诉你，什么是不可能的；工程则告诉你，付出一些代码，可以把它变成可行**，这就是工程的魅力。

## 为什么需要分布式

+ Drivens驱动力：
	+ 大量的CPU、大量的内存、大量的硬盘和大量的并行计算
	+ fault-tolerates：一个机器崩溃完全可以将其任务切换到另一台
	+ 一些问题天然在空间上是分布的，比如转账
	+ security：比如有些代码不被信任，但仍然需要和它交互，可将其部署在单独的机器，通过网络协议使用，限制**出错域**

+ Challenges挑战：主要是由于并发带来的
	+ 多机交互
	+ 故障处理
	+ 性能评估

## 分布式性能评价

+ 可扩展性/可伸缩性Scalability，即只要增加机器数量，系统就应该提高相应的性能；对应的，也能自由的去掉机器  
	以web服务为例，可以通过增加web服务器以分散用户的访问来增加系统可承受的访问量，但是诸如数据库这样的微服务不能通过简单的添加机器来解决。即可扩展性可描述为通过架构设计使很难实现的“通过增加机器的方式实现扩展”得以实现。

+ 容错Fault-Tolerance：在大数定理下，即使一个计算机出现错误的概率很低，但是当系统中的机器足够多时，出现错误几乎是必然（在特定的故障范围内）。

	+ 可用性Availabilty：service continues despite failures  
		比如通过复制replication，多副本，当然多副本就要不可避免的考虑一致性问题

	+ 自我可恢复性Recoverability：系统在寄掉后通过修复可以按之前的继续正常运行  
		比如通过非易失存储non-volatile storage，不断将数据存入硬盘

	>这里将实体机器放远一点有利于容错性，但是远距离的通信花费更多的时间

+ 一致性Consistency，多副本间数据一致
	+ 强一致性Strong Consistency：
	+ 弱一致性：  
		可以想象，强一致性的保证需要各个机器间大量的通信，这里的开销非常大，所以虽然弱一致性可能导致系统出错，但是工程上仍然是有必要的

## Consensus And Replication
就像DDIA（Designing Data-Intensive Applications）上说的Many application today are **data-intensive**，as opposed to compute-intensive. Raw CPU power is rarely a limiting factor for these applications—bigger problems are usually the amount of data, the complexity of data, and the speed at which it is changing.

下面我们来引入标题，分布式一个很重要的话题就是Fail-Tolerance，一个容错的方法就是Replication，一旦复制就要面对Consensus，为了保持一致性有两种方法：State Transfer状态转移和Replicated State Machine复制状态机，后者这种增量式的方式显然更具有性能诱惑力。

下面是出现Raft论文的复制状态机模型：  
![复制状态机模型](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/复制式状态机架构.png)

+ 共识算法特征：
	+ 安全性：在任何non-Byzantine条件（非拜占庭条件）下都能保证安全（从不返回错误结果）
	+ 高可用性：只要**大多数**节点能工作、彼此之间以及和客户端之间能通信，整体系统的功能就完全可用
	+ 可恢复性：Fail后能从持久存储回复
	+ 不依赖时序来保证日志的一致性：最坏情况下，时钟不准、消息验证都不能导致可用性问题
	+ 通常情况下，一个命令收到集群大多数节点的响应时，这个命令就算完成了，少量响应慢的机器不影响整体的性能