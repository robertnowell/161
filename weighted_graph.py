from graph import Graph
from collections import deque
from union_find import UnionFind, Node
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

	def getMinEdgeDijkstra(self):
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

	def assign_edge_list(self):
		self.edgeList = []
		for node in self.edges:
			for neighbor in self.edges[node]:
				self.edgeList.append([node, neighbor])

	"""
	keep track of which vertices are in x by associated a boolean variable with each vertex
	each iteration, exhaustively search all edges
		compute dijkstra score for each edge with tail in x and head outside x
		return crossing edge with smallest score
	"""
	def dijkstra(self, s):
		self.assign_edge_list()
		print(self.edgeList)
		self.visited = set()
		self.visited.add(self.nodes[s])
		for node in self.nodes:
			node.distance = 0 if node.data == s else 1000000
		import pdb; pdb.set_trace()
		while True:
			res = self.getMinEdgeDijkstra()
			if res is None:
				break
			v, w = res
			self.visited.add(self.nodes[w])
			self.nodes[w].distance = self.nodes[v].distance + self.get_edge_weight(v, w)

	def getMinEdgePrim(self):
		minScore = None
		minEdge = None
		for edge in self.edgeList:
			tail, head = edge
			tailnode = self.nodes[tail]
			headnode = self.nodes[head]
			if tailnode in self.visited and headnode not in self.visited:
				score = self.get_edge_weight(tail, head)
				if  minScore is None or score < minScore:
					minScore = score
					minEdge = (tail, head)
		return minEdge

	def prims(self, i=0):
		self.assign_edge_list()
		self.visited = set()
		tree_nodes = set()
		tree_edges = {}
		node  = self.nodes[i]
		self.visited.add(node)
		tree_edges[node.data] = []
		tree_nodes.add(node)
		while True:
			minEdge = self.getMinEdgePrim()
			if minEdge is None:
				return (tree_nodes, tree_edges)
			tail, head = minEdge
			tailnode = self.nodes[tail]
			headnode = self.nodes[head]
			print("choosing edge: {}, {}".format(tail, head))

			self.visited.add(headnode)
			tree_nodes.add(headnode)
			tree_edges[tailnode.data].append(headnode.data)
			tree_edges[headnode.data] = []

	def assign_sorted_weights(self):
		weightset = set()
		for node in self.edges:
			for neighbor in self.edges[node]:
				weightset.add(self.weights[frozenset(set([node, neighbor]))])
		weightsList = sorted(list(weightset))
		self.sorted_weights = weightsList

	def get_edges_by_weight(self, w):
		w_edges = []
		for edge in self.edgeList:
			tail, head = edge
			if self.get_edge_weight(tail, head) == w:
				w_edges.append(edge)
		return w_edges

	def kruskal(self):
		self.assign_edge_list()
		self.assign_sorted_weights()
		tree_nodes = set()
		tree_edges = { node.data: [] for node in self.nodes }
		al = []
		for node in self.nodes:
			al.append(Node(node.data, node.data, 1))
		uf = UnionFind(al)
		import pdb; pdb.set_trace()
		for w in self.sorted_weights:
			w_edges = self.get_edges_by_weight(w)
			for e in w_edges:
				head, tail = e
				# print(tail, head)
				if uf.find(tail) != uf.find(head):
					tailnode = self.nodes[tail]
					headnode = self.nodes[head]
					print("choosing edge: {}, {}".format(tail, head))
					tree_nodes.add(tailnode)				
					tree_nodes.add(headnode)				
					tree_edges[tail].append(head)
					# tree_edges[head].append(tail)
					uf.union(tail, head)
		return tree_nodes, tree_edges

def dijkstra_example():
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
	g = WeightedGraph(nodes, edges, weights)
	g.dijkstra(0)
	for node in g.nodes:
		print(node, node.distance)

