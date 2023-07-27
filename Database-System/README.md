+ [DB Rank](https://db-engines.com/en/ranking)（mybe class）

+ 15445
	+ 学习资料
		+ 讲课：B站Moody-老师

# DB

数据库在理论和实践上都有大量的讨论，所以笔记中会交织概念、理论、构建和使用，请见怪不怪

+ Data：数据
+ DB, DataBase：数据库
+ DBMS, Database Management System

--

+ data model
+ schema

--

+ data model：    
	SQL
	+ relational
	
	--  
	noSQL
	+ kv
	+ graph
	+ document
	+ column-family
	
	--
	+ else

## relational model

+ table：table is relational, relational is table
+ tuple: a row in table
	+ value: must 标量

--

+ primary key主键：用来唯一确定一个table中的tuple

+ primary key主键：唯一确定一个tuple
+ foreign key外键：关联表的关系

--

+ DML, Data mainipulation languages：增删改查
+ DDL, Data Definition Language：修改数据库的数据结构

--

+ DML：
	+ Procedural：带过程的DML——relational algebra关系代数
	+ No-Procedural/Decalarative：不带过程的——relational calculus

## relational algebra
通过关系代数去查询数据是会影响处理过程的，而数据库model和查询语言实现是解耦的

$$
\begin{aligned}
\sigma  &\ Select       &\ 选择  \newline
\Pi     &\ Projection   &\ 投影  \newline
\cup    &\ Union        &\ 联合 \newline
\cap    &\ Intersection &\  \newline
-      &\ Difference   &\  \newline
\times  &\ Product      &\  \newline
\bowtie &\ Join         &\  \newline
\newline
其他
\newline
\newline
\vee    &\ and          &\  \newline
\land   &\ or           &\  \newline
\end{aligned}
$$

+ Select: $\sigma_{predicate}(R)$, 按条件找行
	```sql
	SELECT * FROM R
	WHERE redicate
	```

+ Projection: $\Pi_{A1, A2, ..., An}(R)$, 映射，变化表，比如取出对应列或者对应列进行什么变化
	```sql
	SELECT A1, A2, ..., An
	FROM R
	```

+ Union: $R \cup S$, 合并表，相同列放一起
	```sql
	(SELECT * FROM R) UNION ALL (SELECT * FROM S)
	```

	+ `UNION`去重
	+ `UNION ALL`不去重

+ Intersectoin: $R \cap S$, 取交集，取出两个表中都有的列的都有的行
	```sql
	(SELECT * FROM R) INTERSECT (SELECT * FROM S)
	```

+ Difference: $R - S$, 取出两个表都有的列的前者有而后者没有的
	```sql
	(SELECT * FROM R) EXCEPT (SELECT * FROM S)
	```

+ Product: $R \times S$, 笛卡尔积，全列排列组合（不同表的同名列认为不同）
	```sql
	SELECT * FROM R CROSS JOIN S;
	SELECT * FROM R, S;
	```

+ Join: $R \bowtie S$, 关联
	```sql
	```


+ 从数据库是叫看用文件存储数据
	+ 直接写，不能并行（除非用锁保证顺序执行?）、不能容错，正在写寄了咋办？
	+ 先写进temp file，在重命名。可以并行，重命名是原子的，不能容错，重命名后的文件可能在Cache，Fail可能不能保存到硬盘
	+ 系统调用`fsync`：重命名前刷新data到disk

+ 关系型数据库的查询：
	+ whole
	+ 点查询
	+ Range查询

+ 数据结构选择：
	+ 哈希表（开放寻址）：表转移时的性能问题


+ Page/Block is a fixed-size block of data.
	+ contain tuples, meta-data, indexes, log records，且只包含一种
	+ 可能里面还有一个数据结构支出自己是什么类型
	+ 应该有唯一ID

+ 从内存角度对DB分类：
	+ Disk-oriented DBMS
	+ Memory-oriented DBMS

+ Disk-oriented DBMS数据库运行流程
	+ Disk：DataBase File
		+ Pages
			+ Directory
			+ Block
				+ Header
	+ Memory：Buffer Pool
		+ Pages
			+ Directory
			+ Block

	+ Execution Engine

+ mmap, memory mapping：Disk大，Physical Memory小，mmap提供Virtual Memory，和disk一样大，让软件直接访问虚拟内存，然后mmap把虚拟内存需要的东西从硬盘load的物理内存中，然后建立物理内存对应文件到虚拟内存中的链接。问题是上面的方案对只读没问题，但是对并发写怎么办呢？于是衍生出了很多东西madvice、mlock、msync

+ 数据库面临的问题：
	+ 对非易失性存储介质的随机access比顺序access慢得多，但是我们不能限制用户的行为，所以要尽可能的进行转换，最大化顺序access
	+ Flushing dirty pages to disk in the correct order脏数据什么时候存回去？
	+ Specialized prefetching预取问题
	+ Buffer replacement policy内存中的缓冲区的更换策略
	+ Thread/process scheduling并发调度

## How the DBMS represents the database in files on disk

### File Storage

+ storage manager：维护DB的file，有较于OS更适合DB的文件管理

+ 数据结构
	+ 第一个page里有两个链表的头结点
		+ free page list
		+ data page list

	+ 每个page就有两个指针服务于链表，然后其他就是data

	或者

+ directory目录


### Page Layout

### Tuple Layout


# 事务

+ 事务的引入：

  + 计算环境的脆弱性——故障恢复问题
  + 计算环境的分布性——并发控制问题

  > ```sql
  > read(X); -- 从数据库传送数据项X到事务的工作区中
  > write(X);-- 从事务的工作区中将数据项X写回数据库
  > X := X_; -- 赋值
  > ```

+ 事务的定义：由一系列操作序列构成的程序执行单元，要么都做、要么都不做，是一个不可分割的工作单位

  + 业务逻辑：两个或以上业务必须同时完成，或者同时失败
  + 技术逻辑：两个或以上写操作，必须同时完成，或同时失败

+ 运行：

  + 事务串行执行，同一时刻只有一个事务运行
    + 单处理机并行事务轮流交叉运行
    + 多处理机同时并发执行

+ 特性(ACID)：

  1. 原子性(atomicity：

     事务中包含的所有操作要么全做，要么全不做；

     由**恢复机制**实现。

  2. 一致性(consistency)：

     事务的隔离执行必须保证数据库的一致性：事务开始前和结束后，数据库都处于一致性的状态；

     由**用户**负责，由**并发控制**实现

  3. 隔离性(isolation)：

     系统必须保证事务不受其他并发执事务的影响：

     通过**并发控制机制**实现

  4. 持久性(Durability)：

     一个事务一旦提交后，对数据库的影响必须是永久的；即使发生故障

     通过**恢复机制**实现

# SQL

+ 事务处理(transaction processing)：同来管理成批执行的SQL操作的机制
  + 事务(transaciton)：指一组SQL语句；
  + 回退(rollback)：指撤销指定SQL语句的过程：只能回退数据操作
  + 提交(commit)：指将为存储的SQL语句结果写入数据库表
  + 保留点(savepoint)：指事务处理设置的临时占位符(placeholder)，可对其发布回退

+ 标识事务处理块：

  ```sql
  BEGIN TRANSACTION -- begin
  START TRANSACTIOn -- start transaction
  ```

+ 回退：`ROOLBACK`命令

+ 提交：`COMMIT`命令：在事务中使用

  > 一般SQL语句都是直接对数据库执行和编写，即隐含提交(implicit commit)

+ 保留点：

  ```sql
  SAVEPOINT 保留点名;
  SAVE TRANSACTION 保留点名;
  ```

  + 回退：

    ```sql
    ROLLBACK TO 保留点名;
    ROLLBACK TRANSACTION 保留点名;
    ```

  + 检查：

    ```sql
    IF @@保留点名 <> 0 回退;
    ```

# 并发控制

> 问题引入：
>
> + 丢失修改：不同用户同时修改一个量，后提交的修改覆盖前一个的
> + 不可重复读：在一个用户连续读取一个量的间隙，另一个用户修改，量改变
> + 脏读：一个用户修改数据，另一个用户读取，但是第一个用户撤销了操作，则第二个用户读取到*脏数据*（被遗弃数据）

## 锁

+ 实现并发控制的重要技术

1. 基本锁
   + 读锁（共享锁，S锁）
   + 写锁（排他锁，X锁）

+ 锁协议：

  1. 一级封锁协议：事务在**修改**数据之前必须先加X锁，知道事务结束才释放
  2. 二级封锁协议：在一级封锁协议基础上，在读取数据之前先加S锁，**读完**后释放
  3. 三级封锁协议：在一级封锁协议之上，事务T在读取数据R之前必须先对其加S锁，直到**事务结束**才释放

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Database-System/封锁协议效果.png)

------

+ 饥饿：事务永远无法获得足够资源的情况
+ + 活锁：通过等待
  + 死锁：事务间无限相互等待的情况

+ 死锁预防：
  + 一次封锁：一次性对所有要使用的数据枷锁，否则不执行
  + 顺序封锁：规定数据的封锁顺序，任何事务必须按此顺序封锁
+ 死锁检测：
  + 超时法：等待时间超过阈值
  + 等待图法：有向图的环

## 调度

+ 可串行性：多个事务并发执行是正确的，当且仅当其结果与某次串行执行这些事务时的结果相同

一个并发调度当且仅当它是可串行化的，才是正确调度

+ 1. 串行调度：一个一个来
  2. 可串行化调度：交叉进行，但结果不会相互影响
  3. 不可串行化调度：交叉进行，但结果会相互影响——冲突操作
+ 冲突操作：不同事务对同一数据的读写和写写操作
+ 冲突可串行化：

## 其他锁

+ 封锁粒度：封锁对象的大小
  + 物理对象
  + 逻辑对象
+ 意向锁：
  + 意向共享锁
  + 意向排他锁
  + 共享意向排他锁
