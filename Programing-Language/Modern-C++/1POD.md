# 概述

+ C++是**静态数据(statically typed)类型语言**：在编译时检查类型(type checking)错误。
	>诸如Python这种解释型语言则是在程序运行时检查数据类型

+ C++的**数据对象**（存储类型）包括变量和常量（字面量），以及数组元素，结构成员：**数据对象通过标识符为数据提供位置标签**。
	>数据对象和存储类型是不同资料的翻译，统称为**对象**(Object)即可，变量是一种对象

+ C++的**数据类型**分为基本类型：整型和浮点型；还有复合类型：数组、指针还有结构、共用体和枚举等等（内置类型）和自定义类型

```mermaid
graph LR;
dt[数据类型data type];
type[内置类型build_in type];
clas[自定义类型];
base[基本类型basic type];
composite[复合类型composite type];
num[算术类型arithmetic type];
void[空类型void type];
int[整型integral type];
double[浮点型float type];
char[字符型character type];
bool[布尔类型];
array[数组array];
point[指针point];
re[引用reference];
struct[结构体structure];
union[共用体common];
enum[枚举enum];

dt --> type; dt --> clas;
type --> base; type --> composite;
base --> num; base --> void;
	num ---> int; num ---> double;
		int -.-> char; int -.-> bool;
composite --> array -.- point -.- re;
composite --> struct; composite --> union; composite --> enum;
  ```

**数据类型确定数据对象开辟空间大小和解释方法以及能在数据上执行的操作**

+ **标识符**(identifier)：一个变量、常量、函数和其他实体的名称。
	+ 意义：为数据类型和程序的存储实体提供的**位置标签**。
	+ 命名规则：
		+ 只能使用字母字符、数字和下划线（\_）
		+ 第一个字符不能是数字
		+ 大小写敏感
		+ 不能使用C++关键字
		+ 以两个下划线或下划线和大写字母打头的名称被保留给实现（编译器以其使用的资源）使用。以一个下划线开头的名称被保留给实现，用作全局标识符。
		+ C++对于名称的长度没有限制，但有些平台有长度限制。

# 数据对象

+ ***变量***：提供一个具名的、可供程序操作的存储空间。
	+ 定义：类型说明符(type specifier)以及紧随的变量名列表，逗号分隔，分号结束。  
		列表中的变量名由类型说明符指定，定义时可赋值。
  
+ **常量**：通过`#define`定义的符号常量或者**`const`**限定的不允许修改的变量
	+ 命名规范：1. 首字母大写、2. 整个名称大写、3. 以字母k打头。
	+ 定义方法：
		1. `#define`预处理指令  
			格式：`#define NAME value` 没有等号，没有分号。
		2. **`const`**限定符  
			格式：**`const type`**`name = value; ` C++建议。
		3. C++11新增关键字`constexpr`创建常量表达式。

+ **字面量**(literal)：即时使用的基本类型值，其都对应着一种数据类型  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/指定字面值类型.png" alt="指定字面值类型" style="zoom:67%;" />

+ 声明：C++提供两种声明，但本质只能有一个定义
	1. 引用声明(referencing declaration)或简称为声明(declaration)：`extern type name;`：创建名字
	2. 定义声明(defining declaratin)或简称为定义(definition)：`限定符 type name (= value)`：为名字创建实体

	若声明时初始化则是定义，在函数内则报错；声明可以多次，但是定义只能一次。

+ 初始化(initialized)：在对象创建时获得特定值：将声明和赋值合并在一起。

+ 

  + 语法：
    1. **`type`**` name = value;` value可为符号常量、字面值常量、定义过的变量、表达式。
    2. **`type`**` name(value);` C++为同一类构造函数定义的初始化语法。
    3. 列表初始化(list initialization)：花括号括起来的逗号分隔的值列表：**`type`**`name = {value1, ...};`等号可选
       + 花括号内为空则默认为0
       + 禁止缩窄转换（但value是变量不保证）
       + C++11可用其初始化单值变量
    
  + 初始化：创建变量时赋予其初始值

    赋值    ：把变量当前值擦除并填充新值

    > 形式上类似，但本质很不同

  + 默认初始化(default initialized)：

    + 在函数体外的变量初始化为0
    + 在函数体内的变量不被初始化(uninitialized)，其值未定义
    + 类自决定初始化对象方式

