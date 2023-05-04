## 1.lexing词法分析

+ 
	+ lexemes词素: lexing中的每一组具有某些含义的最小序列
	+ Tokens: 将lexemes和*其他数据*放在一起

+ token data struct
	+ Token type
	+ Literal value字面量
	+ Location info

+ regular language and expression正则语言和表达式
	+ Python的语法不是regular的，因为它缩进敏感，所以要比较连续行的开头空格数量，regular language无法实现

+ 关于分号和全大写关键字，都已经是时代的眼泪的，关于的分号的处理，可以用换行符尝试替代，但是这样的方法在不同的语言中有[不同的处理方式](https://readonly.link/books/https://raw.githubusercontent.com/GuoYaxiang/craftinginterpreters_zh/main/book.json/-/4.%E6%89%AB%E6%8F%8F.md#design-note-implicit-semicolons)。

## 2.syntactic analysis句法分析

### 形式化语言表达语法

+ [Formal grammar形式化语言](https://en.wikipedia.org/wiki/Formal_grammar)：有一组原子片段，即alphabet，分别对应一组string（由alphabet中的letter组成的sequence）
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

### 递归下降建立抽象语法树
abstract syntax tree, AST抽象语法数

怎么构建建立AST的解析器呢？有很多中工具，`LL(k)`、`LR(1)`、`LALR`

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

+ error recovery：
	+ panic mode：当遇到错误，它进入恐慌模式，要先进行synchronization同步，将当前的状态和下面的token的状态对齐，使后面是对的。

+ 抽象语法树的应用
	+ 直接在AST上运行
	+ 不依赖运行时状态的工作
		+ 没有副作用
		+ 没有控制流

## 3.semantic analysis语义分析

不是必须的，概念性的

## +在抽象语法树上运行


## +字节码