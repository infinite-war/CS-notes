### default arg

```python
class Player:
    def __init__(self, name, items=[]) -> None:
        self.name = name
        self.items = items
        print(id(self.items))

p1 = Player("Alice")
p2 = Player("Bob")
p3 = Player("Charles", ["sword"])

p1.items.append("armor")
p2.items.append("sword")

print(p1.items)

"""
> python3 main.py
140296173397056
140296173397056
140296174126720
['armor', 'sword']
"""
```
[manual](https://docs.python.org/3/reference/compound_stmts.html#function)：对于默认参数，表达式只会求值一次，之后都是这个值，所以每个默认list都是同一个list对象

### 迭代器和生成器
+ [iterable](https://docs.python.org/3/glossary.html#term-iterable)可迭代对象：必须实现`__iter__`
+ [iterator](https://docs.python.org/3/glossary.html#term-iterator)迭代器：必须实现`__next__`

for loop会从可迭代对象中生成迭代器，即调用`iter(可迭代对象)`，之后不断用`next()`作用于它，直到`raise StopIteration`
>manual中说iterable也应该实现`__next__`，为了用户通过`next()`去跨过前几个元素

+ generator(function)：含有关键字`yield`的函数，返回generator iterator
	+ 用next从迭代器喊护士得到是yield的值，那么这个函数return的值是通过`catch StopIteration`得到的
+ generator iterator：一种object

generator较于itrator的区别是它基于frame
generator较于itrator的新功能`send`：yield语句可以有“左值”，即在yield后等待生成器对象send新值进来（实质上`next(生成器对象) <==> 生成器对象.send(None)`）

### type hint
[doc](https://docs.python.org/3/library/typing.html)
>只用于静态检查，运行时仍然万物皆对象
>>这里有个小小bug，就是coder按照hint实现，这时在测试时不会出现错误，以为hint正确，实际上可能出现错误，所以要充分的静态检查呀。

+ 好像：typing可能会弃用

+ 类似虚基类指针数组：
	```python
	from typing import Type
	sam: Type[BaseClass] = None
	```

+ 循环依赖：对于之后在做evaluation的type lint：把名称用双引号括起来
+ 模块循环依赖：
	```python
	from typing import TYPE_CHECKING
	
	if TYPE_CHECKING:
		from 包 import 名称
	```
	具体的，`TYPE_CHECKING`在类型检查时为`False`，而在实际运行时为`True`，这样的写法要求这里的`名称`在当前的包内也是只做类型检查

### 魔术方法
[Manual](https://docs.python.org/3/reference/datamodel.html#special-method-names)