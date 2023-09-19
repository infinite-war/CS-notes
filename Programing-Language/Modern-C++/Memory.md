## inline
[ref](https://en.cppreference.com/w/cpp/language/inline)

## const
[ref: cv qualifier](https://en.cppreference.com/w/cpp/language/cv)

+ const类并不是并发安全的，因为内部可能有成员使用`mutable`
+ 螺旋修饰规则：
	+ [first](https://c-faq.com/decl/spiral.anderson.html)
	+ [叔叔](https://zclll.com/index.php/cpp/182.html)


## 存储类别
[ref: storage class specifiers](https://en.cppreference.com/w/cpp/language/storage_duration)

| 存储类别描述       | storage duration | scope | linkage | 如何声明      |
| ------------------ | ---------------- | ----- | ------- | ------------- |
|                    |                  | file  | 外部    | 默认          |
|                    |                  | 块    |         | 函数内        |
|                    |                  | file  | 内部    | `static`      |
| 定义在其他翻译单元 |                  |       | 外部    | `extern` 声明 |

### 存储持续性
描述了数据保存在内存中的时间长度

#### 自动存储持续性
在程序开始执行所属的函数或代码块时被创建，执行完后释放

1. 自动变量：（默认情况）函数中声明的函数参数和变量，存储持续性为自动，作用域为局部，没有链接性。
	+ 嵌套代码块不同层次代码块中的同名变量会：内层hide外层
	+ 寄存器变量：关键字`register`，向编译器**申请**该变量使用CPU寄存器存储自动变量，旨在提供访问变量速度
		>register关键在在C++11中失去作用，只是显示的指出变量是自动变量

#### 静态存储持续性
在整个程序执行期间都存在的存储方式

2. 静态变量：
	1. 外部变量/全局变量外部链接性（可在其他文件访问）：必须在代码块外声明。
	2. 内部链接性（只能在当前文件中访问）：必须在代码块外声明，并使用`static`限定符。
	3. 无链接性（只能在当前函数或代码块中访问）：必须在代码块内声明，并使用`static`限定符。


3. 外部变量/全局变量（相对于局部的自动变量）：链接性为外部，存储持续性为静态，作用域为整个翻译单元。
	+ 引用声明：关键字`extern`，且不进行初始化（如果使用关键字依然初始化则exrern失效）
	+ 多文件，只需一个定义，其他地方使用引用声明
	+ 引用的变量遵循自动变量的同名下处理规则
	+ 在函数中使用该关键字强调函数使用外部变量

4. 静态存储持续性、内部链接性、作用域整个翻译单元，关键字`static`
	+ 不在代码块内声明的变量天然外部链接，使用关键字限定为内部
	+ 在多文件程序中，此种变量只能在所属的翻译单元内使用

	**不**会与其他翻译单元的全局变量**冲突**，但会**覆盖**

5. 静态局部变量：静态存储持续性、无链接性，作用域局部，关键字`static`用于局部变量
	+ 局部变量存储持续性为自动，使用关键字限定为静态
	+ 静态局部变量在程序执行期间一直存在，但名称只在该作用域可见
	+ 再生：在其他代码块使用static再次声明同名变量，则使用同一块地址
	+ 初始化：初始化语句只在申请空间时执行一次

#### 动态存储持续性
由new和delete运算符管理的内存池

#### 线程存储持续性

### 作用域
描述了名称在翻译单元的可见范围

+ 全局（文件作用域）
+ 局部（块作用域）

### 链接性
描述了名称在不同单元间如何共享

+ 函数链接性：
+ 语言链接性：[ref](https://en.cppreference.com/w/cpp/language/language_linkage)

## 名称空间
>1. 实体：变量、函数、结构、枚举、类以及类和结构的成员。
>2. 名称：实体的标识符。

+ 传统的C++名称空间：
	1. 声明区域(declaration region)：可以进行声明的区域
	2. 潜在作用域(potential scope)：从声明点开始，到其声明区域结尾。  
		作用域(scope)：数据对的对程序的可见区域。

		这里潜在作用域较于普通的作用域是区别是什么？比如同名变量的隐藏

	C++关于局部变量和全局变量的规则定义了一种名称空间层次、不同声明区域声明名称相互独立。

+ 现代的C++名称空间：定义并命名一个声明空间——名称空间：提供声明名声的区域，不同区域的同名名称不冲突，运行其他部分使用该名称空间的对象。

+ 名称空间的分类：
	+ 全局名称空间：文件级声明区域，所有名称默认的作用域
	+ 自定义名称空间：
		+ 类作用域。

+ 定义：
	```cpp
	namespace 名称空间名 {
		该名称空间内的实体
	};
	```

	+ 名称空间内的声明和定义规则同全局的相同
	+ 名称空间可定义嵌套，但不能定义于代码块（默认名称空间为链接性外部，块内名称不能是外链接性）
	+ 名称空间是open的

+ 访问：
	1. 作用域解析运算符`::`，格式：`名称空间名::实体标识符`，作为总体使用
		>未限定的名称(unquealified name)：未被装饰的名称  
		>限定的名称(qualified name)：包含名称空间的名称

	2. `using`声明：格式：`using 名称空间名::实体名;` ：将实体名暴露在当前的名称空间中，即可使用未被限定的名称使用
		+ 冲突和覆盖：编译报错，无法导入

	3. `using`编译指令：格式：`using namespace 名称空间名;`：将名称空间内的所有实体名暴露在当前名称空间中
		+ 冲突和覆盖：单独使用::强调

+ 其他特性：
	+ 定义可嵌套，对应的访问是嵌套使用作用域解析运算符，在内嵌的名称空间也可以使用using，而其作用可在内外层传递
	+ 为名称空间创建别名：`namespaces 新名 = 旧名;`
	+ 匿名名称空间
	+ C++标准库放在名称空间std中

# RAII

+ 动态内存Ref：[Dynamic memory management](https://en.cppreference.com/w/cpp/memory)
	+ raw ptr: new&delete
		+ [new](https://en.cppreference.com/w/cpp/keyword/new)和[delete](https://en.cppreference.com/w/cpp/keyword/delete)：正如ref所说，这两个关键字既是expression又是function

	+ smart pointers：
		+ [unique_ptr](https://en.cppreference.com/w/cpp/memory/unique_ptr)
		+ [shared_ptr](https://en.cppreference.com/w/cpp/memory/shared_ptr)
		+ [weak_ptr](https://en.cppreference.com/w/cpp/memory/weak_ptr) 

+ 智能指针的简单实现：
	+ `auto_ptr`（C++17废除），因为拷贝语义实际运行的是移动
	+ `unique_ptr`：只能进行移动，禁用拷贝
	+ `shared_ptr`：

+ shared_ptr的Control Block：
	>热知识，shared_ptr的大小是裸指针的两倍。

	+ shared_ptr的大小是裸指针的两倍，其中一个相当于裸指针，另外一个指针指向Control Block
	+ Control Block即起到引用计数的功能，关于计数的变换使用**原子变量**（所以这部分是多线程安全的，但是shared_ptr整体不是线程安全的）
	+ 还有关于weak_ptr的相关信息，即这块内存表示的裸指针有多少weak_ptr也在维护，如果有weak_ptr，即使shared_ptr都销毁了也应该保留。
	+ 性能相关，这里首先堆内存的使用有一定损耗，另外控制块内部有虚函数的调用（不过通常只有析构这一次），也有对应的损耗。

+ unique_ptr与所有权语义exclusive ownership

+ `unique_ptr`的自定义删除器：
	>热知识，unique_ptr的大小在不定义自定义删除器时时空消耗是和裸指针一样的

	但是unique_ptr并没有Control Block，所以它的删除器相关代码需要放置在实例内部，如果其状态过多，可能需要申请堆内存，届时会有性能损耗

+ Effective Modern C++ Item21，使用make系标准函数而不是使用裸指针去构造只能指针。
	+ 一般情况下标准函数决定可以满足需求了，除了自定义删除器和关于初始化括号的歧义场景
	+ 结合shared_ptr的控制块，如果不小心多次使用裸指针去构造多个shared_ptr，这些控制块可不是同一个。
		+ 那如果我直接将`new`语句作为shared_ptr的构造参数呢？   
			在函数调用时可能出错，因为函数调用要先构造实参，而这个过程是不保序的，而上面的构造过程分成了两个部分，`new`和构造，这两步未必是连续的，如果中间的步骤异常了，则最开始new的空间就泄露了。
	+ 需要`push_back(this)`场景，如果你想这么做，比如将你的类从`std::enable_shared_from_this`去继承，该类有成员函数`shared_from_this()`来代替`this`
	+ 还是结合控制块，make可以直接申请类型大小和控制块大小的堆空间，然后再分别构造，而使用裸指针，就说明这里肯定是分两步了。

+ weak_ptr使用场景：
	+ 工厂设计模式中，如果是根据ID构建，且这个构建昂贵且频繁，就可以把对应的实例缓存起来，但是工厂方法通常使用unique_ptr做返回值，这可没法缓存。
	+ 观察者设计模式，subject需要持有observer的指针，但是它并不关心observer的生成周期。
	+ 循环引用

# 移动语义和完美转发

>移动语义（move semantics）和完美转发（perfect forwarding）：

+ 移动语义使编译器有可能用廉价的移动操作来代替昂贵的拷贝操作。
+ 完美转发使接收任意数量实参的函数模板成为可能，它可以将实参转发到其他的函数，使目标函数接收到的实参与被传递给转发函数的实参保持一致。

右值引用是连接这两个截然不同的概念的胶合剂。它是使移动语义和完美转发变得可能的基础语言机制。

+ 通用引用/转发引用
	```cpp
	template<typename T>
	type foo(T&& t);
	```

	+ 类型参数中的`&&`中和`auto`后的`&&`中都是通用引用，因为这里有类型推导
		+ 但并不是所有类型推导场景都是通用引用，比如`std::vector<T>&`，这里的T就没有“歧义”的可能
		+ 那么多了一个const，`template<typename T>type foo(const T&& t);`，这都不是，这只是右值引用
		+ 而哪怕都符合，还可能不是，比如`std::vector`中的成员函数`push_back`，因为在调用`push_back`是，它的类型参数早就确定了。
  



+ `std::move`和`std::forward`：两者不移动也不转发任何东西，它们仅仅是在做cast转换，前者无条件的将其转换成右值，后者在特定情况下进行转换
	+ 这里做区分是因为，如果是普通的右值，就可以通过std::move无条件的转换成右值（因为他们在被传递进来后变成了左值），当转发通用引用时，通过forward将其有条件的转换成右值
	+ `... foo(const std::strin& s) { std::string s2(std::move(s)); ...}`：这里仍然是拷贝，因为std::move的返回值是通用引用，所以`std::move(s)`的类型是`const std::string&&`，哦吼？这个可不能匹配到移动构造，因为const不匹配。

	+ 移动语义可以用于函数返回局部数据对象么？不能，因为有返回值优化（return value optimization，RVO）的存在。
 

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