+ `sizeof`运算符：C++工具：检测存储长度：返回类型或表达式的字节数

  格式：`sizeof `**`expr`** 或 `sizeof (`**`type`**`)` 。对类型名要放在括号里，对变量名，则是可选的。
  
+ **`const`**限定符：const放在数据类型关键字前使声明的变量只能被初始化赋值

  + const常量只能在本文件中使用

    多文件使用`extern const type name;`：定义时初始化，声明时也使用两个关键字

  1. 定义常量

  2. 对象保护：在函数传参中避免修改实参

  3. 用于指针和引用：

     + 指针（一级间接引用）：指针是派生类型，星号逻辑上依附于变量

       1. const在星号前（底层指针(low-level const)），限定的是`*ptr`，即那个地址，所以不能修改这个地址（通过指针）；
       2. const在星号后（顶层指针(top-level const)），限定的时`ptr`，即指针地址，所以不能修改这个指针变量。

       > 二级间接引用：很混乱，避免。

     + 不用让被限定的地址与无限定的指针或引用绑定，这个行为让值得限定很滑稽，不被定义

  + 常量表达式(const expression)：值不会改变并且在编译过程就能得到计算结果的表达式

    **`constexpr`**关键字（C++11）：使用方式同const，要求限制的对象必须是常量表达式

# 内置数据类型

+ 类型别名(type alias)：

  1. 使用预处理器`#define`：文本替换

     格式：`#define aliasName typeName`

  2. 使用关键字`typedef`：为复杂类型提供新名称

     格式：`typedef typeName aliasName;`

  3. 别名声明(alias declatation)：`using aliasName = typeName;`

  + 对于派生类型如引用和指针，文本替换只能影响一个，类型别名才能全部

  + 数组类型别名：

    ```c++
    typedef type type_[size];
    using type_ = type[size];
    ```

    其中typedef的形式有点反直觉

+ **`auto`**类型说明符（C++11）：与顶层底层const的冲突

  不指定变量的类型，编译器将把变量的类型设置成与初始值相同。

  只能用于单值初始化，不能用于初始化列表，不管这个单值多么复杂。

+ **`decltype`**类型指示符：选择并返回操作数的数据类型

  + 操作：`decltype(what) name;`
  + 与顶层底层const的关系
  + 当为操作数添加一层或多层括号时，其变成表达式，变量是一种可以作为赋值语句左值的特殊表达式，故返回引用类型

## 基本算术类型

+ 数据类型性质：存储大小、解释方法->取值范围和精度，在其上的操作（）运算符

https://en.cppreference.com/w/c/language/arithmetic_types

   img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/C++算术类型.png" style="zoom:70%;" /

  + `climits`头文件有算术类型范围符号常量。

+ 基本类型符号：可作前缀（接空格）修饰其他算术数据类型->算术类型有无符号可由软件工程师设置。

  | 符号类型关键字 | 说明       |
  | -------------- | ---------- |
  | **`signed`**   | 强调有符号 |
  | **`unsigned`** | 无符号     |

+ 类型*转换*(convert)：

  + 发生时间：1. 赋值时；2. 表达式含不同类型时；3. 函数传参。

    + 自动类型转换：

      需大变大：无符号 -> **`long double`** -> **`double`** -> **`float`** -> **`int`** -> 其他整型

    + 强制类型转换（C版本）：

      格式：`(`**`typeName`**`) value` 或者 **`typeName`**` (value)` 。

    + 强制类型转换运算符（C++11）：

      > C++创始人Bjarne Stroustrup看来C的类型转换运算符太过松散，BS添加类型转换运算符使转换过程更规范。

      格式：`cast_name<type>(expression)`

      | 运算符             | 说明                                                         |
      | ------------------ | ------------------------------------------------------------ |
      | `static_cast`      | 常用<br>大值赋小值（不在乎精度损失）<br>找回存于`void*`的指针 |
      | `const_cast`       | 改变表达式常量属性                                           |
      | `reinterpret_cast` | 用于天生危险的类型转换                                       |
      | `dynamic_cast`     | 用于类层次结构中进行向上转换                                 |

  + 转换方向：

    + else -> bool : 非0 -> true、0 -> false ; bool -> else : true -> 1、false -> 0（包括指针）

    + 浮点数->整数：小数部分截断

      整数->浮点数：小数部分为0，精度可能损失

    + 给无符号类型赋超范围值：取模
    
      给符号类型赋超范围值：结果未被定义

