+ C++程序运行时的内存分配：
	+ static静态内存：
	+ stack栈内存：
	+ heap堆内存：dynamically allocate动态存储

## new&delete(C++98)

1. `new`：分配空间、构造对象
   1. 基本类型：`type *p = new type;`           ：返回对象地址
   2. 数组类型：`type *p = new type[num];`：返回对象数组第一个元素地址
      + 长度可以取0，返回的是一个和其他`new`运算符返回一定不同的地址，可作为尾后指针使用
   + 如果堆内存空间不足：
     + 单个元素：引用异常`std::bad_alloc`
     + 数组元素：引用异常`std::bad_array_new_length`  
     定位new为new运算符传入参数使之不返回异常而返回空指针`new (nothrow) ...`
   + 构造`const`类型：`new const ...`

2. `delete`：销毁对象、释放内存，参数是指针指向空间的第一个元素，空间回收但指针变量还在，成为dangling pointer空悬指针
   1. 基本类型：`delete p;`
   2. 数组类型：`delete[] p;`
      > 逆序销毁对象
   
      + new和delete维护数组是扩展语法，智能指针不能原生的支持
   
        1. `unique_ptr`支持：  
           构造`unique_ptr<type[]> p(new type[num])`  
           使用：支持`[]`运算符
        2. `shared_ptr`想支持需自定义deleter：  
           使用：不支持`[]`运算符，需要通过`*(p.get() + i)`使用
           > 因为其默认调用的是`delete`而不是`delete[]`

两运算符**必须**配套使用，不能释放错误（对普通指针释放），不能不释放（内存泄漏），不能重复释放：这些行为都是未被定义
>注意delete一个空指针是没问题的，因为delete会先检测指针

+ 初始化：
  + 内置类型在类型名后面加上初始值，并将其用小括号括起来。
  + 复合类型在类型名后面加上列表值，并将其用大括号括起来。
  1. 括号为空：值初始化，值为类型的0（内置类型的0、类类型默认构造函数）
  2. 没有括号：默认初始化，内置类型未知、类类型默认构造函数

### 定位new
> placement定位

> 诸如上面的nothrow用法就是一种定位new运算符，本质是向new运算符传递一个参数

+ 语法：place_address必须是一个指针
  ```c++
  new (place_address) type;
  new (place_address) type (initializers);
  new (place_address) type [size];
  new (place_address) type [size] { braced initializer list }
  ```
+ 销毁对象而不释放空间：`dvxd -> ~ClassName();`

### 替换函数

+ new替换函数：
  在全局名称空间中，有如下函数原型，使用运算符重载语法。
  ```cpp
  void * operator new(std::size_t);
  void * operator new[](std::size_t);  //分配函数(alloction function)
  void operator delete(void *);
  void operator delete[](void *);  //释放函数(deallocation function)
  ```
  `std::size_t`是一个`typedef`，在使用new和delete时会进行转换

### 重载运算符

> 如果某些程序对内存分配有特殊的需求，需要自定义内存分配的细节，C++允许重载`new`和`delete`运算符
+ 工作机理：
  + **`new`**：
    1. new表达式调用名为`operator new`或`operator new []`的标准库函数，该函数分配空间
    2. 编译器运行相应的构造函数以构造对象并传入初始值
    3. 对象被分配空间并构造完成，返回一个指向该对对象的指针
  + **`delete`**：
    1. 对参数所指的对象或数组中的元素执行析构函数
    2. 编译器调用名为`operator delete`或`operator delete []`的标准库函数释放内存空间

+ 可在**全局**或者**类成员**重载运算符，编译器会优先检测类成员、在检测全局自定义，最后使用标准库定义

  + 重载为类成员：隐式静态，无需显示的声明`static`

+ 可重载的接口：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/动态内存接口.jpg" style="zoom:60%;" />

  + `nothrow_t`是定义在new头文件中的一个无成员的struct，并定义了一个名为**`nothrow`**的const对象，用户可以通过这个对象请求非抛出版本，重载这部分运算符时也**必须**使用`noexcept`异常说明符

