存储的相关问题在计算机很多领域都有讨论，有很多相互借鉴，相互连通的东西。

+ 数据库面临的问题：
	+ 存储是顺序访问较于随机访问快很多，但是我们不能对用户提要求，要在内部对用户的要求改成尽可能改成顺序访问更多的
	+ Flushing dirty pages to disk in the correct order
	+ Specialized prefetching
	+ Buffer replacement policy
	+ Thread/process scheduling

+ 数据库运行流程
	+ Disk：DataBase File
		+ Pages
			+ Directory
			+ Block
				+ Header
	+ Memory：Buffer Pool
		+ Pages
			+ Directory
			+ Block

	+ Execution Engine

--

+ mmap, memory mapping：Disk大，Physical Memory小，mmap提供Virtual Memory，和disk一样大，让软件直接访问虚拟内存，然后mmap把虚拟内存需要的东西从硬盘load的物理内存中，然后建立物理内存对应文件到虚拟内存中的链接。问题是上面的方案对只读没问题，但是对并发写怎么办呢？于是衍生出了很多东西madvice、mlock、msync


### How the DBMS represents the database in files on disk

#### File Storage

+ storage manager

+ page is a fixed-size block of data


#### Page Layout

#### Tuple Layout
