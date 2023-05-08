Raft是一个管理replicated log的consensus algorithm
>容错的一个方法是复制，复制就要面对一致性问题，保持一致性的方法有State Transfer和Replicated State Machine，后者的一个实现方式就是replicated log



+ Raft，一个管理replicated log复制式日志的共识算法，结果于Paxos等价，但更容易理解




+ 怎么实现的呢？


+ 共同选举出来一个leader
+ 给予这个leader管理replicated log的完全职责
+ leader接受来自client的log entries，然后复制给其他节点，并在安全时，告诉这些节点这些entries应用到他们各自的状态机中



+ 资料：
	+ https://thesquareplanet.com/blog/students-guide-to-raft/
	+ http://nil.csail.mit.edu/6.824/2022/labs/raft-locking.txt
	+ http://nil.csail.mit.edu/6.824/2022/labs/raft-structure.txt

	+ https://arthurchiao.art/blog/raft-paper-zh/
	+ https://zhuanlan.zhihu.com/p/91288179