+ Pre: 怎么存储一个巨大的文件呢？一个很自然的想法，sharding，这时就要面对那个经典问题了，在大数定理下，机器数量很大的时候出现错误几乎是必然的，那么怎么fault tolerance呢？又一个自然的想法，就是replication，有了副本，就要面对consistency问题，为了解决一致性问题，机器间就要有额外的网络交互，即更强的一致性的代价是可能导致更低的性能，这里需要有工业上的平衡。  

	+ 强一致性
		1. 对用户来说，多个机器就像一个机器，甚至这个机器只单线程的服务于用户
		2. 多机副本完全相同
			+ 写需要同步到多个副本
			+ 读只需要读取一个机器
				>这显然更快且正确

			这样如果读机器寄了，换到另一个副本的机器没有任何问题。

	强一致性会有这样的问题，如果为了强一致性的1，那么一个机器要面临多个用户的访问，一旦出现多个用户对同一个位置进行覆写，而机器为了强一致性的2会发生通信，万一对应位置副本的机器收到不同覆写消息的顺序不同怎么保证语义？这时如果其他用户再对这个位置读，我们不能保证他们的信息来自同一个机器，那么就很可能不同（这违反了一致性！）

	>所以强一致性是有代价的。

>GFS在2003发表于SOSP，这是一个更注重创新的会议，而GFS提到一致性算法基本都被讨论过。  
>+ GFS的规模非常大，远远大于学术界建立的系统
>+ GFS用于工业界，有些工程上的东西也很有价值
>+ 提出了这样的一个观点：弱一致性也是可以的（因为之前学术界认为一个错误的系统有什么用呢？GFS为了性能并不保证返回正确的数据）

+ 我们希望GFS有的特性
	+ 全局通用（一种通用存储）
	+ sharding
	+ automatic recovery
+ GFS在实现过程中不可避免出现的特性：
	+ GFS机器们在同一个数据中心中（实际上应该分布的更远一些）
	+ Google内部使用
	+ 适用于巨大文件，建议顺序处理（而不是随机），关注点是大吞吐量

## Implementation

+ GFS是中心式的
	+ master（Active-Standby模式）：信息与交互
	+ chunk server（大量）：存储文件数据

+ chunk: 一个文件的分片，大小为64MB
	+ 多个副本，选择一个作为primary chunk，写操作都在primary chunk上
		+ 每个primary chunk是在租约时间内担任


这里的chunk即为一个文件的分片，大小为

### Master

+ data structure
	+ file table: file name - list\[chunk id / chunk handle\] —— nv
		>课上chunk id和chunk handle是同义词，下面只使用handle
	
	+ chunk table: chunk handle - chunk data
		+ chunk data
			+ list\[server\] —— v, 可以通过通信恢复
			+ chunk version —— 和实现有关
			+ primary chunk server —— v, 这个本来就是动态的
				+ 租约过期时间

	>这里的nv：non-volatile非容失

+ log：数据结构存储在内存中，如果master failed，则数据丢失，所以在写数据时master会将一部分数据写入desk，即为log，并偶尔生成一个checkpoint（快照）
	>没有使用数据库是因为log追加多快呀

### chunk server
普通的Linux机器，有一到两块硬盘，使用linux文件系统存储chunk（比如以chunk handle来命名文件）

### read

1. clent: tuple\[file name, offset\] -> master: 
	1. master从file table中得到list, 因为每个chunk大小固定，所以index可以直接求出，继而得到chunk handle
	2. master从chunk table中得到server list, return client

2. client: 从list选择一个去读

+ client会cache return

3. client:\[chunk handle, offset\] -> chunk server: return data

+ 如何request超过64MB或者跨过chunk边界怎么办？
	+ GFS有相应的库，会将这样的request分成多个request

### write

+ append：
	+ 有接口得到文件最后一个chunk handle
	+ 对于多client的写，有接口得到最后一个chunk的server