### 整型

+ 存储：C++数据长度与机器有关

  | 符号整数类型    | 整数宽度                     | 数值范围 |
  | --------------- | ---------------------------- | -------- |
  | **`short`**     | 至少16位                     |          |
  | **`int`**       | 至少与short一样长            |          |
  | **`long`**      | 至少32位，且至少与int一样长  |          |
  | **`long long`** | 至少64位，且至少与long一样长 |          |

+ 整型字面量：**`int`**类型认为是整数最自然的类型，整数如果没有理由（后缀，溢出）用其他类型，默认int型。

  + 类型后缀标识

    | 标识                           | 含义      |
    | ------------------------------ | --------- |
    | 后缀`u`或`U`，可与其他标识组合 | unsigned  |
    | 后缀`l`或`L`                   | long      |
    | 后缀`ll`或`LL`（C++11）        | long long |
    
  + 进制前缀标识：无可容纳类型则报错
  
    | 进制     | 前缀       | 说明                                     |
    | -------- | ---------- | ---------------------------------------- |
    | 十进制   | 默认       | 采用能容纳的int、long和long long中最小的 |
    | 八进制   | `0`        | 在十进制的基础上采用无符号类型           |
    | 十六进制 | `0x`或`0X` | 同八进制                                 |
  
  + 整型字面量可以存储带符号类型，但十进制字面值数不会是负数，负数是运算后的结果

	+ C++14开始提供二进制字面量，即前缀`0b`
		+ 但是IO streams只有`dec`，`hex`，`oct`三种manipulator操纵器
	+ C++14 开始，允许在数字型字面量中任意添加 `'`来使其更可读

#### 字符类型

+ ***char类型***：存储宽度：8 ；取值范围：0~256 ；

  + 定义：存储字符，存储本质是数值。
    + 字符：用单引号（''）括起来的单个字符——char类型字面量
    + 小整数：char默认不说明符号，需要软件工程师定义。

  + 字面量：由单括号括起来的一个字符

    字符串：由双括号括起来的零个或多个字符，可分多行多字符串，编译器自动拼接

  + 转义序列(escape sequence)：不可打印(nonprintable)字符+特殊含义字符
  
    | 字符名称   | ASCII符号 | C++代码 | 八进制      | 十六进制     |
    | ---------- | --------- | ------- | ----------- | ------------ |
    | 换行符     |           | `\n`    | `\三个数字` | `\x所有数字` |
    | 水平制表符 |           | `\t`    |             |              |
    | 垂直制表符 |           | `\v`    |             |              |
    | 退格       |           | `\b`    |             |              |
    | 进纸符     |           | `\f`    |             |              |
    | 回车       |           | `\r`    |             |              |
    | 振铃       |           | `\a`    |             |              |
    | 反斜杠     |           | `\\`    |             |              |
    | 问号       |           | `\?`    |             |              |
    | 单引号     |           | `\'`    |             |              |
    | 双引号     |           | `\"`    |             |              |
    
    > Latin-1字符集：使用八进制和十六进制表示的方法，除了转义字符，也可以表示正常的字符

#### 布尔类型

+ ***bool类型***：存储宽度：1位；
  + 布尔类型可提升为int型：真是一，假是零
  + 数字和指针值可隐式转换为布尔值：非零是真，零是假
+ 字面量：`true和false`

### 浮点型

+ 存储：基准值+缩放因子

  | 浮点数类型        | 有效位数                                | 允许的指数最小范围 |
  | ----------------- | --------------------------------------- | ------------------ |
  | **`float`**       | 至少32位（一般32位）                    | -37~37             |
  | **`double`**      | 至少48位，且不少于float（一般64位）     | -37~37             |
  | **`long double`** | 至少和double一样多（一般80、96、128位） | -37~37             |

+ 字面量：

  + 写法

    | 小数表示法   | E表示法        | 科学计数法 |
    | ------------ | -------------- | ---------- |
    | 必须有小数点 | 尾数E（e）指数 |            |

  + 类型后缀标识：默认double类型；只对浮点型字面量有效，在其他类型字面量则报错（而不是强制转换）

    | 标识         | 含义        |
    | ------------ | ----------- |
    | 后缀`f`或`F` | float       |
    | 后缀`l`或`L` | long double |

    > float类型的数值进行计算会变成double类型再计算，这会降低速度，后缀标识或强制转换可以避免。


