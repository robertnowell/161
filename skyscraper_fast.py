def tallest(g):
	# assume rows >= 1
	num_cols = len(g[0])
	max_height = 0
	tallest_col = -1
	j = 0 # first col
	i = len(g) - 1 # max row
	while(j < num_cols and i > 0):
		if g[i][j] == 0:
			i = go_to_top(g, i, j)
			max_height = len(g)-i
			tallest_col = j
		j += 1
	return tallest_col

def go_to_top(g, i, j):
	while (i >= 0 and g[i][j] == 0):
		i -= 1
	return i+1

grid = [
	[1, 1, 1, 0, 1],
	[1, 0, 1, 0, 1],
	[1, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0],
]

grid1 = [
	[1, 1, 1, 1, 1],
	[1, 0, 1, 1, 1],
	[1, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0],
]

grid2 = [
	[1, 1, 1, 1, 0],
	[1, 1, 1, 1, 0],
	[1, 1, 1, 1, 0],
	[1, 1, 1, 1, 0],
	[1, 1, 1, 1, 0],
	[1, 1, 1, 1, 0],
]

grid3 = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 0],
]

grid4 = [
	[0, 1, 1, 0, 1],
	[0, 0, 1, 0, 1],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0],
]
# print (find_height(grid, 0))
# for i in range(len(grid[0])):
# 	print(find_height(grid, i))

print('tallest:' + str(tallest(grid)))
print('tallest:' + str(tallest(grid1)))
print('tallest:' + str(tallest(grid2)))
print('tallest:' + str(tallest(grid3)))
print('tallest:' + str(tallest(grid4)))

# print is_top(grid, 0, 0)
# print is_top(grid, 1, 0)
# print is_top(grid, 2, 0)
# print is_top(grid, 3, 0)
# print is_top(grid, 4, 0)
# print is_top(grid, 5, 0)

# print is_top(grid, 0, 1)
# print is_top(grid, 1, 1)
# print is_top(grid, 2, 1)
# print is_top(grid, 3, 1)
# print is_top(grid, 4, 1)
# print is_top(grid, 5, 1)

# print is_top(grid, 0, 2)
# print is_top(grid, 1, 2)
# print is_top(grid, 2, 2)
# print is_top(grid, 3, 2)
# print is_top(grid, 4, 2)
# print is_top(grid, 5, 2)

# print is_top(grid, 0, 3)
# print is_top(grid, 1, 3)
# print is_top(grid, 2, 3)
# print is_top(grid, 3, 3)
# print is_top(grid, 4, 3)
# print is_top(grid, 5, 3)
