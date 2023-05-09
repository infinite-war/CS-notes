Consensus Algorithm译为共识算法或者一致性协议甚至一致性算法，在我的笔记中不做明确区分

+ **ELP不可能定理**：No completely asynchronous consensus protocol can tolerate even a single unannounced process death  
	>该定理来自Fisher、Lynch 和 Paterson的[论文](https://ilyasergey.net/CS6213/_static/02-consensus/flp.pdf)

	但是**科学告诉你，什么是不可能的；工程则告诉你，付出一些代码，可以把它变成可行**，这就是工程的魅力。

+ 共识算法特征
	+ 在任何非拜占庭条件下都能保证安全
	+ 只要**多数**结点工作、能通信，则整体系统功能完全可用
	+ 可从持久存储中恢复
	+ 不依赖时序保证一致性
	+ 少量慢响应机器不影响整体性能



+ Raft资料：
	+ https://thesquareplanet.com/blog/students-guide-to-raft/
	+ http://nil.csail.mit.edu/6.824/2022/labs/raft-locking.txt
	+ http://nil.csail.mit.edu/6.824/2022/labs/raft-structure.txt

	+ https://arthurchiao.art/blog/raft-paper-zh/
	+ https://zhuanlan.zhihu.com/p/91288179
	+ 一个翻译：https://arthurchiao.art/blog/raft-paper-zh/