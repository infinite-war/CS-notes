CRTP

## C++11

1. 自动类型推导（auto关键字）
2. 范围for循环（range-based for循环）
3. 统一的初始化语法（uniform initialization syntax）
4. 右值引用（rvalue references）
5. 移动语义（move semantics）
6. lambda表达式
7. 列表初始化（list initialization）
8. nullptr关键字
9. 强类型枚举（strongly-typed enums）
10. 静态断言（static_assert）
11. 并发支持（concurrency support）
12. 委托构造函数
13. 管理动态内存的智能指针（unique_ptr和shared_ptr）
14. 可变参数模板
15. 新的关键字（constexpr和nullptr）
16. 新的标准库组件（例如元组tuple和array）
17. 移动语义
## C++14

1. 二进制字面量（binary literals）
2. 泛型 lambda 表达式（generic lambda expressions）
3. 允许在 constexpr 函数中使用控制流语句和局部变量（allowing control flow statements and local variables in constexpr functions）
4. 函数返回类型后置（trailing return types）中可以使用decltype(auto) 推导返回类型
5. lambda 表达式可以用于 constexpr 函数
6. 初始化列表可用于自定义类型
7. 新增 make_unique() 函数用于创建 unique_ptr
8. 运行时大小数组（variable templates）
9. 改进了类型推导规则（improvements in type deduction）
10. 新增了 std::quoted 用于处理带引号的字符串
11. 新增了几个 STL 算法和容器（several additions to STL algorithms and containers）
12. 常量表达式函数
13. 通用的lambda表达式捕获初始化
14. 模板别名模板

## C++17

1. 结构化绑定（structured bindings），可以将结构体、元组等类型的成员绑定到单独的变量上。
2. if constexpr，允许在编译期选择执行不同的代码分支。
3. inline 变量（inline variables），允许定义内联变量。
4. constexpr if，允许在编译期选择是否对某段代码进行编译。
5. 折叠表达式（fold expressions），用于简化表达式模板的实现。
6. 新增了一些 STL 算法，如 std::clamp()、std::sample()、std::for_each_n() 等等。
7. UTF-8 字符串字面量（UTF-8 string literals），允许使用 UTF-8 编码的字符串字面量。
8. 嵌套命名空间（nested namespaces），允许在命名空间中嵌套其他命名空间。
9. 内联变量模板（inline variable templates），允许定义内联变量模板。
10. if和switch语句中的初始化
11. 强制执行语句attribute
12. 表达式语句if constexpr
13. constexpr lambda表达式

C++20：

1. 概念（Concepts），引入了一种新的语言特性，用于描述类型的概念（concept），以替代传统的 SFINAE 技术，使得模板的错误信息更加清晰明了。
2. 三方运算符（Three-way comparison operator），引入了一个新的运算符 <=>，用于进行三方比较（即比较大小）。
3. 初始化语句允许使用 auto 类型推导（Allowing type deduction for initialized variables）。
4. constexpr 函数的限制大幅放宽（Relaxing constraints on constexpr functions），允许 constexpr 函数包含 if 语句和循环语句等控制流语句。
5. 模块化（Modules），引入了一种新的模块化机制，用于替代传统的头文件包含机制，使得代码的组织和管理更加清晰和高效。
6. 新增了一些 STL 算法和容器，如 std::ranges::views、std::span、std::format 等等。
7. 协程（Coroutines），引入了一种轻量级的协作式多任务机制，使得异步编程更加简单和高效。
8. 初始化列表支持 std::vector 和 std::array（Initializer lists for std::vector and std::array）。
9. 嵌套的命名空间可以用作成员访问（Nested namespaces as members）。
10. 同步队列和信号量
11. 格式化输出
12. 增强型类型枚举
