## blocking mode and nonblocking mode

对于非阻塞的IO，代码并没有获得期望的数据，只有当前调用的状态，要轮询判断是否完成
1. 重复调用：笨笨
2. select：将调用状态关联到一个数组上，然后轮询数组check状态，数量有限
3. poll：将调用状态关联到一个链表上，然后轮询链表check状态，性能低下
4. epoll：自然回调，当事件完成唤醒