## Intro

+ translation program的区分：
	+ Compiler编译器：Program经过compiler输出executable file，执行exe输入Data，输出Output
	+ Interpreter解释器：Program和Data一起同时进入Interpreter，输出Output

	编译和解释有巨大的相似，所以下文不再区分，除非特殊声明，统一使用编译来表示编译和解释

+ 词法分析工具：lex(Unix) <- flex(Linux)：C的扩展，文件扩展名为`l`，通过编译器将其转换成C语言进行编译 
+ 语法分析工具：yacc(Unix) <- bison(Linux)：文件扩展名为`y`

## overview

+ 整个编译过程通常分成front end、middle end、back end
	+ 这个middle end似乎有点怪，几乎可以直接理解为中间代码
	+ 为什么如此划分？想一下，如果你想为`x`个语言编写`y`个指令集机器的编译器，则需要写$x \times y$个软件；如果对于每个语言，分别写个软件将它们转换成中间代码，然后在分别写个软件将中间代码转换成各个指令集的硬件代码，这就只需要`x + y`个

![mountain](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Compiler/mountain.png)

前端：
1. Scanning/lexing/lexical analysis: txt -> token
2. Parsing: token -> parse tree/abstract syntax tree(AST)
3. Static Analysis/Semantic Analysis: 
	+ 比如为identifier和scope进行binding or resolution
	+ 比如type check
	
	这些信息保存在哪里呢？

中端：intermediate representation, IR中介码
4. Optimization:
	+ 比如常量折叠

后端：
5. Code Generation
	1. 生成机器码
	2. 生成bytecode字节码

		+ virtual machine, VM