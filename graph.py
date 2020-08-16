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
		self.depth = 0
		self.path = []
		self.deleted = False

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
		self.maxDepth = 0
		self.maxPath = []

	def get_neighbors(self, node):
		neighbors = [ self.nodes[neighbor] for neighbor in self.edges[node.data] ]
		return neighbors

	def delete_neighbors(self, node):
		i = 0
		while i < len(self.edges[node.data]):
			neighbor = self.edges[node.data][i]
			neighboredges = self.edges[neighbor]
			j = 0
			while j < len(neighboredges):
				n = neighboredges[j]
				if n == node.data:
					del self.edges[neighbor][j]
				else:
					j += 1
			del self.edges[node.data][i]

	def delete_node(self, node):
		node.deleted = True

	# def kosaraju(self):
	# 	print( self.edges)
	# 	self._reverseEdges()
	# 	print( self.edges)
	# 	self.toposort()
	# 	self.visited = set()
	# 	print(([n.label for n in self.labeled]))
	# 	print( self.edges)
	# 	for node in self.labeled:
	# 		if node not in self.visited:
	# 			self.numscc = self.numscc+1
	# 			self._dfs_scc(node)
	# 	for n in self.nodes:
	# 		print((n.scc))

	def kosaraju(self):
		self._reverseEdges()
		print( self.edges)

		print( self.edges)
		self.toposort()
		self.visited = set()
		print(([n.label for n in self.labeled]))
		print( self.edges)
		# self._reverseEdges()
		# print( self.edges)
		for node in self.labeled:
			if node not in self.visited:
				self.numscc = self.numscc+1
				self._dfs_scc(node)
		for n in self.nodes:
			print((n.scc))

	def toposort(self):
		self.visited = set()
		self.label = len(self.nodes)
		for node in self.nodes:
			if node not in self.visited:
				self._dfsTopo(node)

	def _dfsTopo(self, node):
		self.visited.add(node)
		for neighbor in self.edges[node.data]:
			neighbornode = self.nodes[neighbor]
			if neighbornode not in self.visited:
				print(("traversing edge {},{}".format(node.data, neighbornode.data)))
				self._dfsTopo(neighbornode)
		node.label = self.label
		self.label -= 1
		self.labeled.append(node)

	def _dfs_scc(self, node):
		self.visited.add(node)
		node.scc = self.numscc
		for neighbor in self.edges[node.data]:
			neighbornode = self.nodes[neighbor]
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
			# print( self.visited)
			# print( n)
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
					neighbornode = self.nodes[neighbor]
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
				neighbornode = self.nodes[neighbor]
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

	def longestPathDFS(self, n):
		# if n not in self.visited:
		# import pdb; pdb.set_trace()
		# self.visited.add(n)
		if n.depth > self.maxDepth:
			self.maxDepth = n.depth
			self.maxPath = n.path
		for neighbor in self.edges[n.data]:
			neighbornode = self.nodes[neighbor]
			neighbornode.depth = n.depth + 1
			neighbornode.path = n.path + [neighbornode]
			self.longestPathDFS(neighbornode)

	def longestPath(self):
		self.visited = set()
		self.toposort()
		maxLabelNode = None
		for node in self.nodes:
			if maxLabelNode is None or node.label < maxLabelNode.label:
				maxLabelNode = node
		self.visited = set()
		self.longestPathDFS(maxLabelNode)
		print( self.maxPath)
		print( self.maxDepth)

	def dpLongestPath(self):
		# import pdb; pdb.set_trace()
		memo = [0]*len(self.nodes)
		self.visited = set()
		self.toposort()
		print( [ (node, node.label) for node in self.labeled])
		memo[0] = 1
		for i in range(1,len(self.labeled)):
			node = self.labeled[i]
			for j in range(0,i):
				othernode = self.labeled[j]
				import pdb; pdb.set_trace()
				if othernode.data in self.edges[node.data]:
					if 1+memo[j] > memo[i]:
						memo[i] = 1 + memo[j]
		print(memo)

def createGraph1():
	nodes = []
	for i in range(1, 12):
		nodes.append(Node(i-1))

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
	for i in range(11):
		edges[i] = edges[i+1]
	edges[11] = []

	return Graph(nodes, edges)

def createGraph2():
	nodes = []
	for i in range(1, 11):
		nodes.append(Node(i-1))

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
	for i in range(11):
		edges[i] = edges[i+1]
	edges[11] = []

	return Graph(nodes, edges)

def createBipartite():
	nodes = []
	for i in range(6):
		nodes.append(Node(i))

	edges = {
		0: [1, 3],
		1: [2, 0],
		2: [1, 3],
		3: [0, 4],
		4: [1, 5],
		5: [2],
	}
	for i in range(6):
		edges[i] = edges[i]
	return Graph(nodes, edges)

def alsoCreateNotBipartite():
	nodes = []
	for i in range(1, 13):
		nodes.append(Node(i-1))

	edges = {
		1: [2, 4],
		2: [3, 1],
		3: [2, 4],
		4: [1, 5],
		5: [2, 6],
		6: [3, 2],
	}
	for i in range(6):
		edges[i] = edges[i+1]
	edges[6] = []
	return Graph(nodes, edges)

def createNotBipartite():
	nodes = []
	for i in range(1, 13):
		nodes.append(Node(i-1))

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
	for i in range(6):
		edges[i] = edges[i+1]
	edges[6] = []
	return Graph(nodes, edges)

if __name__ == '__main__':
	# g = createGraph1()
	# g.toposort()
	# print(([n.label for n in g.nodes]))
	# g = createNotBipartite()
	# g = alsoCreateNotBipartite()
	g = createBipartite()
	print(g.edges)
	print(g.get_neighors(g.nodes[1]))
	g.delete_neighbors(g.nodes[0])
	print(g.edges)
	print(g.get_neighors(g.nodes[1]))
	# print( g.testBiPartnessDFS())
	# print( g.testBiPartnessBFS())
	# g.dpLongestPath()
