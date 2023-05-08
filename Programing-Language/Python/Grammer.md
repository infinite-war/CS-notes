### commit

+ default arg：[manual](https://docs.python.org/3/reference/compound_stmts.html#function)：对于默认参数，表达式只会求值一次，之后都是这个值
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
	>python3 main.py
	140296173397056
	140296173397056
	140296174126720
	['armor', 'sword']
	"""
	```

### import

+ module：通常是文件，是运行时概念、一个Python的Object，有独立的命名空间
+ package：通常是文件夹，特殊的module，多了一个`__path__`属性
<hr>

absolute import
+ `import test`（test.py是在同目录下的文件）
	+ 把`test`作为一个string
	1. 去缓存找，找到则load给`test`这个identifier
	2. 没有：去几个文件夹下寻找找个string
		>文件列表：`sys.path`

	+ 找到后在一个命名空间中运行这个文件，更新缓存，将这个object给identifier

+ `import test as ts`

+ `import mypackage`
	1. 在文件夹下找到`__init__.py`，如果有，就在命名空间中运行它

+ `import mypackage.subpageckage.module`：则会运行对应module

+ `... as `
	>如果没有as，则命令中的各个名字在当前命名空间都可见

	 有as则只会有尾部的module

relative import：通过module的`__package__`属性变换成绝对路径再import
>这也解释了如果相对导入，然后通过python这个代码会报错，因为这样这个module在一个main package module，不知道其他module（只能被import中才能看到(import了package)）

在我的个人实践中
+ 相对导入只适用于一个大系统的子集，即由程序自己进入了一个package，然后这个package中module进行相互之间的相对导入，其他的基本都有锅

实践上
+ 相对导入适用于一个大系统的子集，比如一个程序运行中会进入一个module，这个module的import就可以通过相对import
+ 在一般情况下都推荐绝对导入，指的注意的是，绝对导入的起点是哪里呢？可以看`__file__`这个属性，从这个列表中的路径和绝对路径尝试进行拼接得到的。
	+ 我们会发现这里通常没有父目录，这意味最基本的跨package的import都不能满足，有两个方法  
		在代码前使用，
		```python
		import sys
		from os.path import abspath, dirname
		sys.path.append(abspath(dirname(dirname(__file__))))
		```
		这样就导入了目录  

		将父目录放入到环境变量中
		```python
		export PYTHONPATH=$PYTHONPATH:父目录绝对路径
		```

 
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

### Type Hint
>只是静态检查、只是静态检查、只是静态检查

+ [Doc](https://docs.python.org/3/library/typing.html)

+ 虚基类指针
	```python
	from typing import Type
	bp: Type[BaseClass] = None
	```

+ 类名循环依赖问题：把名称用双引号括起来解决
+ 模块循环依赖问题：
	```python
	from typing import TYPE_CHECKING
	if TYPE_CHECKING:
		from 包 import 名称
	```

	这个名称`TYPE_CHECKING`在运行时为False，但是静态检查时是True

+ 多种类型：`|`分割或
+ 某种类型或`None`：`Optional[类型]`

+ 可调用类型（函数）：`Callabel[[逗号分割的参数列表]返回值]`
	+ 没有返回值的函数：`NoReturn`

+ 特定项：`Literal[特定项列表]`
	+ 但是不是认为是特定项类型，而是一种独特的类型

	```python
	def request(url: str, method: Literal["GET", "POST"]):
		...

	request("www.baidu.com", "GET")  # 这会报错

	arg_method: Literal["GET", "POST"]
	```


+ 特定项：`Literal`
	+ 但是变量复制就飘红-》给变量做type hint，但是太长，而且不易一起变化
		+ 给Literal赋值给一个变量上做类型别名

+ 类型别名：给一个类型起个别名，
	+ 但是名字不同，但是内部一样，同类型的互用不报错，但是语义不对，
		+ 真的建立新类型`newname = NewType('newname', 原本的类型)`
			+ 但是这样这样就很严格了，需要显示转换

### 魔术方法
[Manual](https://docs.python.org/3/reference/datamodel.html#special-method-names)

`__str__` 方法用于返回对象的人类可读的字符串表示形式，而 `__repr__` 方法用于返回对象的机器可读的字符串表示形式。