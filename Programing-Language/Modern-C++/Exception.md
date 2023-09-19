[exception language ref](https://en.cppreference.com/w/cpp/language/exceptions) | [exception lib ref](https://en.cppreference.com/w/cpp/error/exception)

+ `abort()`和`exit()`
+ [`throw` expression](https://en.cppreference.com/w/cpp/language/throw)和[try-block](https://en.cppreference.com/w/cpp/language/try_catch)
+ [noexcept](https://en.cppreference.com/w/cpp/language/noexcept)

+ 异常安全的代码，指当异常发生时即不会发生资源泄露，也不会使系统处于不一致的状态
	+ 基本保证：抛出异常后，对象仍然是valid的状态（没有数据结构是损害的且没有资源泄露），但是不知道处于什么状态
	+ 强烈保证：抛出异常后，程序的状态没有发生任何变化，就像没有调用这个函数一样
	+ 不抛异常保证：最强保证，函数总能完成它所承诺的事情。