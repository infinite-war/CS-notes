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
python3 main.py
140296173397056
140296173397056
140296174126720
['armor', 'sword']
"""
```

[manual](https://docs.python.org/3/reference/compound_stmts.html#function)：对于默认参数，表达式只会求值一次，之后都是这个值，所以每个默认list都是同一个list对象

### Decorator


### type hint

[doc](https://docs.python.org/3/library/typing.html)

+ 类型检查只是声明，为了可读性，在实际运行中仍然万物皆对象

+ 只在类型检查器执行时执行：
	```python
	from typing import TYPE_CHECKING
	
	if TYPE_CHECKING:
		from 包 import 名称
	```
	如果两个包使用对方的名称，则会出现循环依赖，上面的写法可以在类型检查时引入，而在实际运行时不引入  
	具体的，`TYPE_CHECKING`在类型检查时为`False`，而在实际运行时为`True`  
	这样的写法要求这里的`名称`在当前的包内也是只做类型检查

+ 基类指针：
	```python
	from typing import TYPE_CHECKING
	
	if TYPE_CHECKING:
		from 包 import BaseClass  # 这是我实现的一个类

	class OtherClass():  # 不是这个类和Base继承，是组合，看下面
		dirve: Type["BaseClass"] = None  # 这个属性可以接受BaseClass的子类
	```