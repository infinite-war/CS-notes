这是一份编译原理学习资料中使用的自制语言，我们会在Lox的功能中看到一个语言设计的方方面面

+ 风格：
	+ like js
	+ 动态类型
	+ gc

+ 注释：`//`（只提供单行注释）

+ build-in statement:
	+ print

+ native function:
	+ clock()

+ data types:
	+ Booleans: `true` `false`
		+ 这里定义false和nil是假，其它是真
	+ Numbers: double-precision floating point
	+ Strings: enclosed in double quotes
	+ `nil`

+ Expresions: 
	+ Arithmetic:
		+ binary operators/infix operator: + - \* /
		+ prefix operators: -
		+ 其中+可支持Strings
	+ Comparison and equality
		+ < <= > >=
		+ =\= !=
			+ 禁止隐式转换
	+ Logical operators
		+ `!`
		+ `and` `or`
			+ short-circuit短路
	+ Precedence and grouping：`()`

	优先级和结合性：同C

+ Statements: `;`
	+ expression statement
	+ block: `{}`

+ Variables: `var`，动态类型，不需要指明类型，也不需要初始化，但是这样的语句相当于声明

+ Control Flow：
	+ `if`: same C
	+ `while`: same C
	+ `for`: same C

+ Functions: 
	+ 定义：`fun ...`，其余同C
	+ `return` statement
		+ 没有默认`nil`
	+ Closures: 函数在Lox中是**first class**一等公民：可以赋值给变量

+ Class：
	+ 定义：`class ...`，在类中的方法不用关键字`func`
	+ 属性：可以直接向实例中添加属性
		+ 在类内部通过`this.`访问
	+ 构造函数`init`
	+ Inheritance：`class NewClass < BaseClass`
		+ 通过`super`访问

	+ 类在Lox中也是一等公民

### topic

+ 作用域与环境，前者是理论，后者是实现机制
	+ 块作用域结束后里面的变量应该不在
	+ 不是粗暴的删除，因为可能全局也有同名的，所以块作用域应该是shadow遮蔽
	+ 而且还要考虑块作用域引用了全局的变量

