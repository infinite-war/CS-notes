+ Golang处理并发的方案：
	+ 1. `Channels`
		+ 不需要共享内存
	+ 2. `locks` and `condition variables`
		+ 需要共享内存


+ 区分并发和并行
	+ concurrency并发：交替的管理多个“进程、线程“
	+ 并行。同时，同时做很多