+ 关于`<cstdlib>`中的`malloc`和`free`

  ```c++
  void *operator new(size_t size) {
      if (void *mem = malloc(size))
          return mem;
      else 
          throw bad_alloc()
  }
  void operator delete(void *mem) noexcept { free(mem); }
  ```

## 智能指针 C++11

> C++11的SL提供几种smart pointer智能指针来更容易、安全的管理动态对象

+ 头文件`<memory>`，名称空间`std`

  + `auto_ptr`：C++98使用，在C++11弃用

  1. `shared_ptr`：允许多个指针指向同一个对象，并通过引用计数自动管理其内存的释放

     `weak_ptr`：伴随类、弱引用，指向`shared_ptr`管理的对象

  2. `unique_ptr`：相对`shared_ptr`、独占所指向的对象

  ​                 <img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/智能指针操作.jpg" style="zoom:80%;" />

  智能指针服务于动态内存的，不要用其管理普通变量，因为其默认delete销毁变量

+ 相关规范：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/智能指针规范.jpg" style="zoom: 80%;" />

+ > `shared_ptr`默认调用`delete`释放空间，`delete`会调用对象的析构函数，但是并不是所有的类都有析构函数

  哑类：未定义析构函数的类，其作用是为了和C互通

  解决方法是定义deleter删除器并在构造智能指针指针时传入，删除器是一个函数，参数接受对应类型的指针变量

  + `shared_ptr<type> p(&object, deleter)`
  + 

### shared_ptr

> Reference Count引用计数：相关联的计数器，自动管理，为0销毁对应对象

+ 语法：`shared_ptr<type> p(new type(val...))`/`make_shared<type>(val...)`

  + 智能指针的构造函数是explicit的，不能隐式转换，必须显式初始化

  
  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/shared_ptr构造.jpg)


+ 注意：
  1. 不用混用普通指针和智能指针

#### weak_ptr

+ `weak_ptr`：不控制所指向对象生存期的智能指针，指向由`shared_ptr`管理的对象，**不改变**`shared_ptr`的引用计数

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/weak_ptr操作.jpg)

### unique_ptr

+ `unique_ptr`：拥有所指对象，没有类似`make_shared`的函数，必须指针初始化，不能赋值和拷贝

  + 转移：`p2.reset(p3.release());`（release并没有释放空间）

+ 操作：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/unique_ptr构造.jpg" style="zoom:80%;" />

+ 管理数组：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/unique_ptr指向数组的.jpg" style="zoom:80%;" />

  + 需要显式的调用函数进行销毁：`p.release()`

  + 需要自定义deleter：

    ```c++
    unique_ptr<指针的类型, decltype(对应类型的deleter)*> p(new ..., deleter函数名);  // *是必须的
    ```


## allocator类 C++11

> `new`运算符申请空间和构造对象是一同进行的，不能分开，即这样的方式不适用于没有默认构造函数的类型

头文件`<mempry>`，名称空间`std`

+ 说明：提供*类型感知*的内存分配的方法，是一种模板

 <img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/allocator类.jpg" style="zoom:80%;" />

 <img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/allocator伴随算法.jpg" style="zoom:80%;" />

+ heap堆：内存管理中指动态分配内存的区域，由C中的malloc和free操作。
  + free store自由存储区：特指使用new和delete来分配和释放内存的区域，是heap的子集。
+ stack栈：内存管理中指函数调用过程中产生的本地变量和调用数据的区域
+ RAII：资源管理方式，依托栈和析构函数

---

+ 对于POD类型变量，使用stack管理
+ 对于非POD类型变量，如果使用stack管理，自动调用构造和析构函数

---
## 智能指针的实现

