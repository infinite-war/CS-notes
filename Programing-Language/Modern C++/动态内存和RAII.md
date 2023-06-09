[Dynamic memory management](https://en.cppreference.com/w/cpp/memory)

## raw ptr: new&delete

[new](https://en.cppreference.com/w/cpp/keyword/new)和[delete](https://en.cppreference.com/w/cpp/keyword/delete)：正如ref所说，这两个关键字既是expression又是function

## Smart pointers

+ [unique_ptr](https://en.cppreference.com/w/cpp/memory/unique_ptr)
+ [shared_ptr](https://en.cppreference.com/w/cpp/memory/shared_ptr)
	+ [weak_ptr](https://en.cppreference.com/w/cpp/memory/weak_ptr) 

+ zcl：
	+ unique_ptr相比于raw ptr不会有任何性能损失

## Allocator