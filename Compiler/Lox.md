REPL

这是一份编译原理学习资料中使用的自制语言，我们会在Lox的功能中看到一个语言设计的方方面面

+ 风格：
	+ 类似JavaScript
	+ 动态类型
	+ Automatic memory management
		+ reference couting
		+ tracing garbage collection

+ 注释：`//`
+ biild-in statement: 
	+ print

+ data types
	+ Booleans: `true` and `false`
	+ Numbers: double-precision floating point
	+ Strings: enclosed in double quotes
	+ `nil`

+ Expresions
	+ Arithmetic
		+ binary operators/infix operator: +-*/
		+ prefix operators: -
		+ 其中+可支持Strings
	+ Comparison and equality
		+ < <= > >=
		+ =\=, !=
			+ 返回隐式转换
	+ Logical operators
		+ `!`
		+ `and` `or`
			+ short-circuit短路
			+ 可以用来模拟控制流
	+ Precedence and grouping：`()`

+ Statements: `;`
	+ expression statement
	+ block: `{}`

+ Variables: `var`，动态类型，不需要指明类型，也不需要初始化，但是这样的语句相当于声明

+ Control Flow：
	+ `if`: same C
	+ `while`: same C
	+ `for`: same C

+ Functions: 
	+ 定义：`fun ...`，其余same C
	+ `return` statement
		+ 没有默认`nil`

+ 关于参数：
	+ argument：actual parameter实参，给到函数的值
	+ parameter：formal parameters形参，在函数中的变量

+ Closures: 函数在Lox中是**first class**一等公民：可以赋值给变量

+ Class：
	+ 定义：`class ...`，在类中的方法不用关键字`func`
	+ 属性：可以直接向实例中添加属性
		+ 在类内部通过`this.`访问
	+ 构造函数`init`
	+ Inheritance：`class NewClass < BaseClass`
		+ 通过`super`访问

	+ 类在Lox中也是一等公民

+ OOP语言：
	+ [classes](https://en.wikipedia.org/wiki/Class-based_programming)类
		+ instances实例和类classes
	+ [prototypes](https://en.wikipedia.org/wiki/Prototype-based_programming)原型：比如Golang中的接口就是原型

### 语法的形式化表达

+ Literals: Numbers, strings, Booleans, nil
+ Unary expression: !取非, -取负
+ Binary expressions: +-\*/, =\= \!\= < <= > >=
+ Parentheses: ()

```
expression     → literal
               | unary
               | binary
               | grouping ;

literal        → NUMBER | STRING | "true" | "false" | "nil" ;
grouping       → "(" expression ")" ;
unary          → ( "-" | "!" ) expression ;
binary         → expression operator expression ;
operator       → "==" | "!=" | "<" | "<=" | ">" | ">="
               | "+"  | "-"  | "*" | "/" ;
```