from pprint import pprint

"""
	for each cell
		memo[i][j] = right(k-cell) + down(k-cell)

	if at final cell:
		if cell == k:
			return 1
		else:
			return 0

"""
def also_k_coins(g, k, i, j):
	print(i, j, k)
	n = len(g)
	m = len(g[0])
	# print(i, j)
	if i >= n or j >= m:
		return 0
	cell = g[i][j]
	if i == n-1 and j == m-1:
		if k == cell:
			return 1
		else:
			return 0
	right = also_k_coins(g, k-cell, i, j+1)
	left = also_k_coins(g, k-cell, i+1, j)
	return right + left
















"""
subproblems
	cell = g[i][j]
	memo[i][j] = pickup_k_coins(g, k, i+1, j, sofar+cell) + pickup_k_coins(g, k, i, j+1, sofar+cell)

"""
def pickup_k_coins(g, k, i, j, sofar, memo):
	# import pdb; pdb.set_trace()
	n = len(g)
	m = len(g[0])
	# print(i, j)
	if i >= n or j >= m:
		return 0
	elif memo[i][j][sofar] != -1:
		return memo[i][j][sofar]

	sofar += g[i][j]
	if sofar > k:
		return 0

	if i == n-1 and j == m-1:
		memo[i][j][sofar] = 1 if sofar == k else 0
	else:
		right = pickup_k_coins(g, k, i, j+1, sofar, memo)
		down = pickup_k_coins(g, k, i+1, j, sofar, memo)
		memo[i][j][sofar] = right + down
	return memo[i][j][sofar]

grid = [
	[3, 1, 2],
	[4, 0, 3],
	[0, 2, 1]
]
memo = []
for i in range(len(grid)):
	memo.append([])
	for j in range(len(grid[0])):
		memo[i].append([])
		for k in range(11):
			memo[i][j].append(-1)
# pprint(memo)
# print(pickup_k_coins(grid, 10, 0, 0, 0, memo))
# pprint(memo)

print(also_k_coins(grid, 10, 0, 0))
