+ 函数/例程(function)：命名的计算单元。

1. 函数声明——函数原型(function prototype)：语法较于函数定义没有函数体
	+ 函数列表可不指出形参名
2. 函数定义：
	1. 函数头：
		1. 返回类型(return type)：无返回值则为`void`
		2. 函数名字(function name)：
		3. 参数列表(parameter list)：0个或多个，多个用逗号分隔

		+ 如果不接受参数，则参数列表为`void`（显式）或空（隐式）
			>在ANSI C中，函数声明中括号为空意味着不指明形参，需要在定义中确定。

	2. 函数体(function body/statement)：

3. 函数调用：主调函数(calling function)通过调用运算符(call operator)调用被调函数(called function)：

	+ 形参(**parameter**)：函数定义中的参数变量
	+ 实参(**argument**) ：函数调用中的值

+ 函数签名sigature
	+ Effective Modern C++定义：函数返回值和形参类型列表，相当于`std::function`类型参数
	+ 标准定义：形参类型列表

	忽略函数名，`constexpr`和`noexcept`

+ 函数签名sigature（Effective Modern C++定义），即用来描述`std::function`类型参数的部分，函数返回值和形参类型列表

## 特殊函数

+ 主函数：被*启动代码*调用，是程序和操作系统的接口。
	+ 语法：`int main() {}`：返回是告知OS程序运行情况，常用int，默认返回0（正常），若其他则异常
	+ 参数：`int main(int argc, char *argv[]) {}`：其中argc为argv长度（默认设置），`argv[0]`为程序名（故参数从1开始）

+ 递归函数：

+ 内联函数：
	+ 在函数的原型和定义前加上关键字`inline`，通常做法是省略原型，直接定义。
	+ 提示编译器将函数内联，即优化掉函数调用相关的指令，将函数体内联支调用处，免去调用的开销。但这个指示是非强制性的，一方面不加编译器也会内联，加了编译器也可以不内联，所以这个语义应该不再使用。
	+ Modern C++中该关键字的目的是允许函数（或变量（C++17））在程序中有多于一次的定义，或者说可以直接在头文件给出函数的完整定义，而不必声明和定义分离，对于想提供header-only库的开发者非常关键。
 
+ `constexpr`函数：本质是编译器计算，要求返回类型和所有形参都是字面量，注意返回的值不一定以为着其常量性。

## 参数传递

+ 形参引用实参：实参被引用传递(passed by reference)/函数被传引用调用(called bu reference)：获得实参控制权  
	形参值拷贝实参：实参被值传递(passed by value)/函数被传值调用(called by value)                    ：获得值拷贝

	+ 传引用较于传值因避免拷贝故花销更少

+ 形参是指针：虽然是值传递，但是可以通过指针间接影响值

+ 形参实参类型的cv限定：TODO

+ 数组做参数：
	+ 数组形参：`type funcName(..., type arr[], ...);`
	+ 数组引用形参：`type funcName(..., type (&arr)[size], ...);`
		+ 这里的`size`构成类型的一部分

	+ 高维数组：
		```cpp
		type funcName(type (*arr)[size]);
		type funcName(type arr[][size]);
		```

		即除了第一维之外的长度都有标注。


+ 可变形参：

## 信息返回

+ 返回引用：
	+ 注意引用局部变量
+ 返回数组类型：因为数组不会自动拷贝，所以本质是返回数组的指针或引用。
+ 尾置返回类型，见泛型编程函数模板部分

## 函数多态

默认函数使得函数的参数列表有了一定的灵活性  
函数重载不仅使参数列表的长度可以变化（功能覆盖默认参数（但是多了代码）），其数据类型也是可以调整的（比如可用于对不同数据类型数据使用同一个算法（确实是多了代码））  
函数模板使参数列表的数据类型可自动适配（功能和函数重载交叉）。

### 默认参数

默认参数定义在函数原型，在对应参数在参数列表中进行赋值，并且默认参数必须**从右往左**进行，即默认参数的右边的参数必须都是默认参数，默认参数后，在函数调用时可对默认的参数不提供实参，同时实参必须按**从左往右**的顺序依次赋给相应的形参，而不能跳过任何参数。

+ 在调用时省略的参数被称为*缺省参数*。
+ 默认参数不能是局部变量
+ 默认参数可以是表达式，要求其类型可转换为形参所需的类型，比如函数（声明时解析，调用时求值）
+ 多次声明：每个形参只能设定一个默认参数，
	+ 允许这种：
		```cpp
		type f(type a, type b, type c = 0);
		type f(type a, type b = 0, type c);
		//实际上等于type f(type a, type b = 0, type c = 0);
		type f(type a = 0, type b, type c);
		//实际上等于type f(type a = 0, type b = 0, type c = 0);
		```

### 函数重载

+ 重载：概念与多态一致；函数重载和函数多态是一回事，通常用函数重载。

>默认参数：不同数目的参数调用同一个函数  
>函数重载：使用不同的参数列表完成同样的工作——用于函数执行相同的任务，但使用不同形式的数据时。

+ 原理：名称修饰（name decoration）或名称矫正（name mangling）：C++跟踪每一个重载函数，编译器根据每个函数的形参进行加密。
	+ 函数的参数列表（函数特征标）：参数的数目、类型、顺序同，则特征标同；
		>重载指的是特征标不包含返回类型

	名称无关紧要——C++允许同名函数——C++对特征标不同的同名函数进行重载。

+ 调用函数时如果发现所有的同名函数都有参数列表出现类型不匹配的情况：C会实行强制转换，但是C++会报错

+ 引用性：C++函数将类型引用和类型本身视为同一特征标。
+ cv限定：

### 函数模板

[另一个笔记](./Generic.md#函数模板)

## 匹配决议

+ 匹配等级：
	1. 精确匹配：
		+ 实参和形参类型相同
		+ 实参从数组类型或函数类型转换成对应的指针类型
		+ 实参添删**顶层**const

	2. 通过const转换实现的匹配
	3. 通过类型提升实现的匹配
	4. 通过算术类型转换或指针转换实现的匹配通过类类型转换实现的匹配

## 函数指针、`std::function`和Lambda表达式

+ 函数指针：
	+ 声明：`RetType (* pFunc)(params_list);`
	+ 赋值：`pFunc pf = function_name;`/`pFunc pf = &function_name;`
	+ 调用：`pf(args);`/`(*pf)(args);`

+ lambda表达式：就是一个表达式
+ 闭包enclosure：lambda创建的运行时对象
+ 闭包类：闭包从中实例化，每个lambda都会使编译器生成唯一的闭包类，lambda中的语句成为其闭包类的成员函数中的可执行指令

这里闭包类是编译器概念，闭包是运行时概念。

+ `std::function`类型的变量可存储闭包，还有性能问题（较于直接使用`auto`来声明），因为auto是直接在栈上生成闭包类实例（闭包），而`std::function`可能会有堆空间的申请，另外整个过程还有虚函数的调用（我猜是在`std::function`实例的析构中）

+ 避免使用默认捕获模式：
	+ 默认按引用捕获：可能出现悬空引用的问题
	+ 默认按值捕获：如果捕获的值是指针，就会出现悬空指针（和悬空引用一样危险），且这个不会因为完全使用智能指针而消除，比如在类方法中，默认按值捕获只能捕获**局部非静态变量**，注意，`this`也是局部非静态变量呀，而其他的数据成员不是，这一方面有一个错觉，就是闭包里可以使用数据成员，但是这是因为捕获了this，另一个方面就是就是上面说的，我们捕获了一个裸指针呀，而且这个裸指针很可能被一个智能指针管理，你怎么保证他们有序销毁？