def prim_example1():
	nodes = []
	for i in range(4):
		nodes.append(Node(i))

	edges = {
		0: [1, 2, 3],
		1: [0, 3],
		2: [0, 3],
		3: [0, 1, 2],
	}

	global weightsList

	weights = {
		frozenset(set([0, 1])): 1,
		frozenset(set([0, 2])): 4,
		frozenset(set([0, 3])): 3,
		frozenset(set([1, 3])): 2,
		frozenset(set([2, 3])): 5,
	}

	weightset = set()
	for node in edges:
		for neighbor in edges[node]:
			weightset.add(weights[frozenset(set([node, neighbor]))])
	weightsList = sorted(list(weightset))

	g = WeightedGraph(nodes, edges, weights)
	print(g.prims())
	# for node in g.nodes:
	# 	print(node, node.distance)


def prim_example2():
	nodes = []
	for i in range(9):
		nodes.append(Node(i))

# a 0
# b 1
# c 2
# d 3
# e 4
# f 5
# g 6
# h 7
# i 8

	edges = {
		0: [1, 7],
		1: [0, 2, 7],
		2: [1, 3, 5, 8],
		3: [2, 4, 5],
		4: [3, 5],
		5: [2, 3, 4, 6],
		6: [5, 7, 8],
		7: [0, 1, 6, 8],
		8: [2, 6, 7],
	}

	global weightsList

	weights = {
		frozenset(set([0, 1])): 4,
		frozenset(set([0, 7])): 8,
		frozenset(set([1, 2])): 8,
		frozenset(set([1, 7])): 11,
		frozenset(set([2, 3])): 7,
		frozenset(set([2, 5])): 4,
		frozenset(set([3, 4])): 9,
		frozenset(set([3, 5])): 14,
		frozenset(set([4, 5])): 10,
		frozenset(set([6, 5])): 2,
		frozenset(set([6, 7])): 1,
		frozenset(set([8, 2])): 2,
		frozenset(set([8, 6])): 6,
		frozenset(set([8, 7])): 7,
	}

	weightset = set()
	for node in edges:
		for neighbor in edges[node]:
			weightset.add(weights[frozenset(set([node, neighbor]))])
	weightsList = sorted(list(weightset))

	g = WeightedGraph(nodes, edges, weights)
	nodes, edges = g.prims()
	weightset = set()
	for node in edges:
		for neighbor in edges[node]:
			weightset.add(weights[frozenset(set([node, neighbor]))])
	weightsList = sorted(list(weightset))
	import pdb; pdb.set_trace()
	s = 0
	for edge in edges:
		for neighbor in edges[edge]:
			tail = edge
			head = neighbor
			w = g.get_edge_weight(tail, head)
			s += w
			print(tail, head, w)
	print(s)
	# for node in g.nodes:
	# 	print(node, node.distance)


def prim_example_hw6():
	nodes = []
	for i in range(6):
		nodes.append(Node(i))

# a 0
# b 1
# c 2
# d 3
# e 4
# f 5

	edges = {
		0: [1, 3, 5],
		1: [0, 2, 3, 5],
		2: [1, 5],
		3: [0, 1, 4],
		4: [3, 5],
		5: [0, 1, 2, 4],
	}

	global weightsList

	weights = {
		frozenset(set([0, 1])): 2,
		frozenset(set([0, 3])): 1,
		frozenset(set([0, 5])): 7,
		frozenset(set([1, 2])): 9,
		frozenset(set([1, 3])): 7,
		frozenset(set([1, 5])): 8,
		frozenset(set([2, 5])): 5,
		frozenset(set([3, 4])): 3,
		frozenset(set([4, 5])): 6,
	}


	weightset = set()
	for node in edges:
		for neighbor in edges[node]:
			weightset.add(weights[frozenset(set([node, neighbor]))])
	weightsList = sorted(list(weightset))

	g = WeightedGraph(nodes, edges, weights)
	nodes, edges = g.prims(2)
	weightset = set()
	for node in edges:
		for neighbor in edges[node]:
			weightset.add(weights[frozenset(set([node, neighbor]))])
	weightsList = sorted(list(weightset))
	import pdb; pdb.set_trace()
	s = 0
	for edge in edges:
		for neighbor in edges[edge]:
			tail = edge
			head = neighbor
			w = g.get_edge_weight(tail, head)
			s += w
			print(tail, head, w)
	print(s)
	# for node in g.nodes:
	# 	print(node, node.distance)


