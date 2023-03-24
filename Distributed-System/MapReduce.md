>[论文链接](http://nil.csail.mit.edu/6.824/2022/papers/mapreduce.pdf)

### Demand

Google要处理互联网上海量的数据，对于这样数量级的数据，单机是不能在可接受的时间内处理完的，只能分布式的处理。
+ 将算法转换成分布式算法
+ 处理好分布式要面对复杂

对于第一个问题，已经有些困难了，不是所有的算法都像Floyd一样天然有分布式的形态。

对于第二个问题，不仅会花费工程师大量的精力，而且这部分成本其实和其本来的工作关系不大。

能不能将分布式的复杂性封装起来，由框架设计者考虑，用户可以直接享用分布式的性能。

### Inspired

启发于函数式编程中的map和reduce源语。

工程师只需要考虑编写分布式程序的第一个问题，这里是将算法转换成符合“使用Map和Reduce的函数的编程范式”的算法，将两个实现交给MapReduce，系统内部来面对分布式的复杂性，继而实现我们的需求。

>这其实是一个受限制的实现，因为将原本的算法转换成符合这个程序模型的实现
>+ 需要成本
>+ 可能无解

### Model

+ Map
+ Reduce

### Implementation

1. 系统将input files被分成`M`份（每份通常16MB或64MB），这个大小可以由用户使用参数指定，然后所有程序被拷贝到集群中的每个集群
2. 有一个程序是特殊的，叫master，其他的则是worker；它给其他空闲的worker指派map task或reduce task
3. 被指派map task的worker读取对应的input file split，将其解析成k-v交给用户实现的Map function，输出的intermediate k-v缓存在内存中  
4. 这些中间k-v定期的写在Map worker的硬盘上，并且被parititioning function分成`R`份，这个大小和函数可由用户指定，函数通常是取模，  
	这些文件的名字、大小、位置会发送给master（一段message），master将其存在自己的DS中  
	master会将part结果告诉reudce worker
5. 当一个reduce worker被master通知，它会通过RPC读取这些k-v，读完后会sort，这样同样的key就在一块了，如果太大，则使用external sort
6. reduce worker迭代排序后的intermeidate data并对每个key执行用户实现的reduce function，其结构会append这个partition的output file中
	+ 该task的结束，reduce work会给output file rename（由GFS保证这个操作的原子性）
7. 结束，交回程序控制

+ master data structures
	+ task status: idle, in-progress, completed
	+ worker ID
	+ 每个被分成R份的intermediate的位置和大小（当map task完成时更新），这些信息被push给 in-progress reduce tasks

+ fault-tolerance
	+ worker failed：
		+ 对于map worker，它的fail会让所有被它完成过的task的state init idle
			>因为这些task的输出在这些worker的desk上，已经不能读取了。

			如果这些task被其他map worker re-exectued，则会让所有reduce worker知道（继而不回去本来的worker上rpc-read）
			+ 还记得map worker ok后会发message给master，master只接受一个，如果有一个message描述的是一个completed task，则会忽略

		+ 对于正在进行的task，无论是map worker还是reduce work，都将state init为idle

		>被failed reduce worker不需要re-executed是因为它们的output已经被存储在GFS上了
		
		这样简单的设计就让MapReduce有很强的弹性

	+ master failed：这是一个中心式的分布式系统，如果master寄了，我们就认为它寄了
		>其实可以通过定时快照master的状态来回复。
