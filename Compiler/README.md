参考学习资料：《Crafting interpreters》，全开源，我愿称之为学习编译原理的最好的第一本书
https://github.com/munificent/craftinginterpreters
https://readonly.link/books/https://raw.githubusercontent.com/GuoYaxiang/craftinginterpreters_zh/main/book.json/-/5.%E8%A1%A8%E7%A4%BA%E4%BB%A3%E7%A0%81.md
## Intro

+ translation program的区分：
	+ Compiler编译器：Program经过compiler输出executable file，执行exe输入Data，输出Output
	+ Interpreter解释器：Program和Data一起同时进入Interpreter，输出Output

	实际上这个也不是完全划分的，比如CPython，它显然是先将代码转换成字节码，然后对字节码解释

	下文不再区分，除非特殊声明，统一使用编译来表示编译和解释

+ 
	+ 词法分析工具：lex(Unix) <- flex(Linux)：C的扩展，文件扩展名为`l`，通过编译器将其转换成C语言进行编译 
	+ 语法分析工具：yacc(Unix) <- bison(Linux)：文件扩展名为`y`

+ 
	+ single-pass compilers：直接在parser中生成code
		+ 这会限制语言的设计，比如没有全局数据结构存储全局变量，执行顺序可见
		+ 因为当时的内存非常稀有

	+ tree-walk interpreter：在AST中运行
		+ 慢

+ Just-in-time, JIT complitation即时编译：执行代码最快的方式就是将其转换成机器码，所以对解释型的语言在运行时转换成机器码
	+ 能分析哪些区域对性能最关键，对热点进行重编译

### overview

+ 整个编译过程通常分成front end、middle end、back end
	+ 这个middle end似乎有点怪，几乎可以直接理解为中间代码
	+ 为什么如此划分？想一下，如果你想为`x`个语言编写`y`个指令集机器的编译器，则需要写$x \times y$个软件；如果对于每个语言，分别写个软件将它们转换成中间代码，然后在分别写个软件将中间代码转换成各个指令集的硬件代码，这就只需要`x + y`个

+ source-to-source complier/transcompiler：把你的语言转换成其他的语言或者其他语言的中介码

![mountain](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Compiler/mountain.png)

前端：
1. Scanning/lexing/lexical analysis: txt -> token
2. Parsing/syntactic analysis: token -> parse tree/abstract syntax tree(AST)
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

+ runtime
	+ gc
	+ Reflection

## 1.lexing
词法分析

+ 
	+ lexemes词素: lexing中的每一组具有某些函数的最小序列
	+ Tokens: 将lexemes和*其他数据*放在一起

+ token data struct
	+ Token type
	+ Literal value字面量
	+ Location info

+ regular language and expression正则语言和表达式
	+ Python的语法不是regular的，因为它缩进敏感，所以要比较连续行的开头空格数量，regular language无法实现

+ 关于分号和全大写关键字，都已经是时代的眼泪的，关于的分号的处理，可以用换行符尝试替代，但是这样的方法在不同的语言中有[不同的处理方式](https://readonly.link/books/https://raw.githubusercontent.com/GuoYaxiang/craftinginterpreters_zh/main/book.json/-/4.%E6%89%AB%E6%8F%8F.md#design-note-implicit-semicolons)。

## 2.syntactic analysis
句法分析

+ [Formal grammar形式化语言](https://en.wikipedia.org/wiki/Formal_grammar)：有一组原子片段，即alphabet，对于string（由alphabet中的letter组成的sequence）
	+ 那如何写下一个包含无限多有效字符串的语法呢？
		+ derivations派生
		+ productions生成

+ 其实上面我们也已经看到了，有些语法不能用正则语言处理，这个就是同样的处理的工具，当然它的功能更加强大。  
	对照定义，这个工具
	+ 如果用于词法分析中，则单个字符的表就是alphabet，所有的lexeme就是string
	+ 而在句法分析中，则每个token是的letter，然后组合成expression

+ Context-Free Grammars上下文无关语法：形式化语言的一种
	+ 每个生成式有一个head（名称），一个body，从形式上body是一系列符号symbol
	+ 符号有两种：
		+ terminal：字面量，
		+ nonterminal：名称（一个生成式的（即可以是自己））

	我们可以将无限多的字符串打包到一个有限的语法中

这些是概念上的，具体的什么样子的？

+ 巴科斯范式BNF：`name -> symbols;`，终止符是带引号的字符串，非终止符是小写的单词。

	+ 一种扩展语法：
		+ 支持`}`和`()`的组合
		+ 支持`*`、`+`和`?`（正则表达式概念下的）

我们很快遇到问题，对于一个字符串可能有多种生成的方式（意味着多种可能的AST）

+ Precedence优先级
+ Associativity结合性

至此我们建立的AST，怎么将其构建解析器呢？  
有很多中工具，LL(k) LR(1) LALR

+ recursive descent递归下降（自顶向下解析器）：将语法规则直接翻译成命令式代码的文本翻译器，每个规则变成一个函数
	+ Terminal：匹配并消费一个token
	+ NonTerminal：调用规则对应的函数
	+ `*` and `+`：loop
	+ `?`：if

+ 检查语法错误：因为代码解析同样出现于静态分析，比如高亮，所以解析器会大量遇到错误的代码
	+ Detect and report the error
	+ Avoid crashing or hanging

	+ Be fast
	+ Report as many distinct errors as there are
	+ Minimize cascaded errors最小化级联错误

	+ error recovery


