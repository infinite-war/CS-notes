## config

+ `ccache`：顾名思义，一个大型项目的每次修改调试都需要重新编译，实际上只需要重新编译小部分，但是默认全部重新编译，该软件可以识别只编译修改过的
	+ config：rc：`export PATH=/usr/lib/ccache:$PATH`，要放在前面，此时`which gcc`为`/usr/lib/ccache/gcc`

## args

+ `make`命令是单线程的，我们可以通过`lscpu`查看机器cpu数量，然后通过添加参数`-j?`来多CPU并行编译，其中`?`为数字
	>`lscpu`查看机器cpu数量