## 复合类型

### 引用

+ 引用(reference)类型：为数据对象定义**别名**，将新对象与初始值**绑定**(bind)（而不知拷贝值），无法解绑必须初始化；

+ 格式：`typeName &sam_ = sam;`
  + 引用本身不是对象，所以不能定义引用的引用
  + 一个声明语句中可以有多个引用，每个引用标识符必须以`&`开头

1. 必须在声明引用变量时进行初始化——引用变量的指向不能变：两个标识符指向同一块地址
2. 右值引用

### 数组

+ 对数组来说，数组大小也是类型的一部分

+ 声明格式：**`typeName`**` arrayName[arraySize];` 其中`[]`为成员运算符

  arratSize为指定元素数目，必须是整型常数或const值或者是常量表达式

+ 访问：通过下标/索引对元素进行编号，从0开始。使用带索引的方括号表示法指定数组元素（编译器不检查下标有效性）

  > 下标类型为`size_t`类型，一种与机器相关的无符号类型，在`<cstddef>`头文件中定义

  + 确定数组尾后指针/超尾：（超尾不能解引用或递增——只能保证其存在而对其他一无所知）

    1. ```c++
       type *en = &a[size];
       for (auto it = arr; it != en; ++ it);
       ```

    2. C++11提供函数`begin()`和`end()`，使其类似容器使用

       ```c++
       for (int en = end(arr), it = begin(arr); it != en; ++ it)
       ```

+ 初始化：

  1. 初始化列表：花括号括起来的用逗号分隔的值列表

     + 数目不对应时按顺序初始化，其余初始化为0。
  2. 初始化器`typeName arr[len] ={ [3] = 2; } `
     + 无指定则按顺序填充0

  + 若定义时有初始化而方括号为空，C++编译器自动计算数组个数确定长度

+ 多维数组：本质是数组的套娃

  ```cpp
  int sam[123][456];  //sam是一个123个元素的数组，每个元素是456个元素的数组
  int a[2][3] = {
      {1, 2, 3},
      {4, 5, 6}
  };
  char s[len][num] = {  //开辟的地址连续
      "qwe",
      "asd"
  };
  char * s[Num] = {  //此为指针的数组，只开辟指针的空间，其指向（指针的值）未必连续
      "qwe",
      "asd"
  };
  string s[Num];
  ```

  + 范围for：除最内层外的循环变量应用引用类型，即使不修改：防止auto的新变量是指针而不是数组

+ 数组的替代品：标准模板库的模板类——向量（可变长数组）`vector`

  + 包含在vector头文件、名称空间std中，存储在自由存储区或堆中。
  + 语法：`vector<typeName> vt(n_elem, 初始化);` 其中n_elem可以是整型常量，也可以是整型变量。
    + 用数组初始化向量：`vector<type> vec(begin(arr), end(arr))`
    + 访问：
      1. 中括号表示法：可与数组一样使用成员运算符（`[]`）；因为数组名本质指针，索引非法不会被警告。
         1. 成员函数`at()`：`at(seat)`，捕获非法索引，**慢**。
      2. 包含成员函数`begin()`和`end()`来确定边界。

#### 字符串

+ 空字符：写作`\0`，ASCII码为0。


1. C风格字符串：以空字符标记结尾的字符数组。

   + 用法：

     1. `char str[] = {'', '', '', '\0'};` 必须要有空字符，不然就仅是字符数组而已。

        + 键盘输入字符串时，不用特意输入末尾空字符，会自动添加

          同时，数组大小要可以存储字符串，包括自动添加的空字符。如果数组更大，其余元素自动填充空字符。

     2. 字符串字面量：双引号（“”）括起来的若干字符，编译器会在末尾自动填充空字符。

        > C++将字符串字面量解释为指向字符串所在地址的指针（其为静态变量，一直存在）
        >
        > `char str[] = "oabaoaboaba";` 注意区别 `"a"` 和 `'a'` 前者是一个字符串的地址，后者是一个字符的编码数值。
        
        + 原始(raw)字符串（C++11）：前缀R表示，内容用双括号括起来，不用使用转义序列：`R"(字符串)"`、`+*(字符串+*)`
        

     + 由空白分隔的字符串常量自动拼接成一个字符串：`cout << "123" "qwe";`是合法的。

   + 相关函数：`cstring`头文件

     1. | sizeof运算符     | strlen()函数                 |
        | ---------------- | ---------------------------- |
        | 指出整个数组长度 | 返回字符串长度，不包括空字符 |

     2. | 输入函数                  | 说明                                            |
        | ------------------------- | ----------------------------------------------- |
        | cin>>str                  | 遇到空白停止                                    |
        | cin.getline(char *,  int) | 遇到换行符或len - 1停止，丢弃换行符、添加空字符 |
        | cin.get(char *, int)      | 遇到换行符或len - 1停止，返回换行符、添加空字符 |

        + get不借助帮助不能跨过换行符，不过它有一个变体`cin.get()`：读取下一个字符。

          两个类成员函数拼接合并即为`cin.get(str, len).get();`

          数值字符混合：cin读取字符会留下空白，可以`(cin >> sam).get().get(str, len);`

