+ `const`并不是并发安全的，因为const实例中可能有`mutable`类型成员，所以在并发上下文中需要额外的东西。

+ 使用`nullptr`而不是`0`或者`NULL`，因为`0`除了可以表示空指针还表示整数，而`NULL`的具体含义和实现有关。  
	这不仅影响函数重载决议，还影响类型推导。
	+ 如果非得使用`0`或者`NULL`就要注意避免重载指针和整型

+ 断言：
	+ [assert](https://en.cppreference.com/w/cpp/language/aggregate_initialization)：运行期断言
	+ [static_assert](https://en.cppreference.com/w/cpp/language/static_assert)：编译器断言

+ run-time type identification, RTTI运行时类型识别

+ 螺旋修饰规则：
	+ [first](https://c-faq.com/decl/spiral.anderson.html)
	+ [叔叔](https://zclll.com/index.php/cpp/182.html)

+ [aggregate聚合](https://en.cppreference.com/w/cpp/language/aggregate_initialization)
	+ 聚合断言：[判断一个类型是否是断言](https://en.cppreference.com/w/cpp/types/is_aggregate)

+ [concepts](https://en.cppreference.com/w/cpp/language/constraints)

+ `auto`：auto可不仅仅是语法糖
	+ 这里
		```cpp
		std::unordered_map<std::string, int> m;
		for(const std::pair<std::string, int>& p : m) {}
		```
		这对吗？要知道`std::unordered_map`的key是`const`的，这和`p`的类型可不一样，而编译器会“贴心”的进行转换，即copy一下哈希表中的键值对做临时对象，然后p是这个临时对象的引用，这样就出现了语义错误，使用`auto`肯定不会有这样的错误。

	+ 那什么时候又不能用auto呢？
		```cpp
		std::vector<bool> vec;
		...
		auto flag = vec[i];  // 错误，不仅是错误，而是UB！
		bool flag = vec[i];  // 正确
		```

		因为如果使用auto，flag将不再是bool类型，这是因为`std::vector<bool>::operator[]`不会返回容器中元素的引用，而是返回`std::vector<bool>::reference`对象（它能模拟bool的一切行为（涉及诸多技术）），它的本质是和实现有关的，有一种实现是一种**代理类**，你并不知道这里会发生什么（通常代理类的对象的生命周期不会设计活过一条语句）

		所以这里一个通用的原则是，不可见的代理类不适用auto，这里的不可见指除了智能指针之外的。  
		但是这就意味着我们放弃`auto`么？解决方案是

	+ 显式类型初始器惯用法（the explicitly typed initialized idiom)
		```cpp
		auto flag = static_cast<bool>(vec[i]);
		```
		卧槽，那么我不直接放弃auto呢？因为不适用auto因隐式类型转换，没有证据证明你是故意的，但是这里这样可以表明你是故意的。

+ 初始化问题：
	+ 一般认为有三种初始化方式：
		1. `int x(0);`
		2. `int y = 1`;
		3. `int z = {2};`

		通常1和3也能使用`=`：`int x = (0);` and `int z = {2};`

		这里认为通常忽略`=`

	+ 场景1：
		```cpp
		ClassName a;      // 使用构造函数
		ClassName b = a;  // 不是赋值运算，而是调用拷贝构造函数
		b = a;            // 是赋值运算，调用拷贝赋值运算符
		```
	+ 场景2：非静态数据成员默认初始化，`{}`和`=`都是可以的，而`()`不行
	+ 场景3：对于不可拷贝对象的定义，`{}`和`()`都是可以的，而`=`不行
	+ 场景4：对于内置类型间隐式的变窄转换（narrowing conversion），`{}`是会检测并在编译报错的，而`()`和`=`不会
	+ 场景5（编译层），你看代码`ClassName c();`你说这究竟是对象默认构造还是函数声明？而`{}`肯定不会

	我们发现`{}`是最具有广泛意义的写法。

	那么它的问题呢？就是和`std::initializer_list`的纠葛，会有很多问题。

+ `constexpr`关键字：除了`const`常量的语义外，还有编译器可知的意思，所以一个最起码的差别就出现了，const是可以这样的
	```cpp
	int sz;
	...
	const auto sz_ = sz;  // 没有问题，这里仅仅表示sz_不在可变，而不能不需要它在编译器都知道，但是constexpr可不行。
	```

	+ 当`constexpr`修饰函数时，其实是相当自由的，如果某个函数调用可以在编译器确定，则在编译器计算， 否则依然可以调用。 

	再深入的说，constexpr是为了获得字面量，在C++14中，可不仅是内置类型才能是字面量，自定义类型（在构造函数前添加关键字）也可以做字面量。
	+ 如果将类的Set方法可以设置为constexpr么？一方面不行，因为constexpr也意味着const，而且Set方法的返回值是 `void`，void可不是一个字面量，但是这两个限制在C++14中被放开
		>意思是constexpr不意味着const？
		

+ Pimpl（pointer to implementation）惯用法
	+ 不完整类型
	+ 初学者错误，析构错误，是因为默认析构在使用static_assert查看是否是不完整类型，我们需要让类的函数知道这个类型，所以在.cpp中，不完成类型的完整定义要在其他函数的实现前，即使使用default，也应该放在.cpp 中


+ 移动语义（move semantics）和完美转发（perfect forwarding）：
	+ 移动语义使编译器有可能用廉价的移动操作来代替昂贵的拷贝操作。
	+ 完美转发使接收任意数量实参的函数模板成为可能，它可以将实参转发到其他的函数，使目标函数接收到的实参与被传递给转发函数的实参保持一致。

	右值引用是连接这两个截然不同的概念的胶合剂。它是使移动语义和完美转发变得可能的基础语言机制。



	下面开始


	```cpp
	void foo(ClassName&& c);  // 注意!这里的形参c是一个左值呦
	```


	+ std::move和std::forward不移动也不转发任何东西，他们仅仅是cast转换，前者无条件的将其转换成右值，forward在特定情况进行转换
	+ 通用引用（universal reference）

	+ std::move仅仅是转换成右值，所有这样的函数
		```cpp
		void foo(const std::string s) {
			std::string s2(std::move(s));
		}
		```
		仍然是一个拷贝调用，因为const属性一直被保留，此时由由于std::move的返回类型是通用引用，所以std::move(s) 的类型是`const std::sting&&`，呕吼，这个可不能给到移动构造，因为const不匹配，

+ 区分通用引用和右值引用，哦天哪，这两个并不是一回事，现在又有说法管他就转发引用

	+ 在类型参数的`&&`中和auto的&&中都是通用引用，因为这里有类型推导
		+ 但是也不一定，而且这种推导确实会发生两种情况，比如 `std::vector<T>&&`，这里的T就没有歧义
		+ 即使是多个const，也不是
		+ 即使都符合，也可能不是！，比如push_back，因为当push_back有的时候，这里的T已经确定了！


+ 这里做区分是因为，如果是普通的右值，就可以通过std::move无条件的转换成右值（因为他们在被传递进来后变成了左值），当转发通用引用时，通过forward将其有条件的转换成右值


+ 返回值优化（return value optimization，RVO）：即在函数中返回局部变量，则这个变量的构造位置就是函数的返回位置，这样省略一次拷贝，这时如果非得std::move就坏了，此时的返回类型和std::move(x)可不是同一个类型，没法rvo


+ effect提到一个奇技淫巧：
	```cpp
	std::multiset<std::string> names;       //全局数据结构
	
	template<typename T>                    //志记信息，将name添加到数据结构
	void logAndAdd(T&& name)
	{
	    auto now = std::chrono::system_clokc::now();
	    log(now, "logAndAdd");
	    names.emplace(std::forward<T>(name));
	}
	std::string nameFromIdx(int idx);   //返回idx对应的名字
	
	void logAndAdd(int idx)             //新的重载
	{
	    auto now = std::chrono::system_clock::now();
	    log(now, "logAndAdd");
	    names.emplace(nameFromIdx(idx));
	}
	```

	有大问题，对short，使用的是通用引用


	来看魔法
	```cpp
	template<typename T>
	void logAndAdd(T&& name)
	{
	    logAndAddImpl(
	        std::forward<T>(name),
	        std::is_integral<typename std::remove_reference<T>::type>()
	    );
	}
	```

	甚至这里不能用` std::is_integral<T>()`，因为tm`int&`不是interger

	那么具体的实现呢？

	tag dispatch,
	这是模板元编程的标准构建模块

	```cpp
	template<typename T>                            //非整型实参：添加到全局数据结构中
	void logAndAddImpl(T&& name, std::false_type)	//译者注：高亮std::false_type
	{
	    auto now = std::chrono::system_clock::now();
	    log(now, "logAndAdd");
	    names.emplace(std::forward<T>(name));
	}
	std::string nameFromIdx(int idx);           //与条款26一样，整型实参：查找名字并用它调用logAndAdd
	void logAndAddImpl(int idx, std::true_type) //译者注：高亮std::true_type
	{
	  logAndAdd(nameFromIdx(idx)); 
	}
	```


	但是这只能有两个分支呀

	`std::enable_if`可以给你提供一种强制编译器执行行为的方法


+ 引用折叠就发生在通用引用中，