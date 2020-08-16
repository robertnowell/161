from graph import Node as _node
class Node(_node):
	def __init__(self, index, parent=None, size=0):
		self.index = index
		self.parent = parent
		self.size = size
		self.data = index
		super().__init__(index)

	def __repr__(self):
		return "Node (index: {}), (parent: {}), (size: {})\n".format(self.index, self.parent, self.size)

class UnionFind():
	def __init__(self, forest):
		self.forest = forest

	def find(self, i):
		node = self.forest[i]
		parent = node.parent
		while parent != node.index:
			node = self.forest[parent]
			parent = self.forest[parent].parent
		return node.index

	def union(self, i, j):
		rooti = self.find(i)
		rootj = self.find(j)
		if rooti == rootj:
			return
		if self.forest[rooti].size > self.forest[rootj].size:
			self.forest[rootj].parent = rooti
			self.forest[rooti].size += self.forest[rootj].size
		else:
			self.forest[rooti].parent = rootj
			self.forest[rootj].size += self.forest[rooti].size

	def __repr__(self):
		return ",".join([str(node) for node in self.forest])

if __name__ == '__main__':
	forest = []
	for i in range(10):
		forest.append(Node(i, i, 1))
	uf = UnionFind(forest)
	print(uf.find(5))
	uf.union(5, 6)
	print(uf.find(6))
	print(uf.find(5))
	uf.union(5, 3)
	print(uf.find(6))
	print(uf.find(5))
	print(uf.find(3))
	print(uf)
	