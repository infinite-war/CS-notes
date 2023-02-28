# Intro
项目[地址](https://github.com/opencurve/curve)
# Use
## Deploy-CurveAdm
Curve的[doc](https://github.com/opencurve/curve/blob/master/README_cn.md)中的一节[快速体验](https://github.com/opencurve/curve/blob/master/README_cn.md#curvebs-%E5%BF%AB%E9%80%9F%E4%BD%93%E9%AA%8C)：部署和管理Curve的工具CurveAdm（[project](https://github.com/opencurve/curveadm)、[wiki](https://github.com/opencurve/curveadm/wiki)）
# Develop
## Compile
[guide](https://github.com/opencurve/curve/blob/869d29972bf677fef4f745c1d14be419376f1bce/docs/cn/build_and_run.md)
## Develop-tool-v2
>旧工具：[code](https://github.com/opencurve/curve/tree/master/src/tools)、[use-guide](https://github.com/opencurve/curve/blob/master/docs/cn/curve_ops_tool.md)  

+ 新工具：[code](https://github.com/opencurve/curve/tree/master/tools-v2)、[develop-guide](https://github.com/opencurve/curve/blob/master/tools-v2/docs/zh/develop.md)
+ 新工具开发进度：较于旧工具的[差别](https://github.com/opencurve/curve/tree/master/tools-v2#curve-bs)



urve bs delete peer 127.0.0.1:8200:0 --logicalpoolid=1 --copysetid=10001 --peers=127.0.0.1:8200:0,127.0.0.1:8201:1,127.0.0.1:8202:2 --rpcretrytimes=1 --rpctimeout=10s