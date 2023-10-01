[DB Rank](https://db-engines.com/en/ranking)

+ Consistency（一致性）在不同语境下的含义
	+ 分布式领域中的Consistency即CAP理论中的“C”，严格的说应该值的是[Linearizability](https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf)中的一致性模型。
	+ 数据库领域中的Consistency翻译成中文是一致性（或者说内部一致性（这个是和下面提到的外部一致性对应），但是普遍就叫一致性），它指的是ACID中的C，所以这个应该严格上来说应该是Consistency in ACID，指的是事务的执行一定保证数据库终端数据的约束不被破坏。
	+ 数据库领域中还有External Consistency外部一致性，是[这篇论文](https://www.semanticscholar.org/paper/Information-storage-in-a-decentralized-computer-Gifford/fafaebf830bc900bccc5e4fd508fd592f5581cbe?p2df)（3.1节），先定义Serializability可串行化，再定义External Consistency外部一致性，指的是符合绝对时间约束的Serializability，所以它描述的应该是ACID中的“I”隔离性。

+ 外部一致性为什么还需要在可串行化之上再加上一个“绝对时间”的限制？因为可串行化描述是单机数据库，而外部一致性描述是分布式数据库，即一个写、一个读、一次执行，但是读可能为空，这是符合可串行化的，但是也真实的发生在分布式数据库中了，所以要加上绝对时间的限制。

+ Reference：
	+ CMU 15445：
		+ B站Moody-老师

## Primer

+ 术语名词：Data数据 | DB, DataBase：数据库 |DBMS, DataBase Managment  System数据库管理系统

+ Data Model：
	+ SQL：
		+ relational
	+ no-SQL：
		+ key value pair
		+ graph
		+ document
+ DML，Data mainipulation languages：增删改查  
	+ Procedural：带过程的DML，即relational algebra关系代数
	+ No-Procedural/Decalarative：不带过程的，即relational calculus
