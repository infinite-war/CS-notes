>这是一份编译原理学习资料中使用的自制语言

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

+ misc
	+ 变量存在滞后性，先声明的函数可以使用在后面声明的全局变量，为了递归的方便实现


### 完整语法
```
// 语法
program        → declaration* EOF ; // Lox是一系列“声明”, 有一个《特殊》的声明是“语句”
// 声明
declaration    → classDecl
               | funDecl
               | varDecl
               | statement ;

classDecl      → "class" IDENTIFIER ( "<" IDENTIFIER )?
                 "{" function* "}" ;
funDecl        → "fun" function ;
varDecl        → "var" IDENTIFIER ( "=" expression )? ";" ;
// 语句: 声明会产生绑定, 语句则不会
statement      → exprStmt
               | forStmt
               | ifStmt
               | printStmt
               | returnStmt
               | whileStmt
               | block ;

exprStmt       → expression ";" ;
forStmt        → "for" "(" ( varDecl | exprStmt | ";" )
                           expression? ";"
                           expression? ")" statement ;
ifStmt         → "if" "(" expression ")" statement
                 ( "else" statement )? ;
printStmt      → "print" expression ";" ;
returnStmt     → "return" expression? ";" ;
whileStmt      → "while" "(" expression ")" statement ;
block          → "{" declaration* "}" ;
// 实用规则: 上面有些的表达比较复杂, 下面是一些中间量
function       → IDENTIFIER "(" parameters? ")" block ;
parameters     → IDENTIFIER ( "," IDENTIFIER )* ;
arguments      → expression ( "," expression )* ;
// 表达式
expression     → assignment ;

assignment     → ( call "." )? IDENTIFIER "=" assignment
               | logic_or ;

logic_or       → logic_and ( "or" logic_and )* ;
logic_and      → equality ( "and" equality )* ;
equality       → comparison ( ( "!=" | "==" ) comparison )* ;
comparison     → term ( ( ">" | ">=" | "<" | "<=" ) term )* ;
term           → factor ( ( "-" | "+" ) factor )* ;
factor         → unary ( ( "/" | "*" ) unary )* ;

unary          → ( "!" | "-" ) unary | call ;
call           → primary ( "(" arguments? ")" | "." IDENTIFIER )* ;
primary        → "true" | "false" | "nil" | "this"
               | NUMBER | STRING | IDENTIFIER | "(" expression ")"
               | "super" "." IDENTIFIER ;
// 词法, 注意这里的非递归的, 所以是正则的
NUMBER         → DIGIT+ ( "." DIGIT+ )? ;
STRING         → "\"" <any char except "\"">* "\"" ;
IDENTIFIER     → ALPHA ( ALPHA | DIGIT )* ;
ALPHA          → "a" ... "z" | "A" ... "Z" | "_" ;
DIGIT          → "0" ... "9" ;
```