2. string类库：ISO/ANSI C++98标准添加string类扩展了C++库；需要头文件`string`，string类位于名称空间`std`中。

   + string类具有C风格字符串的属性，其为简单变量来隐藏数组属性，==string字符串的末尾不是空字符==

   + 操作：

     1. 赋值（=`strcpy()`）：可以当作基本类型直接赋值，而不是按数组元素拷贝。

     2. 拼接/附加（=`strcat()`）：可用运算符`+`将两个string类对象合并，可用运算符`+=`将字符串附加在string对象末尾

        > 操作数必须有string类对象

     3. 拼接和附加：简化字符串合并操作，可以使用运算符`+`将两个string对象合并起来，还可以使用运算符`+=`将字符串附加到string对象的末尾。

     4. 获取字符串字符数：类方法`size()`
     
        > 其返回值是`stirng::size_type`类型，是**无符号类型**
     
     5. I/O：
     
        | 方法              | 说明                   |
        | ----------------- | ---------------------- |
        | cin >>            | 遇到空白停止，返回空白 |
        | getline(cin, str) | 读取一行，丢弃换行     |
     
     6. 转换为C-风格字符串：类方法`char* c_str();`
     

### 指针

+ 空指针：
  + `(* void) 0 `
  + C语言  预处理变量(preprocessor variable)：NULL（头文件cstdlib），其值为0
  + C++11 关键字**`nullptr`**
+ 描述指针的表示法：十六进制法

1. 符号：取地址运算符（`&`）：获得数据对象（常规变量）地址。

   ​			解除引用（间接值）运算符（`*`）获取指针指向的数据对象的值。
   
2. 声明：格式：`type * name;`：若连续声明多个指针，要在每个指针变量前都加上星号（因为指针是派生量）

   + `*`运算符两边的空格是可选的

     1. `type* name;` 强调`type*`是一个类型：指向`type`的指针类型。
     2. `type *name;` 强调`*name`是一个指针：`*name`是`type`类型的。

   + 指针的类型：

     + `void *`指针：可存放任意对象的地址，但不能直接操作

   + 指向指针的指针：`**p`

     引用指针的引用：`*&r`

3. 初始化：未初始化的指针变量其指向的内存是不知道的


+ C++对数组名的解释：

  1. C++将数组名解释为指针：

     ```cpp
     int a[N];
     //a 等价 &a[0]
     //*(a + i) 等价 a[i]
     ```

  2. 数组名是指针常量。

  3. `sizeof`运算符：

     + 数组对应得到数组的字节长度        这种情况C++不会对数组名解释为地址。
     + 指针对应得到指针本身的字节长度

  4. 对数组名取地址`&arrayName`：虽然数组名被解释为地址，但对数组名取地址得到的是整个数组的地址

     + `type (* ParrayName)[10] = &arrayName;` 

     + `[]`的优先级大于`*`

       ```c++
       int * p[10];  	//p是一个指针数组，先于[]结合成为数组，再与*结合成为指针，是指针的数组
       int (* p)[10]:	//p是一个指针，可以指向一块10个int型长度的地址（首
       ```

+ 指针算术：

  1. 指针加一：加上的量是指针指向的基本类型的字节数量

  2. 指针相减：仅用于同一数组，得到元素间隔（只能用于同一数组）

     > 指针相减的结果是`ptrdiff_t`的标准库类型，定义在`cstddef`头文件中，是符号类型

  3. 指针比较：必须同类型，必须有值，比较的地址而不是指向的值

