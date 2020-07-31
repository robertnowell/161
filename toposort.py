from collections import deque
# define label = number of nodes
# perform dfs
# anytime we reach the end of a search, assign label and decrement
class Node():
	def __init__(self, data):
		self.data = data
		self.label = None
		self.scc = None
		self.color = None

	def __repr__(self):
		return "Node {}".format(self.data)

class Graph():
	def __init__(self, nodes, edges):
		self.nodes = nodes
		self.edges = edges
		self.visited = set()
		self.label = len(nodes)
		self.numscc = 0
		self.labeled = []

	def kosaraju(self):
		self._reverseEdges()
		print self.edges
		self.toposort()
		self.visited = set()
		print([n.label for n in self.labeled])
		for node in self.labeled:
			if node not in self.visited:
				self.numscc = self.numscc+1
				self._dfs_scc(node)
		for n in self.nodes:
			print(n.scc)

	def toposort(self):
		self.visited = set()
		self.label = len(self.nodes)
		for node in self.nodes:
			if node not in self.visited:
				self._dfsTopo(node)

	def _dfsTopo(self, node):
		self.visited.add(node)
		for neighbor in self.edges[node.data]:
			neighbornode = self.nodes[neighbor-1]
			if neighbornode not in self.visited:
				print("traversing edge {},{}".format(node.data, neighbornode.data))
				self._dfsTopo(neighbornode)
		node.label = self.label
		self.label -= 1
		self.labeled.append(node)

	def _dfs_scc(self, node):
		self.visited.add(node)
		node.scc = self.numscc
		for neighbor in self.edges[node.data]:
			neighbornode = self.nodes[neighbor -1]
			if neighbornode not in self.visited:
				self._dfs_scc(neighbornode)

	def _reverseEdges(self):
		revEdges = {}
		for node in self.nodes:
			revEdges[node.data] = []
		for k, elist in self.edges.items():
			for dest in elist:
				revEdges[dest].append(k)
		self.edges = revEdges

	def bipartiteBFS(self, q):
		while len(q) > 0:
			n = q.popleft()
			# print self.visited
			# print n
			if n == -1:
				self.color = 1 if self.color == 0 else 0
				if len(q) > 0:
					q.append(-1)
			elif n in self.visited:
				if self.color != n.color:
					return False
			else:
				n.color = self.color
				self.visited.add(n)
				for neighbor in self.edges[n.data]:
					neighbornode = self.nodes[neighbor-1]
					q.append(neighbornode)
		return True

	def bipartiteDFS(self, n, color):
		"""
			make sure every child node 
				has no color or opposite color of current node
				pass opposite color and recurse on child
		"""
		if n in self.visited:
			if n.color != color:
				return False
		else:
			self.visited.add(n)
			n.color = color
			oppositeColor = 1 if color == 0 else 0 
			for neighbor in self.edges[n.data]:
				neighbornode = self.nodes[neighbor-1]
				if not self.bipartiteDFS(neighbornode, oppositeColor):
					return False
		return True

	def testBiPartnessDFS(self):
		self.visited = set()
		return self.bipartiteDFS(self.nodes[0], 0)

	def testBiPartnessBFS(self):
		self.color = 0
		q = deque()
		self.visited = set()
		q.append(self.nodes[0])
		q.append(-1)
		return self.bipartiteBFS(q)

def createGraph1():
	nodes = []
	for i in range(1, 12):
		nodes.append(Node(i, i-1))

	edges = {
		1: [3],
		2: [4, 10],
		3: [5, 11],
		4: [7],
		5: [1, 7, 9],
		6: [10],
		7: [9],
		8: [6],
		9: [2, 4, 8],
		10: [8],
		11: [6, 8],
	}
	return Graph(nodes, edges)

def createGraph2():
	nodes = []
	for i in range(1, 11):
		nodes.append(Node(i, i-1))

	edges = {
		1: [2, 5, 3],
		2: [7],
		3: [10],
		4: [3],
		5: [],
		6: [4, 8],
		7: [8],
		8: [1, 9],
		9: [5, 7],
		10: [6],
	}
	return Graph(nodes, edges)

def createBipartite():
	nodes = []
	for i in range(1, 13):
		nodes.append(Node(i, i-1))

	edges = {
		1: [2, 4],
		2: [3, 1],
		3: [2, 4],
		4: [1, 5],
		5: [2, 6],
		6: [3],
	}
	return Graph(nodes, edges)

def alsoCreateNotBipartite():
	nodes = []
	for i in range(1, 13):
		nodes.append(Node(i, i-1))

	edges = {
		1: [2, 4],
		2: [3, 1],
		3: [2, 4],
		4: [1, 5],
		5: [2, 6],
		6: [3, 2],
	}
	return Graph(nodes, edges)

def createNotBipartite():
	nodes = []
	for i in range(1, 13):
		nodes.append(Node(i, i-1))

	edges = {
		1: [2, 4, 5],
		2: [1, 3, 5],
		3: [2],
		4: [1],
		5: [1, 7],
		6: [2, 8],
		7: [5, 8],
		8: [6, 7],
	}
	return Graph(nodes, edges)

if __name__ == '__main__':
	# g = createGraph1()
	# g.toposort()
	# print([n.label for n in g.nodes])
	# g = createNotBipartite()
	g = alsoCreateNotBipartite()
	# g = createBipartite()
	print g.testBiPartnessDFS()
	print g.testBiPartnessBFS()
