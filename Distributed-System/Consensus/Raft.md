Raft是一个管理replicated log的consensus algorithm
>容错的一个方法是复制，复制就要面对一致性问题，保持一致性的方法有State Transfer和Replicated State Machine，后者的一个实现方式就是replicated log

### replicated state machines

一言以蔽之：分布式要面临容错问题，容错的一个方法是复制，复制就要面对一致性问题，保持一致性的方法有State Transfer转移和Replicated State Machine复制状态机，后者的一个实现方式就是replicated log复制式日志。

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/Consensus/复制式状态机架构.png)

### mechanism

1. 选举leader
2. 给该leader管理replicated log完全职权
3. leader接受来自client的log entries，leader复制给其他结点，