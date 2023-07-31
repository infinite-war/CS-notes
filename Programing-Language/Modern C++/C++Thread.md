## `volatile`

+ Reference：
	+ [始终的《谈谈 C/C++ 中的 volatile》](https://liam.page/2018/01/18/volatile-in-C-and-Cpp/)

## 锁

### 互斥锁
[`<mutex>`](https://zh.cppreference.com/w/cpp/thread/mutex)，请查看示例

+ `std::mutex`的定义：
	+ 在类中：
		```c++
		mutable std::mutex m;
		```
		其中`mutable`即为可变的，因为如果类对象是const的，但是锁肯定需要被修改的，这是特殊说明

+ 如何使用：
	```c++
	type function_name(...) {
		std::unique_lock<std::mutex> lck(m);
		...
		lck.unlock();  // 显示解锁
		lck.lock();    // 显示上锁
	}
	```
	对象`lck`在构建时自动上锁，之后可通过方法`lock`或`unlock`显式上下锁。

	+ 在Golang中有这样的写法：
		```go
		var lck sync.Mutex
		func foo() {
			lck.Lock()
			defer lck.Unlock()
		    // ...
		}
		```
		因为在函数中随时可能退出或者抛出异常，正常写法需要在每个地方都进行显式的开锁。  
		`defer`语句即为退出当前代码块（无论是退出还是抛出）时解锁。  
		C++也有类似的
		```c++
		type function_name(...) {
			std::lock_guard<std::mutex> lck(m);
			...
		}
		```
		这样即可实现同样的功能

	lock_guard语法更简单，unique_lock有更自由的功能，相应的有更高的时空消耗。

#### 锁的唤醒
如果我们想因为某种条件上锁，并在某些条件下解锁怎们办呢？  

[`<condition_variable>`](https://zh.cppreference.com/w/cpp/thread/condition_variable)，请查看示例

### 读写锁
对于同一个临界资源，有多个线程要访问，对于只读访问，它似乎不需要加入阻塞，让他们自由的访问临界资源似乎没什么不妥。

[`<shared_mutex>`](https://zh.cppreference.com/w/cpp/thread/shared_mutex)，请查看示例

### 独占性的唤醒
shared_mutex的unique_lock和mutex的lock一样，而condition_variable的第一个参数必须是std::mutex，有无类似的？

[`<condition_variable_any>`](https://zh.cppreference.com/w/cpp/thread/condition_variable_any)，请查看示例

