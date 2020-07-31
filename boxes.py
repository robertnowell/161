from graph import Node, Graph

#array of tuples (w, h)
def longestChain(boxes):
	nodes = []
	for i in range(len(boxes)):
		nodes.append(Node(i))		
	edges = {}
	for i in range(len(boxes)):
		box = boxes[i]
		n = nodes[i]
		edges[i] = []
		for j in range(len(boxes)):
			other = boxes[j]
			if box[0] > other[0] and box[1] > other[1]:
				edges[i].append(j)
	print(nodes, edges)
	g = Graph(nodes, edges)
	g.dpLongestPath()

if __name__ == '__main__':
	boxes = [(100, 100), (1000, 1000), (500, 500)]
	longestChain(boxes)