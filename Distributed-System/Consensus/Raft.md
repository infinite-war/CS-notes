Raft是一个管理replicated log复制式日志的consensus algorithm

什么叫复制式日志呢？就要引入复制状态机

一言以蔽之：分布式肯定要面临容错问题，容错的一个方法是复制，一旦复制就要面对一致性问题了，保持一致性的方法有两种，分别是State Transfer状态转移和Replicated State Machine复制状态机，前者就是把必须的信息全部拷贝、后者是增量式的拷贝，拷贝确定性的变化，节点各自还原到相同状态。后者的一个实现方式就是Replicated Log复制式日志。

流程如图<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/Consensus/复制式状态机架构.png" style="vertical-align:top">

+ 共识算法特征：
	+ 安全性：在任何non-Byzantine条件下都能保证安全（从不返回错误结果）
	+ 高可用性：只要**大多数**节点能工作、彼此之间以及客户端之间能通信，整体系统的功能就完全可用
	+ 可恢复性：Fail后能从持久存储回复
	+ 不依赖时序来保证日志的一致性
		>最坏情况下，时钟不准、消息验证都不能导致可用性问题

	+ 通常情况下，一个命令收到集群大多数节点的响应时，这个命令就算完成了，少量响应慢的机器不影响整体的系统性能

# Raft

Raft是一个中心式的集群，它实现共识的机制是：共同选举一个Leader，给予这个Leader管理Replicated Log的完全责任，Leader接受来自Client的Log entries，然后复制给其他节点，并在安全时告诉这些节点将entrie应用到各自的状态机。

只有一个Leader的设计简化了Replicated Log的管理，Leader决定Log Entry位置而不必咨询其他机器，数据流也从Leader流向其他机器。

如果Leader Fail，则重新选举（当然如果没有意外，Leader就一直是担任）

## Leader Election

+ 在任意给定时刻，每个节点处于以下三种状态之一：`leader`、`follower`、`candidate`
	+ Candidate是特殊状态
	+ Follower是Passive的，不会主动发起请求，只会简单的相应来自Leader和Candidate的请求
		+ 如果有一段时间没有收到信息，就变成Candidate，然后发起选举
	+ Leader在上面描述了它的部分职责，除此之外
		+ 且只有Leader处理来自Client的请求，如果一个Client向Follower发起请求，则Followe会将它重定向到Leader上

	状态机如图<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/Consensus/状态机.png" style="vertical-align:top">

+ 任期Term：  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/Consensus/term.png">  

	Raft将时间划分成长度不固定的任期，每个任期从election选举开始，选举成功就normal operation；可能整个任期都没有选举成功（no emerging leader），则进入下一个任期

	+ 选举开始时，有多个Candidate都试图称为Leader
	+ Raft要保证一个任期最多有一个Leader
		+ “最多”，一个任期可能没有Leader，即没有节点选举成功

	+ 每个节点看到的任期是不一样的，甚至看不到任期

	+ 每个节点都记录当前任期号

	+ 节点通信会带上任期信息：
		+ 如果一个节点发现自己的比其他的小，则立刻更新（自己知道的任期过期了）
		+ 如果一个Candida和Leader发现自己的任期过期了，则立刻切换到Follower状态
		+ 如果一个节点接收到携带了过期任期编号的请求，则拒绝

+ 通信：通过RPC实现
	+ RequestVote：由Candida在选举期间发起
	+ AppendEntries：由Leader发起，用于Replicated Log Entries并作为heartbeat方式

+ Heartbeat机制
	+ 节点启动是Follower，只要持续从Leader和Candidate收到合法RPC请求，就一直是Follower
	+ Leader定期发送心跳（空的AppendEntries）给所有Follower，即Heartbeat
	+ 如果一个Follower在Election Timeout时间内没有收到，则变成Candidate

