+ `make`命令是单线程的，我们可以通过`lscpu`查看机器cpu数量，然后通过添加参数`-j?`来多CPU并行编译
+ 还能继续加速，要知道对于一个大项目，编译那么长时间，每次修改再编译，实际上每次修改只是很小的部分，很大的部分不需要重新编译  
	ccache
	+ 配置：
		```bashrc
		export PATH=/usr/lib/ccache:$PATH
		export CCACHE_COMPILERCHECK=content
		export CCACHE_DIR=~/.cache
		```
		+ sudo ln -s /usr/lib/ccache/gcc /usr/bin/gcc
+ which gcc和g++检查下，应该到是/usr/bin/gcc. 作为一个RTFM的练习, 接下来你需要阅读man ccache中的内容, 并根据手册的说明, 在.bashrc文件中对某个环境变量进行正确的设置. 如果你的设置正确且生效, 重新运行which gcc, 你将会看到输出变成了/usr/lib/ccache/gcc. 如果你不了解环境变量和.bashrc, STFW.