+ C++程序运行时内存分配：
	+ [Dynamic memory management](Dynamic memory management)
+ [new](https://en.cppreference.com/w/cpp/keyword/new)和[delete](https://en.cppreference.com/w/cpp/keyword/delete)：正如ref所说，这两个关键字既是expression又是function

## Smart pointers

+ [unique_ptr](https://en.cppreference.com/w/cpp/memory/unique_ptr)
+ [shared_ptr](https://en.cppreference.com/w/cpp/memory/shared_ptr)
	+ [weak_ptr](https://en.cppreference.com/w/cpp/memory/weak_ptr) 

## Allocators
>make ptr内部是new，new是




  
  


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