+ 选举过程：
	+ 当一个Follower试图发起选举时
		1. 增大自己当前的Term
		2. 切换到Candidate状态
		3. 选举自己作为Leader，并发的向集群其他节点发送RequestVote RPC
		4. 直到发生下面三种情况之一
			+ 该Follower赢得此次选举，成为Leader
			+ 另一个节点赢得此次选举，成为Leader
			+ 选举超时，每个产生有效Leader

		当一个Candidate赢得选举后，就会成为Leader，然后就立刻发送心跳信息给其他所有节点来建立自己的权威，防止新的选举的发生

	+ 获胜条件：如果一个Candidate获得集群**大多数节点针对同一任期的投票**，那么它就赢得了这个任期内的选举
	+ 选举规则：针对给定的任期，每个节点最多只能投一票，投票的标准是First-Come-First-Served
		>zweix: 一个任期一票

	+ 选举分裂：比如多个Follower几乎同时的发起选举，肯可能选票很分散，导致这轮选举没有Leader的产生
		>如果这些Candidate同时进入下轮选举，上面的情况可能会无限循环下去

		**随机选举超时**：每个Candidate等待选票的时间是从一些固定时长中随机选择一个选举超时时间，然后早超时的Candidate再次发起一轮选举成为Leader

+ 如果一个Candidate在等待选举时收到Leader的RPC，会对比任期编号，如果Leader的任期大于等于自己，则承认其为合法，否则则拒绝仍然是Candidate

	这个策略基本用于共同选举帮助称为Leader的节点顺利建立权威

	+ 我们再来看这么个情况，因为网络问题一个节点误成为Candidate，此时它的任期肯定比它之前的Leader大（至少不同），这会导致其他Follower给它投票致之成为Leader，当其在向集群发送心跳信息时，之前的Leader收到了一个任期更大的Leader的后，自己就变成Follower，仍然正确。

## Log replication
当选出来一个Leader后，它就开始服务客户端的请求

+ 复制流程：
	1. 每个Client的Request包含一条Comman，将由Replicated State Machine执行
	2. Leader会将这个命令追加到它自己的Log，然后并发的通过AppendEntries RPC将其复制给其他结点
	3. 复制成功（无冲突）之后，Leader才会将这个entry应用到自己的状态机，然后将执行结果返回给Client
	+ 如果Follower Fail or 很慢 or 丢包，Leader会无限重试AppendEntries（即使它已经给客户端发送了响应），直到所有Follower最终都存储了所有的Log entries

+ Log文件结构：由Log Entry组成
	+ Entry数据结构：
		+ Index：唯一递增整数编号
		+ Term：创建该Entry的Leader的Term
		+ Command

+ Commit提交
	+ 一个节点的Entry，Commit is Entry被安全地应用到状态机后
	+ 一个Entry：
		1. 创建这个Entry的Leader将它复制到大多数节点
		2. 1中的提交也提交了Leader Log中的所有前面的Entry，包括之前由其他Leader创建的Entry

	+ Follower一旦确定某个Entry被提交了，就将这个Entry应用到它自己的状态机（in log order）

+ Log matching特性保证Log coherency高度一致性

	如果不同Log中的两个Entry有完全相同的Index和Term，那么
	1. 这两个Entry一定包含相同的命令
		>证明：

	2. 在两个Log中，从该Index往前的所有Entry都分别相同
		>证明：

	+ AppendEntries一致性检查：
		+ 在请求中，Leader会带上Log中前一个紧邻Entry的Index和Term
		+ 如果Follower Log中相同的Index没有Entry，或者有Entry但Term不同，则拒绝新的Entry

	组合以上各点，通过归纳法可以证明 Log Matching Property

+ 对Log不一致的应对
	>Leader的Fail会出现Log不一致
	
	还记得上面的AppendEntries中的一致性检查嘛？如果在这个环境发现不一致，则直接暴力复制给Follower一份Header的Log
	1. 找到最后两者共同认可的Entry
	2. 多余丢掉
	3. 同步

+ 优化：
	>在上面Follower会因为Log不一致拒绝AppendEntries，怎么减少这样的情况呢？

## Safely
安全的语义是确保状态机以相同顺序执行相同的命令流


# 其他问题

## 脑裂
