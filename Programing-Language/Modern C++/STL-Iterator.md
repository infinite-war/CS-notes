STL(Standard Template Library)标准模板库


# 迭代器

+ 迭代器：**`iterator`**；头文件`<iterator>`

+ 迭代器范围(iterator range)：由一对迭代器表示，分别指向同一个容器中的元素和尾元素之后的位置(one past the last element)——begin、end/first、last（会有歧义）——左闭合区间(left-inclusive interval)：$[begin, end)$

  + 方法：`begin()`和`end()`：

    + 重载：如果对象为const的，其返回也是const的

      或者：`cbeing/end()`：返回const

    > 反向迭代器：`rbegin/rend()`：也做了重载`rcbegin()/rcend()`

  | 迭代器定义方式 | 具体格式                                     | 获取方法          |
  | -------------- | -------------------------------------------- | ----------------- |
  | 正向迭代器     | `容器类名::iterator 迭代器名;`               | `begin()/end()`   |
  | 常量正向迭代器 | `容器类名::const_iterator 迭代器名;`         | `cbegin()/cend()` |
  | 反向迭代器     | `容器类名::reverse_iterator 迭代器名;`       | `rbegin()/rend()` |
  | 常量反向迭代器 | `容器类名::const_reverse_iterator 迭代器名;` |                   |

+ 运算符：++/--/==/！=

  + 随机迭代器：+/-/+=/-=/<>

    + 算术运算操作数是int：跳跃

      ​			   操作数是迭代器：距离，类型`defference_type`

+ Iterator Category迭代器类型：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/迭代器类别2.jpg)

  + 容器使用的迭代器类型：

    | 容器     | 迭代器类型 |
    | -------- | ---------- |
    | `array`  |            |
    | `vector` | 随机       |
    | `deque`  |            |
    | `list`   |            |
    | `set`    |            |
    | `map`    | 前向       |

## 其他迭代器

+  iterator正向迭代器：

+ reverse iterator反向迭代器：

  > 除了forward_list之外的容器都提供

  + `base()`方法：获得对应位置的正向迭代器

+ Insert iterator插入迭代器：`<iterator>`中的`back_inserter()`：接受一个指向容器的引用，返回一个与该容器绑定的插入迭代器

  ```c++
  vector<type> vec;
  auto it = back_inserter(vec);  //调用push_back
  for (int i = 1; i <= 9; ++ i) *it = i; //vec = {1..9}
  ```

   ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/插入迭代器.jpg)

+ Stream iterator流迭代器：将流当作一个**特定类型**的**元素序列**

  + 绑定流，使用`<<`或`>>`控制流
  + 默认初始化的迭代器可作为循环的尾后迭代器

  ```c++
  istream_iterator<int> in_iter(cin), eof;
  while (in_iter != eof) vec.push_back(*in_iter++);//1
  vector<int> vec(in_iter, eof);//2
  
  //结合算法库，极限压行
  cout << accumulate(istream_iterator<int>(cin),
                     istream_iterator<int>( ), 
                     0) << endl;
  ```

  + 操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/流迭代器.jpg)

+ move iterator移动迭代器