+ new的过程：

  ```c++
  new ClassName(...);
  {
      void* t = operator new(sizeof(ClassName));  // 先分配内存
      try {
          ClassName* p = static_cast<ClassName*>(t);
          p->ClassName(...);  // 然后构造
          return ptr;
      } catch(...) {
          operator delete(p);
          throw;
      }
  }
  
  RAII
  if (p != nullptr) {  // 对于空指针依然能正确delete（它根本就不会被delete）
      p->~ClassName();
      operator delete(p);
  }
  ```

+ 智能指针：

  ```c++
  class shape_wrapper {
  public:
      explicit shape_wa
  }
  ```

  





+ 智能指针

  ```c++
  #include <iostream>
  
  template<typename T>
  class Ptr {
  public:
      explicit Ptr(T* ptr = nullptr) : ptr_(ptr) {}
      ~Ptr() {
          delete ptr_;
      }
      T* get() const { return ptr_; }
      T& operator*() const { return *ptr_; }
      T* operator->() const { return ptr_; }
      bool operator()() const { return ptr_; }
  private:
      T* ptr_;
  };
  
  class Class {
  public:
      void say() { std::cout << "Hello"; }
  };
  
  int main() {
      Ptr p(new Class());
      
      p->say();  // p.operator->()->say();
      
      return 0;
  }
  ```

  
+ 关于赋值函数中`if (this != &rhs)`的强异常安全性：赋值分为拷贝构造和交换两步

  ```c++
	Ptr(Ptr& other) {
		ptr_ = other.release();
	}
	T* release() {
		T* ptr = ptr_;
		ptr_ = nullptr;
		return ptr;
	}
	Ptr& operator=(Ptr& rhs) {
		Ptr(rhs).swap(*this);
		return *this;
	}
	void swap(Ptr& rhs) {
		using std::swap;
		swap(ptr_, rhs.ptr_);
	}
  ```

  注意这里的赋值运算符，是先通过拷贝构造函数构造一个新的对象，然后将这个对象和本对象进行交换，这样如果在构造这个对象是就出错，this不会受损

+ C++17废除的auto——ptr是直接将指针进行“移动”（转移所有权）

  ```c++
      Ptr(Ptr&& other) {  //参数把引用变成移动
          ptr_ = other.release();
      }
      Ptr& operator=(Ptr rhs) {  // 参数从引用变成普
          Ptr(rhs).swap(*this);
          return *this;
      }
  ```

  C++如果定义了移动构造而没有定义拷贝构造，则默认拷贝构造是delete的，此时该智能指针只能移动拷贝，赋值也只能赋值move后的，
+ RTTI是运行截断类型识别(Runtime Type Identificaton)的简称，旨在程序在运行阶段确定对象的类型提供一种标准方式。

  + 用途：基类指针可以指向派生类对象地址，如何确定基类指针指向对象的类型——RTTI只用于包含虚函数的类层次结构。

  + 原理：C++有三个支持RTTI的元素

    1. 如果可能的话，`dynamic_cast`运算符将使用一个指向基类的指针来生成一个指向派生类的指针；否则，该运算符返回0——空指针。

       ```cpp
       ClassName * p = dynamic_cast<ClassName *>(dvxdName);
       如果可以安全转换，运算符返回对象的地址，否则返回空指针。
       ```

       也可以用于引用，但是没有”空引用“，出现错误则请求不正确会引发bad_cast异常

    2. `typeid`运算符返回一个指出对象的类型的值——可以确定两个对象是否为同一类型

       `typeid(参数);` 参数接受两种：类名和结果为对象的表达式

       返回一个对`type_info`（头文件`<typeinfo>`旧为`<typeinfo.h>`定义的一个类）对象的引用，

       它重载了`==`和`!=`运算符可以实现两个返回值的比较

       它定义了`name()`的成员来返回一个随实现而异的字符串

    3. `type_info`（头文件`typeinfo`（以前为`typeinfo.h`）中的一个类）结构存储了有关特定类型的信息

       typeid运算符返回一个对type_info对象的引用











