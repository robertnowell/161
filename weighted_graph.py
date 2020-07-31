from graph import Node, Graph
from collections import deque

class WeightedGraph(Graph):
	def __init__(self, nodes, edges, weights):
	    super().__init__(nodes, edges)
	    self.weights = weights

	def get_edge_weight(self, s, t):
		key = frozenset(set([s, t]))
		return self.weights[key]

	def canDeliver(self, s, t, weight):
		self.visited = set()
		start = self.nodes[s]
		target = self.nodes[t]
		q = deque()
		q.append(start)
		while(len(q) > 0):
			n = q.popleft()
			self.visited.add(n)
			# print(q)
			# print(n)
			# print(target)
			if n == target:
				return True
			for neighbor in self.edges[n.data]:
				neighbornode = self.nodes[neighbor]
				if (neighbornode not in self.visited
						and self.get_edge_weight(n.data, neighbornode.data) >= weight):
					q.append(neighbornode)
		return False

	# def maxSupportedWeight(self, s, t):
	# 	# sort weights list
	# 	# binary search on weights list for max canDeliver weight between s and t
	# 	global weightsList
	# 	weightsList = sorted(weightsList)
	# 	low = 0
	# 	high = len(weightsList)-1
	# 	while low<high:
	# 		mid = (low+high)//2
	# 		if not self.canDeliver(s, t, weightsList[mid]):
	# 			high = mid-1
	# 		else:
	# 			low = mid+1
	# 	mid = (low + high)//2
	# 	if self.canDeliver(s, t, weightsList[mid]):
	# 		return weightsList[mid]
	# 	else:
	# 		return weightsList[mid-1]

	def maxSupportedWeight(self, s, t):
		# sort weights list
		# binary search on weights list for max canDeliver weight between s and t
		global weightsList
		weightsList = sorted(weightsList)
		low = 0
		high = len(weightsList)-1
		while low<=high:
			mid = (low+high)//2
			if self.canDeliver(s, t, weightsList[mid]):
				x = weightsList[mid]
				low = mid+1
			else:
				high = mid-1
		return x

	def getMinEdge(self):
		minScore = None
		minEdge = None
		for edge in self.edgeList:
			tail, head = edge
			tailnode = self.nodes[tail]
			headnode = self.nodes[head]
			if tailnode in self.visited and headnode not in self.visited:
				score = tailnode.distance + self.get_edge_weight(tail, head)
				if  minScore is None or score < minScore:
					minScore = score
					minEdge = (tail, head)
		return minEdge

	"""
	keep track of which vertices are in x by associated a boolean variable with each vertex
	each iteration, exhaustively search all edges
		compute dijkstra score for each edge with tail in x and head outside x
		return crossing edge with smallest score
	"""
	def dijkstra(self, s):
		self.edgeList = []
		for node in self.edges:
			for neighbor in self.edges[node]:
				self.edgeList.append([node, neighbor])
		print(self.edgeList)
		self.visited = set()
		self.visited.add(self.nodes[s])
		for node in self.nodes:
			node.distance = 0 if node.data == s else 1000000
		import pdb; pdb.set_trace()
		while True:
			res = self.getMinEdge()
			if res is None:
				break
			v, w = res
			self.visited.add(self.nodes[w])
			self.nodes[w].distance = self.nodes[v].distance + self.get_edge_weight(v, w)

nodes = []
for i in range(5):
	nodes.append(Node(i))

edges = {
	0: [1, 2, 3, 4],
	1: [0, 4],
	2: [0, 3],
	3: [0, 2],
	4: [0, 1],
}

global weightsList

weights = {
	frozenset(set([0, 1])): 30,
	frozenset(set([0, 2])): 10,
	frozenset(set([0, 3])): 8,
	frozenset(set([0, 4])): 6,
	frozenset(set([1, 4])): 12,
	frozenset(set([2, 3])): 15,
}

weightset = set()
for node in edges:
	for neighbor in edges[node]:
		weightset.add(weights[frozenset(set([node, neighbor]))])
weightsList = sorted(list(weightset))

if __name__ == '__main__':
	g = WeightedGraph(nodes, edges, weights)
	g.dijkstra(0)
	for node in g.nodes:
		print(node, node.distance)
	# print (g.maxSupportedWeight(3, 4))
	# print (g.maxSupportedWeight(0, 1))
	# print (g.maxSupportedWeight(3, 1))
	# print (g.canDeliver(1, 0, 15))
