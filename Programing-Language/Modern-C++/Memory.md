
## inline
[ref](https://en.cppreference.com/w/cpp/language/inline)

## const
[ref: cv qualifier](https://en.cppreference.com/w/cpp/language/cv)

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
	1. 声明区域(declaration region)：可以进行声明的区域。
	2. 潜在作用域(potential scope)：从声明点开始，到其声明区域结尾。  
		作用域(scope)                 ：数据对象对程序可见的区域

		>潜在作用域中并非全都是作用域，ege：同名变量隐藏

	C++关于局部变量和全局变量的规则定义了一种名称空间层次、不同声明区域声明名称相互独立。

+ 新的C++名称空间特性：定义并命名一个声明空间——名称空间：提供声明名称的区域，不同区域的同名名称不冲突，允许其他部分使用该名称空间的对象

+ 名称空间分类：
	+ 全局名称空间(global namespace)：文件级声明区域，所有名称默认的作用域
	+ 自定义名称空间：
		+ 类作用域

----

+ 定义：

  ```c++
  namespace 名称空间名 {
      该名称空间内的实体
  };
  ```

  + 名称空间内的声明和定义规则同全局的相同
  + 名称空间可定义嵌套，但不能定义于代码块（默认名称空间为链接性外部，块内名称不能是外链接性）
  + 名称空间是open的

+ 访问：

  1. 作用域解析运算符`::`格式：`名称空间名::实体标识符`，作为总体使用

     > 未限定的名称(unquealified name)：未被装饰的名称
     >
     > 限定的名称(qualified name)           ：包含名称空间的名称

  2. `using`声明：格式：`using 名称空间名::实体名;` ：将实体名暴露在当前的名称空间中，即可使用未被限定的名称使用

     + 冲突和覆盖：无法导入

  3. `using`编译指令：格式：`using namespace 名称空间名;`：将名称空间内的所有实体名暴露在当前名称空间中

     + 冲突和覆盖：单独使用::强调

+ 其他特性：
  + 定义可嵌套，对应的访问是嵌套使用作用域解析运算符，在内嵌的名称空间也可以使用using，而其作用可在内外层传递
  + 为名称空间创建别名：`namespaces 新名 = 旧名;`
  + 匿名名称空间
  + C++标准库放在名称空间std中


# 动态内存和RAII

[Dynamic memory management](https://en.cppreference.com/w/cpp/memory)

## raw ptr: new&delete

[new](https://en.cppreference.com/w/cpp/keyword/new)和[delete](https://en.cppreference.com/w/cpp/keyword/delete)：正如ref所说，这两个关键字既是expression又是function

## Smart pointers

+ [unique_ptr](https://en.cppreference.com/w/cpp/memory/unique_ptr)
+ [shared_ptr](https://en.cppreference.com/w/cpp/memory/shared_ptr)
	+ [weak_ptr](https://en.cppreference.com/w/cpp/memory/weak_ptr) 

## Allocator

## 智能指针的简单实现

+ `auto_ptr`（已经在C++17废除）
	```cpp
	template <typename T> class z_auto_ptr {
	public:
	  explicit z_auto_ptr(T *ptr = nullptr) : ptr_(ptr) {}
	  ~z_auto_ptr() { delete ptr_; }
	  T *get() const { return ptr_; }
	
	  T &operator*() const { return *ptr_; }
	  T *operator->() const { return ptr_; }
	  operator bool() const { return ptr_; }
	
	  z_auto_ptr(z_auto_ptr &other) { ptr_ = other.release(); } // 转移所有权
	  z_auto_ptr &operator=(z_auto_ptr &rhs) {
	    z_auto_ptr(rhs).swap(*this);
	    // 这里本质分成两步，首先拷贝构造，然后进行swap，如果拷贝构造失败抛出异常，则不会影响到this
	    return *this;
	  }
	  T *release() {
	    T *ptr = ptr_;
	    ptr_ = nullptr;
	    return ptr;
	  }
	  void swap(z_auto_ptr &rhs) {
	    using std::swap;
	    swap(ptr_, rhs.ptr_);
	  }
	
	private:
	  T *ptr_;
	};	
	
	```

+ `unique_ptr`：
	```cpp
		template <typename T> class z_unique_ptr {
	public:
	  explicit z_unique_ptr(T *ptr = nullptr) : ptr_(ptr) {}
	  ~z_unique_ptr() { delete ptr_; }
	  T *get() const { return ptr_; }
	
	  T &operator*() const { return *ptr_; }
	  T *operator->() const { return ptr_; }
	  operator bool() const { return ptr_; }
	
	  // template <typename U> z_unique_ptr(z_unique_ptr<U> &&other)
	  // 注意，上面并不是移动构造函数，拷贝构造不会默认删除
	  z_unique_ptr(z_unique_ptr &&other) { ptr_ = other.release(); }
	  // 提供移动构造函数而没有手动提供拷贝构造函数，则后者被自动禁用
	  z_unique_ptr &operator=(z_unique_ptr rhs) {
	    // 在传递参数时隐形调用移动构造函数
	    rhs.swap(*this);
	    return *this;
	  }
	
	  T *release() {
	    T *ptr = ptr_;
	    ptr_ = nullptr;
	    return ptr;
	  }
	  void swap(z_unique_ptr &rhs) {
	    using std::swap;
	    swap(ptr_, rhs.ptr_);
	  }
	
	private:
	  T *ptr_;
	};
	```

+ `shared_ptr`：
	```cpp
	class shared_counter {
	public:
	  shared_counter() : count_(1){};
	  void add_count() { ++count_; }
	  long reduce_count() { return --count_; }
	  long get_count() const { return count_; }
	
	private:
	  long count_;
	};
	
	template <typename T> class z_shared_ptr {
	  template <typename U> friend class z_shared_ptr;
	
	public:
	  explicit z_shared_ptr(T *ptr = nullptr) : ptr_(ptr) {
	    if (ptr) {
	      shared_counter_ = new shared_counter();
	    }
	  }
	  ~z_shared_ptr() {
	    if (ptr_ && !shared_counter_->reduce_count()) {
	      delete ptr_;
	      delete shared_counter_;
	    }
	  }
	  T *get() const { return ptr_; }
	
	  T &operator*() const { return *ptr_; }
	  T *operator->() const { return ptr_; }
	  operator bool() const { return ptr_; }
	
	  z_shared_ptr(const z_shared_ptr &other) {
	    ptr_ = other.ptr_;
	    if (ptr_) {
	      other.shared_counter_->add_count();
	      shared_counter_ = other.shared_counter_;
	    }
	  }
	  template <typename U> z_shared_ptr(const z_shared_ptr<U> &other) {
	    ptr_ = other.ptr_;
	    if (ptr_) {
	      other.shared_counter_->add_count();
	      shared_counter_ = other.shared_counter_;
	    }
	  }
	  template <typename U> z_shared_ptr(const z_shared_ptr<U> &&other) {
	    ptr_ = other.ptr_;
	    if (ptr_) {
	      shared_counter_ = other.shared_counter_;
	      other.ptr_ = nullptr;
	    }
	  }
	  z_shared_ptr &operator=(z_shared_ptr rhs) {
	    // 在传递参数时隐形调用移动构造函数
	    rhs.swap(*this);
	    return *this;
	  }
	
	  void swap(z_shared_ptr &rhs) {
	    using std::swap;
	    swap(ptr_, rhs.ptr_);
	    swap(shared_counter_, rhs.shared_counter_);
	  }
	
	  long use_count() const {
	    if (!shared_counter_)
	      return 0;
	
	    return shared_counter_->get_count();
	  }
	
	private:
	  T *ptr_{nullptr};
	  shared_counter *shared_counter_{nullptr};
	};
	```