+ 指针和字符串：

  1. 字符串常量被认为指向字符串存储位置的第一个元素的地址

  2. ==`cout`对`char*`类型：会从此地址开始打印至空字符为止。==

     > 在cout和多数C++表达式中，char数组名、char指针以及引号括起的字符串常量都被解释为字符串第一个字符的地址

  3. copy字符串：

     1. 复制地址：直接指针赋值拷贝的是地址

     2. 拷贝内容：使用`cstring`头文件的`strcopy(char *, const char *)` `strncopy(char *, const char *, int);`

        ​                   前者不处理多余的字符，后者如果过多会停止，不过这样原数组末尾不是空字符，要手动修改
     
  4. C-风格的字符串比较

     C++将C-风格的字符串视为地址，所以不能直接用关系运算符来比较。

     使用`strcmp(const char *, const char *)`函数

+ 指针与结构、联合、枚举：

  + 指针访问结构体成员

    1. 箭头成员运算符（`->`）：`ps -> igyr1;`
    2. 解引用                             ：`(* ps).igyr1;` （注意优先级）

### 结构

#### 结构体

结构是用户定义的类型，而结构声明定义了这种结构的数据属性；定义类型后，可以创建这种类型的变量。

+ 定义
+ 创建
+ 初始化
+ 访问成员
+ 位字段：TODO

+ 

#### 共用体

能存储不同的数据类型，但是只能同时存储其中的一种类型，可在不同时期存储不同成员对应的值

关键字`union`

#### 枚举

+ C++98：`enum name = {NUM1, NUM2, NUM3, ……};` 可以省略枚举类型名
	+ 可显式地设置枚举量地值：`enum name = {NUM1 = 1, NUM2 = 2, NUM3 = 4;}`
	+ 可显式地定义其中一部分枚举量地值：`enum name = {NUM1, NUM2 = 100, NUM3};`，其余按照顺序，定义后按顺序递增。
	+ 可创建多个值相同的枚举量：`enum {NUM1, NUM2 = 0, NUM3, NUM4 = 1};` 两个0两个1。

+ C++11类作用域内枚举（因为关键字class，所以也被称为枚举类）：`enum class Name {Num1, Num2, ... , Numn};` 其中`class` 可以用`struct` 代替。
	>解决同一文件不同枚举定义同名枚举量的冲突

	+ 避免隐式转换
	+ 明确底层实现
		+ 甚至可以指定：`enum class enumName: type {...};`

## 运算符

+ 表达式(expression)：由运算符(operator)和运算对象(operand)组成，每个表达式都有值，即结果(result)
	+ 可分为一元运算符(unary operator)和二元运算符binary operator，元即操作数。

+ 运算符考虑precedence优先级和associativity结合律去考虑order of evaluation求值顺序

+ 赋值运算符：
	+ 值类型问题
	+ 结合性从左到右，所以可以连续赋值

+ 递增运算符和递减运算符
	+ 不要在同一条语句对同一个值多次使用，C++没有定义正确的行为。C++可以保证在一个顺序点前完成副作用，但是具体什么时候进行不确定。

+ [运算符优先级表](https://en.cppreference.com/w/cpp/language/operator_precedence)

## 字面量

+ 自定义字面量
	```cpp
	#include <iostream>
	
	struct Length {
	
	  static constexpr double fac[] = {1000.0, 1.0, 1e-3};
	  enum class Unit {
	    kilometre,  // 千米
	    metre,      // 米
	    centimetre, // 厘米
	  };
	  explicit Length(double v, Unit u = Unit::metre) {
	    value = v * fac[static_cast<int>(u)];
	  }
	  friend Length operator+(Length lhs, Length rhs) {
	    return Length(lhs.value + rhs.value);
	  }
	
	  double value;
	};
	
	constexpr double Length::fac[]; // Definition of static member
	
	Length operator"" _km(long double v) {
	  return Length(v, Length::Unit::kilometre);
	}
	Length operator"" _m(long double v) { return Length(v, Length::Unit::metre); }
	Length operator"" _cm(long double v) {
	  return Length(v, Length::Unit::centimetre);
	}
	
	int main() {
	  auto t = 1.0_m + 10.0_cm;
	  std::cout << t.value << '\n';
	  return 0;
	}
	```
