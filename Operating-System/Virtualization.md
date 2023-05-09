+ 虚拟化体现在两个方面：
	+ time sharing：比如一个CPU运行多个程序
		+ scheduling调度 policy策略
	+ space sharing

+ 
	+ program是静态的概念
	+ process是动态的概念

+ machine state
	+ menory，指令在内存、数据在内存，所以内存是address space寻址空间
	+ register，很多指令明确读取和更新寄存器
		+ program counter(PC)/instruction pointer(IP)
		+ stack pointer and associated frame pointer，栈、管理函数参数、本地变量和返回地址
	+ IO information
