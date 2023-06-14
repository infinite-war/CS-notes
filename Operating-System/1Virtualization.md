+ Virtualizing resources：
	+ CPU
	+ Memory


## Process Abs

Process is a running Program

+ CPU Time Sharing：实现某种illusion，多个程序同时运行在一个CPU上
	+ 性能开销
	+ Scheduling调度Policy策略
	+ mechhanisms
		+ context switch

+ Process Abstracion：
	+ machine state
		+ memory，因为指令在内存、数据也在内存，所以内存的address space寻址空间是process的一部分
		+ register，很多指令明确读取和更新寄存器
			+ program counter(PC)/instruction pointer(IP)：指向下一个指令
			+ stack pointer and associated frame pointer
				+ 栈：管理函数参数、本地变量和返回地址
		+ IO information

	+ Process States：
		+ Running
		+ Ready
		+ Blocked
		+ initial
		+ final

	+ Data Structure
		+ process list
		+ context for every process/Process Control Block
			+ 

+ Process API：
	+ `Create`：
		1. load **pieces** of code and static data from desk into memory
		2. allocat memory for program's run-time stack and heap
		3. file descriptiors
	+ `Destory`
	+ `Wait`
	+ `Miscellaneous Control`
	+ `Status`

paging and swapping