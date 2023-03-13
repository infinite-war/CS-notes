## 锁

### 互斥锁
[cplusplus](https://cplusplus.com/reference/mutex/)

`<mutex>`

+ 定义：`std::mutex m;`
	+ 定义在类中通常：`mutable std::mutex m;`其中mutable即为可变的，因为对象可以是`const`，但是锁显然是要被修改的，这样特殊声明

+ 使用：
	```c++
	type function_name(...) {
		std::unique_lock<std::mutex> lck(m);  // 其中m为一个mutex类型的变量

		...
		lck.unlock();  // 显示解锁
		lck.lock();    // 显示上锁
	}
	```
	对象`lck`在构建时自动上锁，之后可通过方法`lock`或`unlock`显示上下锁

	+ 在Golang中有这样的写法：
		```go
		var lck sync.Mutex
		func foo() {
			lck.Lock()
			defer lck.Unlock()
		    // ...
		}
		```
		因为在函数中随时可能退出或者抛出异常，正常写法需要在每个地方都进行显示的开锁。  
		`defer`语句即在退出当前代码块（无论是退出还是抛出），都会解锁。  
		C++也有类似的
		```c++
		type function_name(...) {
			std::lock_guard<std::mutex> lck(m);  // m同上
			...
		}
		```
		这样即可实现同样的功能

	我们发现unique_lock有更自由的功能，但是lock_guard有更简单的写法，同时前者实际上有更高的时空消耗

#### 锁的唤醒
如果我们想因为某种条件上锁，并在某些条件下解锁怎们办呢？
[cplusplus](https://cplusplus.com/reference/condition_variable/condition_variable/)

`<condition_variable>`

+ 变量定义：`std::condition_variable cv;`
+ 核心方法：
	```c++
	template <class Predicate>  void wait (unique_lock<mutex>& lck, Predicate pred);
	```
	其中Predicate是一个可调用对象，比如一个返回值是bool的函数或者Lambda表达式

+ 使用：
	```c++
	cv.wait(lck, ...);
	```
	+ 唤醒：
		1. `cv.notify_one();`
		2. `cv.notify_all();`

### 读写锁
我们想象这样的场景，就是对同一个临界资源，有多个线程要访问，实际上很多都是读，少数是写，显然这些读的线程不应该被阻塞，让它们自由的访问临界资源没有什么不妥，但是std::mutex显然会连它们都阻塞掉，有无方法避免？
`<shared_mutex>`

用法和mutex类似，但是没有自动解锁的lock_guard，而是有“两个上锁级别”：shared和exclusive，我们来看cpluscplus的例子
```c++
class ThreadSafeCounter {
 public:
  ThreadSafeCounter() = default;
 
  // Multiple threads/readers can read the counter's value at the same time.
  unsigned int get() const {
    std::shared_lock lock(mutex_);
    return value_;
  }
 
  // Only one thread/writer can increment/write the counter's value.
  void increment() {
    std::unique_lock lock(mutex_);
    ++value_;
  }
 
  // Only one thread/writer can reset/write the counter's value.
  void reset() {
    std::unique_lock lock(mutex_);
    value_ = 0;
  }
 
 private:
  mutable std::shared_mutex mutex_;
  unsigned int value_ = 0;
};
```

使用`shared_lock`不会被相互阻塞，只有使用`unique_lock`才会被阻塞。