class Node():
	def __init__(self, f, left=None, right=None):
		self.f = f
		self.left = left
		self.right = right

	def __repr__(self):
		return "Node {}\nleft:({}), right:({})\n".format(self.f, self.left, self.right)

def huffman(forest):
	for i in range(len(forest)-1):
		smallest = Node(float("inf"))
		secondSmallest = Node(float("inf"))
		for node in forest:
			# import pdb; pdb.set_trace()
			if node.f <= smallest.f:
				secondSmallest = smallest
				smallest = node
			elif node.f < secondSmallest.f:
				secondSmallest = node
		new = Node(smallest.f + secondSmallest.f)
		new.left = smallest
		new.right = secondSmallest
		forest.remove(smallest)
		forest.remove(secondSmallest)
		forest.add(new)
	print(forest)

if __name__ == '__main__':
	forest = set()
	for i in range(10):
		forest.add(Node(10-i))
	huffman(forest)
