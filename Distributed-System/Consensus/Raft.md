Raft是一个管理replicated log的consensus algorithm
>容错的一个方法是复制，复制就要面对一致性问题，保持一致性的方法有State Transfer和Replicated State Machine，后者的一个实现方式就是replicated log

+ Replicated State Machines
	+ 一言以蔽之：分布式要面临容错问题，容错的一个方法是复制，复制就要面对一致性问题，保持一致性的方法有State Transfer转移和Replicated State Machine复制状态机，后者的一个实现方式就是Replicated Log复制式日志。
	+ 一图胜千言：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/Consensus/复制式状态机架构.png" alt="复制式状态机架构" style="vertical-align:top">
---

## Raft共识算法

共同选举一个leader，它有管理replicated log的完全职责，它接受来自client的log entries，复制给其他机器，并在适当时候让它们将log应用到各自的状态机上，leader能决定新entry放在log的哪个位置（而不必咨询其他机器）（数据也是从leader流向其他结点），leader可能fail or disconnected，则选举新leader

基于这个机制，Raft将共识问题分解成下面三个相对独立的子问题

### Leader Election

### Log replication

### Safely




1. 共同选举一个leader

3. 选举leader
4. 给该leader管理replicated log完全职权
5. leader接受来自client的log entries，leader复制给其他结点，