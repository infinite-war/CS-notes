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
		+ 这里定义false和nil是假，其它是真
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
			+ 禁止隐式转换
	+ Logical operators
		+ `!`
		+ `and` `or`
			+ short-circuit短路
			+ 可以用来模拟控制流
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

+ 作用于scope：定义了名称映射到特定实体的一个区域，多个作用于允许相同名称在不同的上下文指向不同的内容。
	+ Lexical scop/static scope，就是可以通过阅读知道作用域，比如大括号
	+ 动态作用域，就是多态

+ 作用域与环境，前者是理论，后者是实现机制
	+ 块作用结束后里面的变量应该不在
	+ 但是不同粗暴的删除，因为可能全局也有同名的，所以块作用域应该是shadow遮蔽
	+ 而且还要考虑块作用域引用了全局的变量
 