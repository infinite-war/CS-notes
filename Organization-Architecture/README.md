+ Von Neumann冯诺依曼 Processor
	+ **fetch** instruction from memory
	+ **decodes** it
	+ **executes** it
	+ move to next instruction
	and so on

+ 从上到下，越来越慢、越来越大、越来越便宜
	+ ：Volatile
	1. CPU Registers：寄存器
	2. CPU Caches：缓存，多级
	3. DRAM：内存Memory
	+ Disk：Non-Volatile
	4. SSD：固态硬盘
	5. HDD：机器硬盘
	6. Network Storage
	7. Tape Archives

+ 发展历史
	+ 1
	+ 2
	+ Solid State Drive, SSD闪存

## Cache

+ Reference：
	+ [给我树苗的《Cache的基础知识》](https://zhuanlan.zhihu.com/p/632189718)


## 分支预测

+ Reference：
	+ [johnnysswlab的《How branches influence the performance of your code and what can you do about it?》](https://johnnysswlab.com/how-branches-influence-the-performance-of-your-code-and-what-can-you-do-about-it/)

+ Pre：现在CPU一般都有一下几个功能：
	+ Pipeline流水线
	+ Out of order execution乱序执行
	+ Branch prediction分支预测
	+ Speculative execution推测执行TODO

	分支预测主要是为了服务流水线，不然怎么流水出多分支的指令？

+ 在没有分支预测的CPU上，也会提前处理分支后的指令，如果错误了，就重新

+ Vectorization：一下处理多个数据。不论是算还是存

