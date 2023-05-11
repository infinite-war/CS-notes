Raft是一个管理replicated log复制式日志的consensus algorithm

什么是复制式日志呢？

一言以蔽之：分布式肯定要面临容错问题，容错的一个方法是复制，一旦复制就要面对一致性问题了，保持一致性的方法有两种，分别是State Transfer状态转移和Replicated State Machine复制状态机，前者就是把必须的信息全部拷贝、后者是增量式的拷贝，拷贝确定性的变化，节点各自还原到相同状态。后者的一个实现方式就是Replicated Log复制式日志。

流程如下：  
![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/Consensus/复制式状态机架构.png)

# Raft

现在请忘记上面的东西，Raft提高可理解性的方法之一就是把算法分成几个相对独立的部分，在看下面的笔记请不要试图把整体联系起来，就面对每个小问题即可

## Leader Election

+ Raft是一个中心式的集群，每个机器处于一下三个状态之一：`leader`、`follower`、`candidate`  
	正常情况下，集群有且只有一个Leader，剩下的都是Follower
	+ Candidate是特殊状态
	+ Follower是Passive的，不会主动发起请求，只会简单的相应来自Leader和Candidate的请求
		+ 如果有一段时间没有收到信息，就变成Candidate，然后发起选举
	+ Leader是共同选举处理的，它有管理Replicated Log的完全职责
		+ 它接受来自client的log entries，复制给其他机器，并在适当的时候让它们将Log应用到各自的状态机上
			+ 且只有Leader处理来自Client的请求，如果一个Client向Follower发起请求，则Followe会将它重定向到Leader上
		+ Leader能决定新entry放在Log的哪个位置而不必咨询其他机器，数据也是从Leader流向其他节点
		+ Leader如果Fail，则选举新Leader
			+ 当然如果没有意外，Leader就一直Leader
	
	状态机：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/Consensus/状态机.png" alt="状态机" style="vertical-align:top">

### Pre

+ 任期Term：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/Consensus/term.png" alt="term" style="vertical-align:top">

	Raft将时间划分成长度不固定的任期，每个任期从election选举开始，选举成功就normal operation；可能整个任期都没有选举成功（no emerging leader），则进入下一个任期

	+ 选举开始时，有多个Candidate都试图称为Leader
	+ Raft要保证一个任期最多有一个Leader
		+ “最多”，一个任期可能没有Leader，就是没有选举成功嘛

	+ 每个节点看到的任期是不一样的，甚至看不到任期

	+ 任期数据结构
		+ 任期号currentTerm，一个只会增加的整数

	+ 节点通信会带上任期信息：
		+ 如果一个节点发现自己的比其他的小，则立刻更新（自己知道的任期过期了）
		+ 如果一个Candida和Leader发现自己的任期过期了，则立刻切换到Follower状态
			+ 此时发生了什么呢？
		+ 如果一个节点接收到携带了过期任期编号的请求，则拒绝

+ 通信：通过RPC实现
	+ RequestVote：由Candida在选举期间发起
	+ AppendEntries：由Leader发起，用于Replicated Log Entries并作为heartbeat方式

+ heartbeat机制
	+ 节点启动是Follower，只要持续从Leader和Candidate收到合法RPC请求，就一直是Follower
	+ Leader定期发送心跳（空的AppendEntries）给所有Follower，即heartbeat
	+ 如果一个Follower在Election Timeout时间内没有收到，则变成

### 选举

选举肯定是一个Follower发起的，当选举开始时

1. 增大自己当前的Term
2. 切换到Candidate状态
3. 并发的向集群其他节点发送RequestVote RPC
	+ 每个节点都有整个集群所有节点的信息？

+ 之后它将处在Candidate状态，直到发生一下三种状态之一
	+ 该Follower赢得此次选举，称为Leader
	+ 另一个节点赢得此次选举，称为Leader
	+ 选举超时，每个产生有效Leader

+ 当一个Candidate赢得选举后，就会称为Leader，然后就立刻发送心跳信息给其他所有节点来建立自己的权威，防止新的选举的发生

+ 选举规则：
	+ 获胜条件：如果一个Candidate获得集群**大多数节点针对同一任期的投票**，那么它就赢得了这个任期内的选举
		+ 这个限制条件保证了一个任期只能有一个Leader
	+ 游戏玩法：针对给定的任期，每个节点最多只能投一票，投票的标准是First-Come-First-Served

+ 在等待投票期间，一个Candidate可能会从其他server收到一个AppendEntries RPC（声称自己是Leader）  
	如果这个Leader的Term
	+ 大于等于这个Candidate的currentTerm，那么该Candidate就承认这个Leader是合法的，回归Follower状态
	+ 小于这个Candidate的currentTerm，则拒绝这个RPC，仍然留在Candidate状态

+ 还有这样的情况，就是Candidate很分散，可能会导致没有Leader的出现
	>而且这样的情况，选举失败了，这些节点会再次同时发起一轮选举，如此往复

	+ 怎么避免无效循环的投票分裂呢？随选举超时