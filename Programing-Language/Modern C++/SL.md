
# bind

通用函数适配器：版本C++11，头文件`<functional>`：接受可调用对象，生成新的可调用对象

+ 语法：`auto newCallable = bind(callable, arg_list)`

  + arg_list的各个参数包含形如`_n`的占位符，其中`n`为整数，表示哪些未知的参数没有调整
    + 如果非顺序，则可对应映射，相当于调换函数参数位置

  其中`callable`就是一个可调用对象，其有参数列表，在bind的参数列表中可为其的某些参数提供默认值（参数绑定），则可以通过新的可调用对象使用不同的参数列表来调用原可调用对象。

  ```c++
  //有 type f(type arg1, type arg2)
  auto f_ = bind(f, _1, arg2_val);
  //则可以这样使用 f_(arg1_val);  // 相当于f(arg1_val, arg2_val)
  ```

## ref&cref

> 解决bind中的参数绑定只能值绑定不能引用绑定的问题

头文件同`bind`

+ `ref(参数)`：返回一个包含给定引用的对象
+ `cref`：ref的const引用版本

# pair

 ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/pair.jpg)

## 函数对象

 ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/标准库函数对象.png)

## 类型转换

`<type_traits>`

 ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/标准类型转换模板及应用.png)

## utility

+ `move`
+ `forward`：通过显式模板实参返回显式实参类型的右值引用，用于转发


# tuple

> 将一些数据合成单一对象，但是不想麻烦定义一个新数据结构来表示，tuple很好用

可以有任意数量的成员，

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/tuple.png)

+ 定义和初始化：
  + tuple的构造函数是explicit的
    + `make_tuple`
+ 访问成员：`std::get<第几个>(一个tuple对象)`，索引从0开始
+ 辅助类模板：
  + tuple数量：`tuple_size<decltype(一个tuple对象)>::value`（`size_t`）
  + 对应位置元素类型：`tuple_element<第几个, decltpe(一个tuple对象)>::type`
+ 运算：要求对每个元素使用对应运算符必须是合法的
  + 相等：只有相同数量才比较

# bitset

+ 初始化：

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/bitset初始化.png)

+ 操作：

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/bitset操作.png)



# 正则表达式

`<regex>`





# 随机数

