泛型编程技术是为了实现代码的可重用性，对于某个算法，不必关系具体使用的类型，那么这里讲的一些技术就是为了实现这个目的。
>在C中也有类似的技术，`typedef`，术语一种类型别名，但是这可不足够的代码重用，仍然是只能服务一直类型

# 模板

提供参数化(parameterized)类型，让类型名作为参数传递给接收方来建立类或函数。其原理是编译器根据代码中的信息，对针对模板对某种类型生成代码，然后在编译，以这样的方式实现代码的重用。有些教材将代码中的模板代码叫做"声明"，将实例化后或者具象化后的代码叫做"定义"。

另外的话，一般情况下是要区分模板函数和函数模板、模板类和类模板的，这篇文章不严格区分。

+ 建立模板
	```cpp
	template<class TypeName> ...
	template<typename TypeName> ...
	```
	这里的`TypeName`即传进来的类型的名字，术语为*泛型标识符*

	+ 两种写法，C++98提供后面的语法，为了向后兼容，前者语法仍然可以使用

+ 非类型non-type参数/表达式expression参数：指定特殊的类型而不是泛型作为类型参数，从传递类型变成传递某个常量，该值只能是整型、枚举、引用或者指针。
	```cpp
	template<typename T, int N>
	```

	这里的`N`即接受一个`int`型的参数，在模板中，该标识符`N`即接受的`int`类型的值的别称。  
	模板内的代码不能修改其值，也不能对其取址。  
	在实例化模板时，用作非类型参数的值必须是常量表达式。

+ 默认类型模板参数：
	+ 为类型参数提供默认值，类模板可以，函数模板不可以。
	+ 为非类型参数提供默认值，类模板和函数模板都可以。

+ 使用模板：
	+ 模板内代码：在类型参数控制的区域可以把泛型标识符作为内置类型使用
	+ 调用模板代码：通过实例化以确定类型按照模板代码生成具体的代码

+ 实例化(instantiation)：让编译器通过模板代码针对具体类型生成对应代码
	+ 隐式实例化(implicit instantiaion)：在使用模板时，编译器自动为其生成对应类型的代码
	+ 显式实例化(explicit instantiaion)：在代码中手动命令编译器生成对应类型代码
		```cpp
		template RetType funcName<type...>(type par1, ...) {}
		template class ClassName<type...>;
		```

+ 具体化(specialization)：不使用模板生成定义，而是专门为特定类型进行定义
	```cpp
	template <> RetType funcName(type par1, ...) { ... }
	template <> class ClassName<...> {};
	```

	+ 部分具体化：TODO
 

## 函数模板

来个经典的
```cpp
template<typename T>
void swap(T& a, T& b) {
	T t = a; a = b; b = t;
}
{
	int a = 1, b = 2;
	swap(a, b);       // 隐式实例化
	swap<int>(a, b);  // 显式实例化
}
```

+ 后置返回类型(trailing return type)：
	一般情况下，如果返回类型和参数类型有关，没问题的`template<typename T> T add(T a, T b);`，但是如果我希望生成类型这样的`double add(int a, double b);`呢？注意这里的`int`和`double`也能调换，实际上，这样的函数没有问题，发生了**类型提升**嘛，这些可以自动实现，但是在模板函数中，代码使用哪个类型参数呢？比如`template<typename T1, typename T2> ? add(T1 a, T2 b);`，这时可以引入`decltype`关键字，通过表达式自动生成正确的类型，即`decltype(a + b)`，那么新的问题，这时就用到了形参的名称，但是在返回值的位置还不知道形参的名字，这时就可以使用这样的语法`template<typename T1, typename T2> auto add(T1 a, T2 b) -> decltype(a + b);`

## 类模板

+ 定义类模板：
	```cpp
	template<typename T>
	class ClassName {
		...
	};
	```

	+ 模板类方法定义：
		```cpp
		template<typename T>
		RetType ClassName<T>::mothedName(...) {...}
		```

+ 使用模板类：`ClassName<type> instanceName;`

+ 特例化成员，上面讨论过模板实例化和具体化，其中有部分具体化，这里的具体化是指类型参数，如果我只想具体化某种类型下模板类的某个方法呢？TODO

### 友元

+ 非模板友元，模板类中的常规友元是所有模板类的友元
+ 模板友元：
+ 约束(bound)模板友元：TODO
+ 非约束(unbound)模板友元：TODO

### CRTP

## MISC

+ 实例化控制：模板只有在使用时才会进行实例化，所以相同的模板实例可能出现多个代码文件中，这是额外的开销

	+ 实例化声明：`extern template declaration;`
	+ 实例化定义：`template declaration;`

+ variadic template可变参数模板：接受可变数目的类型参数的函数模板或类模板，TODO

+ 模板类声明和实现的分离，对于一般的类，我们都是声明和定义分离的，这里可以加快编译速度。但是对于模板类来说，声明和定义的分离是不行的。如果一定要实现呢？就是使用模板实例化。

+ 类型别名：
	+ C：`typedef`
	+ C++11：`using`
		+ 类模板别名

	```cpp
	template<typename T> using twin = paair<T, T>
	twin<string> authors;  // authors是一个pair<string. string>

	template<typename T> using partNo = pair<T, unsigned>
	partNo<string> books;  // books是一个pair<string, unsigned>
	```

	使用`typedef`依然可以实现，但是更复杂。



