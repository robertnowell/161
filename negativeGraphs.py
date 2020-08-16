from weighted_graph import WeightedGraph
from graph import Node
from pprint import pprint
class NegGraph(WeightedGraph):
	def __init__(self, nodes, edges, incoming, weights):
	    super().__init__(nodes, edges, weights)
	    self.incoming = incoming

	def get_edge_weight(self, s, t):
		key = frozenset(set([s, t]))
		return self.weights[key]

	def bellman_ford(self, source, minimum):
		sourceNode = self.nodes[source]
		n = len(self.nodes)
		default_value = float("inf") if minimum else -float("inf")
		memo = [ [default_value for i in range(n)] for i in range((n + 1)) ]
		for i in range(n):
			memo[0][i] = default_value if i != source else 0
		for i in range(n+1):
			memo[i][source] = 0
		pprint(memo)
		for k in range(1, n+1):
			for i in range(0, n):
				# i = index-1
				candidate = memo[k-1][i]
				for e in self.incoming[i]:
					weight = self.get_edge_weight(e, i)
					potential = memo[k-1][e] + weight
					if minimum == True and potential < candidate:
						candidate = memo[k-1][e] + weight
					elif minimum == False and potential > candidate:
						candidate = memo[k-1][e] + weight
				memo[k][i] = candidate
		if memo[-1] == memo[-2]:
			pprint(memo)
			return memo
		else:
			print("negative cycle")
			return None

		"""
		iterate 0 to n
			iterate through every node
				iterate through every incoming edge
					memo[k][i] = min(memo[k][i])
		min path weight sum from any incoming edge of length k or path weight sum using k-1
		"""

	# def find_max_distances(self, source):
	# 	n = len(self.nodes)
	# 	D = [-float("inf") for i in range(n)]
	# 	D[source] = 0
	# 	import pdb; pdb.set_trace()
	# 	for topoI in range(n):
	# 		node = self.labeled[topoI]
	# 		i = node.data
	# 		maximum = D[topoI]
	# 		for topoJ in range(topoI):
	# 			nodej = self.labeled[topoJ]
	# 			j = nodej.data
	# 			if j in self.incoming[i]:
	# 				candidate = D[topoJ] + self.get_edge_weight(i, j)
	# 				if candidate > maximum:
	# 					maximum = candidate
	# 		D[topoI] = maximum
	# 	return D


	def find_max_distances(self, source):
		n = len(self.nodes)
		D = [-float("inf") for i in range(n)]
		D[source] = 0
		import pdb; pdb.set_trace()
		for topoI in range(n):
			node = self.labeled[topoI]
			i = node.data
			maximum = D[topoI]
			for j in self.incoming[i]:
				nodeJ = self.nodes[j]
				topoJ = nodeJ.label-1
				if topoJ < topoI:
					candidate = D[topoJ] + self.get_edge_weight(i, j)
					if candidate > maximum:
						maximum = candidate
			D[topoI] = maximum
		return D

	def find_min_distances(self, source):
		return self.bellman_ford(source, True)

	# def find_max_distances(self, source):
	# 	return self.bellman_ford(source, False)

nodes = []
for i in range(5):
	nodes.append(Node(i))

# s 0
# t 1
# u 2
# v 3
# w 4

edges = {
	0: [2, 3],
	1: [],
	2: [3, 4],
	3: [1],
	4: [1],
}

incoming = {
	0: [],
	1: [3, 4],
	2: [0],
	3: [0, 2],
	4: [2],
}
global weightsList

weights = {
	frozenset(set([3, 1])): 4,
	frozenset(set([1, 4])): 2,
	frozenset(set([2, 0])): 2,
	frozenset(set([3, 0])): 4,
	frozenset(set([3, 2])): -1,
	frozenset(set([4, 2])): 2,
}

names = {
	0: 's',
	1: 't',
	2: 'u',
	3: 'v',
	4: 'w',
}

weightset = set()
for node in edges:
	for neighbor in edges[node]:
		weightset.add(weights[frozenset(set([node, neighbor]))])
weightsList = sorted(list(weightset))

if __name__ == '__main__':
	g = NegGraph(nodes, edges, incoming, weights)
	g.toposort()
	g.labeled = [i for i in reversed(g.labeled)]
	# print([ (names[n.data], n.data) for n in g.labeled ] )
	# g.find_min_distances(0)
	print(g.find_max_distances(0))
	# g.dijkstra(0)
	# for node in g.nodes:
	# 	print(node, node.distance)
	# print (g.maxSupportedWeight(3, 4))
	# print (g.maxSupportedWeight(0, 1))
	# print (g.maxSupportedWeight(3, 1))
	# print (g.canDeliver(1, 0, 15))
