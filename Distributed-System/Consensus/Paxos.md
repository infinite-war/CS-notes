在Raft之前，Paxos几乎是一致性算法的代名词
+ 但是它有两个严重缺点
	+ 很难准确理解，即使是对专业研究者和领域教授
	+ 很难正确实现。复杂加上某些理论描述模糊

Raft于2013年诞生，有更强的可理解性，经过证明且更强的一致性，效率和其他算法相当

Paxos其正确性是得到证明的，且一般情况下也高效，且其本身是点对点模型，最后为了性能考虑建建议弱领导力的模型，但是在实际应用中通常是中心式的才够高效。所以There are significant gaps between the description of the Paxos algorithm and the needs of a real-world system. . . . the final system will be based on an **un-proven** protoco