## 类型推导问题

我们以下面的代码为例
```cpp
template<typename T>
void foo(ParamType param);  // 这里的ParamType是一个和T有关的代码
```

+ 如果ParamType是引用或者指针，则实参类型中的cv类型限定会被保留进T中，而实参的引用性会被忽略
+ 引用折叠：如果ParamType是**通用引用**(右值引用)，此时左值的实参会被认为是引用，右值的实参会被认为是右值引用
+ 如果ParamType没有引用，则实参的引用性会被直接忽略
	+ 实参的cv类型限定也会被忽略
		>为什么要这样？因为引用性被忽略了，形参肯定是实参的拷贝，此时即使没有cv限定，实参也是安全的。

		+ 在讨论这样的场景，实参类型是`const char* const`，则形参是`const char*`，所以形参是可以变化的，但是依然不能通过形参修改本来字符串，依然安全。

+ 数组实参，一般情况下，数组可以退化成指针，如果直接把数组名作为参数，则参数类型被推导为`T[]`，在C语言这个就会退化成指针，但是如果形参传入一个数组名的引用呢？它是为了引用传递进去的数组实参，此时数组的长度信息就应该拿到，所以需要模板添加非类型参数，就像下面代码
	```cpp
	template<typename T, std::size_t N>
	constexpr std::size_t arraySize(T (&)[N]) noexcept {  // 形参没有名字，我们只关注数组长度
		return N;
	}
	```

上面是模板类型推导的场景，下面引用关键字`auto`  
实际上绝大部分规则是一致的，但是在下面的场景

```cpp
auto x1 = 42;      // C++98
auto x2(42);       // C++98
auto x3 = { 42 };  // C++11
auto x4{ 42 };     // C++11
```

+ 在这样的场景下，前两者会被推导成`int`，而后两者会被推导成`std::initializer_list<int>`
+ 但是同样的情况在模板中，是可以被正确推导的，如果需要转换成`std::initializer_list`，反而需要在函数参数列表中使用`std::initializer_list<T>`

+ 在C++14中运行`auto`用于函数返回值或者Lambda函数的形参，这是使用的规则就是**模板类型推导**，同样不会自动向`std::initializer_list<T>`推导。

我们在引入`decltype`关键字。


首先介绍下
+ 对于`decltype(expression) var;`这里参数可以是数据类型或表达式
	+ 如果expr是一个没有用括号括起来的标识符，则var的类型与标识符类型相同，包括cv限定，但忽略引用性
	+ 如果expr是一个函数调用，则var的类型与函数返回类型相同
	+ 如果expr是一个左值（你会疑惑，上面不说了标识符了，但是还有什么场景标识符不是左值？这里实际指的是用括号括起来的标识符，这个肯定也是左值），则在上面的基础上，var的类型还会包含expr的引用。
	+ 其他
 
主要的问题发生在这样的情况
```cpp
template<typename Container, typename Index>
auto authAndAccess(Container& c, Index i) ->decltype(c[i]) {
	authenticateUser();
	return c[i];
}
```

我们希望传会一个传进数组的某个位置的引用

+ 在C++11中，`auto`支持单一语句的lambda表达式的返回类型，而在C++14扩展到允许自动推导所有lambda表达式和函数，即使它们内含多条语句  
	所以上面代码可以直接去掉`decltype`部分，直接使用`auto`的类型推导，但是`auto`的类型推导和`decltype`不一样，BUG  
	总之C++14有了这么个东西
	```cpp
	template<typename Container, typename Index>
	decltype(auto)
	authAndAccess(Container& c, Index i) {
		authenticateUser();
		return c[i];
	}
	```
	神奇不，这里`auto`表示这里要类型推导，而`decltype`又表示按照`decltype`的方式进行推导。

## 关键字typeid和Boost.TypeIndex

typeid [ref](https://en.cppreference.com/w/cpp/language/typeid)：该关键字会返回`std::type_info`类型对象，这个对象有方法`name()`返回一个字符串表示表达式类型，但结果并不一直可信


## 模板元编程

variable template (C++14) [cpp ref ](https://en.cppreference.com/w/cpp/language/variable_template)

+ 取模板类型参数创建另一种类型，可能需要type traits类型特性，主要在头文件`<type_traits>`中，比如
	```cpp
	std::remove_const<T>::type          //C++11: const T → T 
	std::remove_const_t<T>              //C++14 等价形式
	
	std::remove_reference<T>::type      //C++11: T&/T&& → T 
	std::remove_reference_t<T>          //C++14 等价形式
	
	std::add_lvalue_reference<T>::type  //C++11: T → T& 
	std::add_lvalue_reference_t<T>      //C++14 等价形式
	```
	指的一题的是，C++11版本使用的是`typedef`相关的技术，而C++14的接口才是类型别名`using`的相关技术

	实际上可以
	```cpp
	template <class T> 
	using remove_const_t = typename remove_const<T>::type;
	
	template <class T> 
	using remove_reference_t = typename remove_reference<T>::type;
	
	template <class T> 
	using add_lvalue_reference_t =
		typename add_lvalue_reference<T>::type; 
	```

	这里的关键字`typename`就是`typedef`较于`using`的一些问题。
