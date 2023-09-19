>Googel开源的命令行框架

## Install

## Use

### include
```c++
#include <gflags/gflags.h>
```

### define
```c++
DEFINE_type(变量名, 默认值, 描述)
```
+ `type`：
	```
	bool
	int32
	int64
	uint64
	double
	string
	```

### use
+ `main`开始位置：
	```c++
	gflags::ParseCommandLineFlags(&argc, &argv, true);
	```

```c++
FLAGS_变量名
```

#### check
```c++
// 定义check函数
static bool NamedatePort(const char* flagname, type name) {
	//check
	//log
	return bool;
}
// 定义注册函数
DEFINE...;
static const bool port_name = gflags::RegisterFlagValidator(&FALGS_port, &NamedatePort);
```

### complier

`-lgflags`

### exec

1. `...exe -变量名=value`
2. file: `XXX.flags`:
	```
	--name=value
	....
	```
	`...exe --flagfile XXX.flags`

### extern
```c++
DECLARE_type(name); 
```
