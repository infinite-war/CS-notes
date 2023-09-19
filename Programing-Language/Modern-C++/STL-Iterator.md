+ 迭代器：**`iterator`**；头文件`<iterator>`
+ 迭代器范围(iterator range)：由一对迭代器表示，分别指向同一个容器中的元素和尾元素之后的位置(one past the last element)  
	左闭合区间(left-inclusive interval)：$[begin, end)$

	+ 方法：`begin()`和`end()`：
		+ 重载：如果对象为const的，其返回也是const的

		或者：`cbegin/cend()`：返回const

	+ 反向迭代器：`rbegin/rend()`：也做了重载`rcbegin()/rcend()`

  | 迭代器定义方式 | 具体格式                                     | 获取方法          |
  | -------------- | -------------------------------------------- | ----------------- |
  | 正向迭代器     | `容器类名::iterator 迭代器名;`               | `begin()/end()`   |
  | 常量正向迭代器 | `容器类名::const_iterator 迭代器名;`         | `cbegin()/cend()` |
  | 反向迭代器     | `容器类名::reverse_iterator 迭代器名;`       | `rbegin()/rend()` |
  | 常量反向迭代器 | `容器类名::const_reverse_iterator 迭代器名;` |                   |

+ 运算符重载：++/--/\==/\!=
	+ 随机迭代器：+/-/+=/-=/<>

Iterator Category迭代器类型
![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/迭代器类别2.jpg)

