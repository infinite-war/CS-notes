+ Page/Block is a fixed-size block of data.
	+ contain tuples, meta-data, indexes, log records，且只包含一种
	+ 可能里面还有一个数据结构支出自己是什么类型
	+ 应该有唯一ID

+ 从内存角度对DB分类：
	+ Disk-oriented DBMS
	+ Memory-oriented DBMS

+ Disk-oriented DBMS数据库运行流程
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

+ mmap, memory mapping：Disk大，Physical Memory小，mmap提供Virtual Memory，和disk一样大，让软件直接访问虚拟内存，然后mmap把虚拟内存需要的东西从硬盘load的物理内存中，然后建立物理内存对应文件到虚拟内存中的链接。问题是上面的方案对只读没问题，但是对并发写怎么办呢？于是衍生出了很多东西madvice、mlock、msync

+ 数据库面临的问题：
	+ 对非易失性存储介质的随机access比顺序access慢得多，但是我们不能限制用户的行为，所以要尽可能的进行转换，最大化顺序access
	+ Flushing dirty pages to disk in the correct order脏数据什么时候存回去？
	+ Specialized prefetching预取问题
	+ Buffer replacement policy内存中的缓冲区的更换策略
	+ Thread/process scheduling并发调度

### How the DBMS represents the database in files on disk

#### File Storage

+ storage manager：维护DB的file，有较于OS更适合DB的文件管理



#### Page Layout

#### Tuple Layout
