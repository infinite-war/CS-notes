在Raft之前，Paxos几乎是一致性算法的代名词

+ 但是它有两个严重缺点
	+ 很难准确理解，即使是对专业研究者和领域教授
	+ 很难正确实现。复杂加上某些理论描述模糊
		+ Paxos本身是点对点模型，最后为了性能考虑建议弱领导力的模型，但是在实际应用中通常是中心式的才够高效，所以There are significant gaps between the description of the Paxos algorithm and the needs of a real-world system. . . . the final system will be based on an **un-proven** protocol
			>注意Paxos的正确性是得到了证明的，且一般情况下也高效

另一个更实际的困难是Paxos复杂难懂但是又没有其他适合教学的替代算法

因为从工业界和学术界需求出发，斯坦福大学博士生 Diego Ongaro 及其导师 John Ousterhout 提出了 Raft 算法（2013年），它的最大设计目标是可理解性understandability