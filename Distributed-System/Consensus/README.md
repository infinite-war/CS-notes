Consensus Algorithm译为共识算法或者一致性协议甚至一致性算法，在我的笔记中不做明确区分

+ **ELP不可能定理**：No completely asynchronous consensus protocol can tolerate even a single unannounced process death  
	>该定理来自Fisher、Lynch 和 Paterson的[论文](https://ilyasergey.net/CS6213/_static/02-consensus/flp.pdf)

	但是**科学告诉你，什么是不可能的；工程则告诉你，付出一些代码，可以把它变成可行**，这就是工程的魅力。