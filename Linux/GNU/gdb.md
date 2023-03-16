>GDB, GNU Debugger

+ 学习资料：
	+ [QuickStart](https://www.cprogramming.com/gdb.html)

```bash
starti  # 执行程序第一条语句

set args argument1 argument2 ...


bt  # 打印栈

c  # continue  到下一个断点
r  # run
s  # 单步执行，执行一行源代码
n  # 单步执行但不进入函数

finish  # 执行指导当前函数返回

p ... 打印变量或寄存器的值
b ... # 打断点


x # 扫描内存

watch  # 设置监视点

layout src  # 查看源码



help xxx
```