在写xv6 lab时的笔记，包括坑点和随手笔记，估计这样的笔记不可避免的涉及剧透，请酌情观看

+ 在read system call中，其中的第三个arg是“期待字节数”
	+ 如果fd是动态的，比如pipe，会阻塞当前进程，等待pipe中字节数足够
	+ 只有过程中出现问题了，才会error，返回-1
	+ 那什么时候小于这个数字呢？很有可能在文件中， 那么read是怎么知道是真的不足了而不是暂时不足了？是通过EOF，文件末尾有EOF，所以如果close pipe这个操作也是往管道中放入EOF

+ lab2的调试按照manual的步骤是运行不起的，把问题的具体描述和解决方案放在[so](https://stackoverflow.com/questions/76025743/error-shown-a-problem-internal-to-gdb-has-been-detected-when-doing-xv6)上了
+ 