def kruskal_example():
	nodes = []
	for i in range(9):
		nodes.append(Node(i))

# a 0
# b 1
# c 2
# d 3
# e 4
# f 5
# g 6
# h 7
# i 8

	edges = {
		0: [1, 7],
		1: [0, 2, 7],
		2: [1, 3, 5, 8],
		3: [2, 4, 5],
		4: [3, 5],
		5: [2, 3, 4, 6],
		6: [5, 7, 8],
		7: [0, 1, 6, 8],
		8: [2, 6, 7],
	}

	global weightsList

	weights = {
		frozenset(set([0, 1])): 4,
		frozenset(set([0, 7])): 8,
		frozenset(set([1, 2])): 8,
		frozenset(set([1, 7])): 11,
		frozenset(set([2, 3])): 7,
		frozenset(set([2, 5])): 4,
		frozenset(set([3, 4])): 9,
		frozenset(set([3, 5])): 14,
		frozenset(set([4, 5])): 10,
		frozenset(set([6, 5])): 2,
		frozenset(set([6, 7])): 1,
		frozenset(set([8, 2])): 2,
		frozenset(set([8, 6])): 6,
		frozenset(set([8, 7])): 7,
	}

	weightset = set()
	for node in edges:
		for neighbor in edges[node]:
			weightset.add(weights[frozenset(set([node, neighbor]))])
	weightsList = sorted(list(weightset))

	g = WeightedGraph(nodes, edges, weights)
	nodes, edges = g.kruskal()
	weightset = set()
	for node in edges:
		for neighbor in edges[node]:
			weightset.add(weights[frozenset(set([node, neighbor]))])
	weightsList = sorted(list(weightset))
	s = 0
	for edge in edges:
		for neighbor in edges[edge]:
			tail = edge
			head = neighbor
			w = g.get_edge_weight(tail, head)
			s += w
			print(tail, head, w)
	print(s)
	# for node in g.nodes:
	# 	print(node, node.distance)


def kruskal_example_hw6():
	nodes = []
	for i in range(6):
		nodes.append(Node(i))

# a 0
# b 1
# c 2
# d 3
# e 4
# f 5

	edges = {
		0: [1, 3, 5],
		1: [0, 2, 3, 5],
		2: [1, 5],
		3: [0, 1, 4],
		4: [3, 5],
		5: [0, 1, 2, 4],
	}

	global weightsList

	weights = {
		frozenset(set([0, 1])): 2,
		frozenset(set([0, 3])): 1,
		frozenset(set([0, 5])): 7,
		frozenset(set([1, 2])): 9,
		frozenset(set([1, 3])): 7,
		frozenset(set([1, 5])): 8,
		frozenset(set([2, 5])): 5,
		frozenset(set([3, 4])): 3,
		frozenset(set([4, 5])): 6,
	}

	weightset = set()
	for node in edges:
		for neighbor in edges[node]:
			weightset.add(weights[frozenset(set([node, neighbor]))])
	weightsList = sorted(list(weightset))

	g = WeightedGraph(nodes, edges, weights)
	nodes, edges = g.kruskal()
	weightset = set()
	for node in edges:
		for neighbor in edges[node]:
			weightset.add(weights[frozenset(set([node, neighbor]))])
	weightsList = sorted(list(weightset))
	s = 0
	for edge in edges:
		for neighbor in edges[edge]:
			tail = edge
			head = neighbor
			w = g.get_edge_weight(tail, head)
			s += w
			print(tail, head, w)
	print(s)
	# for node in g.nodes:
	# 	print(node, node.distance)

if __name__ == '__main__':
	prim_example_hw6()
	kruskal_example_hw6()