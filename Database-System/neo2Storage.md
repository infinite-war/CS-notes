存储的相关问题在计算机很多领域都有讨论



顺序肯定比随机快，但我们不能要求用户用顺序存储，所以要想办法最大化的把随机变成顺序


+ 一般流程：
	+ Disk：DataBase File
		+ page
			+ Directory
			+ black
				+ header
	+ Memory：Buffer Pool
		+ page
			+ Dir
			+ 缓存
	+ Execution Engine

+ mmap, memory mapping：Disk大，Physical Memoty小，前者的东西不可能全部load到后者上，mmap提供Virtual Memory虚拟内存，和desk一样大，所以软件直接访问虚拟内存，然后mmap把虚拟内存中的东西load到物理内存里，然后把物理内存的位置链接到虚拟内存中。本质就是
	+ 上面是只读，要是并发写就G
	+ 衍生出很多：madvise，mlock，msync

+ 面对的问题
	+ Flushing dirty pages to disk in the correct order
	+ Specialized prefetching
	+ Buffer replacement policy
	+ Thread/process scheduling


--
How the DBMS represents the database in files on disk

+ File Storage
	+ storage manager：管理file像page
	+ page is a fixed-size block of data
		+ 有个id

>page
>+ hardware page
>+ os page
>+ database base



+ Page Layout
+ Tuple Layout