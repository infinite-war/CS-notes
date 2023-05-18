+ 学习资料推荐：
	+ [ostep](http://www.ostep.org/)，南大蒋岩炎老师称之为操作系统最好的自学书籍
		+ 完全开源，但是各个章节分成多个PDF，[这个脚本](https://github.com/zweix123/zyutils/blob/master/spider/get_ostep_all_pdf_and_merge.py)的功能是爬取所有章节并拼接成一份PDF
			+ 上面这个脚本是同步，不是那么快，有相对官方的汉化版书籍，我又写了[一个爬虫](https://github.com/zweix123/zyutils/blob/master/spider/get_zh_ostep_all_pdf_and_merge.py)，这个具有超过的并发
		+ 作者GitHub[链接](https://github.com/remzi-arpacidusseau)

	+ MIT6.S081
		+ 野生讲义翻译https://mit-public-courses-cn-translatio.gitbook.io/mit6-s081/


+ what is OS?virtual machine?standard library?resource manager
+ design goals：
	+ virtualize resources
	+ 虚拟化关系到concurrency
	+ store persistently
	+ 为了方便和容易使用的abstractions
	+ performance（minimize the overhead）
	+ protection
		+ isolation
		+ security
	+ reliability
	+ energy-efficiency
	+ mobility