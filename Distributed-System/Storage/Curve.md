+ 项目[地址](https://github.com/opencurve/curve)
	+ [中文README](https://github.com/opencurve/curve/blob/master/README_cn.md)

+ 提供两种服务：
	+ BS, block system：curvebs
	+ FS, file system：curvefs

# Use

## CurveAdm
用于deploy curve

+ 项目[地址](https://github.com/opencurve/curveadm)
	+ [wiki](https://github.com/opencurve/curveadm/wiki)

### Args

+ hosts
+ topology

### All-in-one
[tutor](https://github.com/opencurve/curve/blob/master/README_cn.md#curvebs-%E5%BF%AB%E9%80%9F%E4%BD%93%E9%AA%8C)

## tool
>旧工具：[code](https://github.com/opencurve/curve/tree/master/src/tools)、[use-guide](https://github.com/opencurve/curve/blob/master/docs/cn/curve_ops_tool.md)  

+ 新工具：[code](https://github.com/opencurve/curve/tree/master/tools-v2)、[develop-guide](https://github.com/opencurve/curve/blob/master/tools-v2/docs/zh/develop.md)
+ 新工具开发进度：较于旧工具的[差别](https://github.com/opencurve/curve/tree/master/tools-v2#curve-bs)

# Develop
## Compile
[guide](https://github.com/opencurve/curve/blob/869d29972bf677fef4f745c1d14be419376f1bce/docs/cn/build_and_run.md)

## playground
[guide](https://github.com/opencurve/curve/blob/master/tools-v2/docs/zh/develop.md#%E9%83%A8%E7%BD%B2-curve-%E9%9B%86%E7%BE%A4)

+ 锅：
	+ 执行`curveadm playground`部署playground报错，应使用`sudo $(which curveadm) playground run --kind curvebs`