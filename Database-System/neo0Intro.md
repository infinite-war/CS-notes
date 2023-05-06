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
