+ 学习资料推荐：
	+ [ostep](http://www.ostep.org/)，南大蒋岩炎老师称之为操作系统最好的自学书籍
		+ 完全开源，但是各个章节分成多个PDF，[这个脚本](https://github.com/zweix123/zyutils/blob/master/spider/get_ostep_all_pdf_and_merge.py)的功能是爬取所有章节并拼接成一份PDF
			+ 上面这个脚本是同步，不是那么快，有相对官方的汉化版书籍，我又写了[一个爬虫](https://github.com/zweix123/zyutils/blob/master/spider/get_zh_ostep_all_pdf_and_merge.py)，这个具有超过的并发
		+ 作者GitHub[链接](https://github.com/remzi-arpacidusseau)

	+ MIT6.S081
		+ [野生讲义翻译](https://mit-public-courses-cn-translatio.gitbook.io/mit6-s081/)

+ OS Deisgn Goals:
	+ Abstractions
	+ Virtualize Resources
	+ Concurrency(Multiplex)
	+ Store Persistently
	+ Protection
		+ Isolation：故障不互相影响
		+ Sharing and Security
	+ Performance
	+ Reliability
	+ else：
		+ energy-efficiency
		+ mobility

+ 操作系统的分层设计
	+ Userspace：
	+ Kernel：一个特殊的程序，总在运行，首先运行
		+ 管理用户空间进程
		+ 管理硬件资源，以供用户空间的程序使用
		+ 内置服务
			+ 文件系统
			+ 进程管理系