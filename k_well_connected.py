from graph import Graph, Node

# want incoming and outgoing edges
# for each node, if has fewer than k edges
# delete node
# delete outgoing edges
# for each outgoing edge
# 	delete incoming edge
# 
def k_well_connected_subgraph(g, k):
	for node in g.nodes:
		modified_dfs(g, node, k)

def modified_dfs(g, node, k):
	g.visited.add(node)
	neighbors = g.get_neighbors(node)
	if len(neighbors) < k:
		g.delete_neighbors(node)
		g.delete_node(node)
		for neighbor in neighbors:
			modified_dfs(g, neighbor, k)
	else:
		for neighbor in neighbors:
			if neighbor not in g.visited:
				modified_dfs(g, neighbor, k)

def createBipartite():
	nodes = []
	for i in range(6):
		nodes.append(Node(i))

	edges = {
		0: [1, 3],
		1: [2, 0, 4],
		2: [1, 3],
		3: [0, 2],
		4: [1, 5],
		5: [2, 4],
	}
	for i in range(6):
		edges[i] = edges[i]
	return Graph(nodes, edges)

if __name__ == '__main__':
	g = createBipartite()
	k_well_connected_subgraph(g, 2)
	print(g.edges)
