## OOP
>object-oriented projramming面向对象程序设计

+ 核心思想：数据抽象（类的接口与实现分离）、继承和多态

## 函数重载-多态

+ 函数重载
	+ 默认参数相当于函数重载
+ 运算符重载：将多态的概念扩展到运算符
+ 虚函数：基类指针数组使用对象方法与指向类型有关$\rightarrow$同一表达式行为不同

## 面向对象-抽象

## MISC

+ [aggregate聚合](https://en.cppreference.com/w/cpp/language/aggregate_initialization)
	+ 聚合断言：[判断一个类型是否是断言](https://en.cppreference.com/w/cpp/types/is_aggregate)

	+ 属性：
		+ 所有成员都是`public`的
		+ 没有定义任何构造函数
		+ 没有类内初始化
		+ 没有基类、也没有`virtual`函数

	+ 初始化：提供花括号括起来的成员初始值列表、顺序对应
	+ 字面值常量类：数据成员都是字面值类型的聚合类
		+ 属性：
			+ 数据成员都必须是字面值类型
			+ 至少有一个`constexpr`构造函数
			+ 使用默认析构函数
