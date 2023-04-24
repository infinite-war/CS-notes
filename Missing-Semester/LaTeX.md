>摸索中

+ overleaf是一个比较好用的在线LaTeX编辑器
+ 一些资源：
	+ [编辑器和编程器教程](https://zhuanlan.zhihu.com/p/508823527)
	+ [支持中文教程](https://jingyan.baidu.com/article/ff411625e229d512e482379c.html)

+ 使用Scoop可以方便的搭建差不多的LaTeX环境
	```bash
	scoop bucket add scoopet https://github.com/ivaquero/scoopet
	scoop install texlive  # 下载实践略久
	```

## Tikz
>以下记录是经验性质的，不是系统的教程

+ 环境：Obsidian的tikzjax插件
+ 用法：

 
 
```



```
	

\\`\\`\\`tikz








	```


obsidian-tikzjax

```tikz
\begin{document}

\begin{tikzpicture}
  \foreach \i in {1,...,4} {
    \draw (\i,0) rectangle (\i+1,1) node[midway] {\i};
  }
  \draw (0.5,0.5) node {$\cdots$};
  \draw (5.5,0.5) node {$\cdots$};
\end{tikzpicture}


\end{document}
```
