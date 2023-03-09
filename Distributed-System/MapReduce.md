>论文在MIT6.824[官网](http://nil.csail.mit.edu/6.824/2022/schedule.html)给出[链接](http://nil.csail.mit.edu/6.824/2022/papers/mapreduce.pdf)，同时网上有诸多论文翻译作为辅助资料
>>这篇论文写的非常的好，读起来简直是享受。如果你对算法有一定感情，一定会惊艳于函数式编程的奥妙

+ zweix的注解：
	+ 区分`worker`和`master`、`task`和`job`的概念（主要在实现部分），worker是系统中的一个物理机器，master是特殊的worker，每个work（无论是Map worker和Reduce worker）都会读入一些文件并处理，一个文件的读入和处理就是一个task，一个worker上可能运行多个Map或Reduce函数，worker处理这些文件并分给这些函数，一个运行的函数就是一个job
		>这里对task和job的界限好像不是那么明确
		
	+ 整个系统的存储基于GFS, Google File System（又是一篇论文），在这里把它当做黑盒就可以了。

---

+ 意义：Google面临着对大量数据的运算，只有分布式的部署才能在可接受的时间范围内解决，但分布式是一个复杂问题，工程师必须具备分布式开发的能力，同时必须要面对分布式中诸如并行运算、容错、本地优化和负载均衡等等问题。Google希望将这些细节封装起来，使工程师将注意力集中在要解决的问题上，甚至不具备分布式开发的能力也能充分使用分布式的性能。
	>这里的实现是受限制的restricted的，需要工程师将原本的算法转换成一个符合*mapreduce specification*的实现

+ 启发：启发于函数式编程语言的*Map*和*Reduce*原语primitives，有些问题可以转换成这样的算法模型（或者该模型的组合）：这个算法模型由多个Map函数和多个Reduce函数组成
	```
	map    (k1. v1)       -> list(k2, v2)
	reduce (k2, list(v2)) -> list(v2)
	```
	+ 一个map函数通常读入一个文件，比如key是文件名、value是文件内容，然后输出一些键值对的列表，这些键值对被称为“中间键值对”
	+ 每个reduce函数从各个Map输出的中间键值对中选择某一个键的所有值进行计算

---

+ 评估：
	+ 可行性：上面说“某些问题”，在论文中阐述了较多的案例。
		>在上课的学生提问中，老师也提到设计这样的算法其实也不简单

	+ 可扩展性：上面我们发现map的处理是“上下文无关”的，也就是说如果map内的算法是“确定的”，那么一个任务拆分成多个map去处理和单个map处理的结果应该是等价的，同时每个reduce只关注每个中间键值对的某个键，如果map们的输出是确定的，那么reduce接受的数据也是确定的。  
		即我们可以通过增加机器来更快的完成任务
		>关于“确定性”的问题在论文中也讨论了如果map和reduce是不确定的情况

那么MapReduce框架的用户只需要考虑如果将问题转换成上面的程序模型，即可利用框架实现分布式的部署，而用户不用考虑分布式所面临的并行运算、容错、本地优化和负载均衡等等问题。

---

一个MapReduces在一个程序中往往作为子程序，由于启发于函数编程的原语，甚至可能多个MapReduce子程序先后运行完成任务，所以我们可以把MapReduce看做一个大函数，下面称为mr。

一个mr的输入被split成**M**份，即有M个Map worker，中间data通过一个哈希取模分成**R**份，即有R个Reduce worker，输出R个文件。
>从性能考虑，Task的数量应该远大于Worker的数量

+ worker：master（实验中被称为coordinator）、Map worker、Reduce worker

进入mr函数，部署集群，map worker处理被split的输入，然后将中间data存在desk并向master发信号，master指派reduce通过RPC读入这些data并处理，其输出直接在mr的文件系统中
>后面会讲到，一个task可能有多个worker在做
>+ map task：无所谓，结果在对应map worker的desk中，不会影响mr
>+ reduce task：虽然它们工作在同一个文件系统中，但是每个task写入的文件不是一个，关键在于最后的rename，这个动作由DFS保证原子

+ Master：定期ping worker
	+ data structure：
		+ status of **task**（空闲、工作、完成）
		+ 中间data info
	+ 对于没有resp的worker，认为它G了，对于它完成的task
		+ Map Task重新运行（因为这玩意存在Map worker的desk，拿不出来）
		+ Reduce Task不需要，它的output已经在DFS中了
	+ master failure：**认为**mr failure
		>虽然可以通过对master的data定时备份然后找新机器重启，但是这样在工程上是不值当的。

---

+ 如果一个worker运行时间很长而没有完成（straggler）呢？mr选择在运行后期有大量机器空闲时一起完成余下的task
+ 还记得中间data是经过某种sort最后被reduce input的，如果key是url，我们想一个host的url在同一个output file，hash肯定不能保证，可以定制这部分。

---

+ 效果：
	+ 程序的设计和实现更加容易，且代码量急剧减少
	+ 将问题的处理和分布式的部署解耦，在项目修改时快很多
	+ 程序运行更流程且很容易扩展
