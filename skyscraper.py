def tallest(g):
	# assume rows >= 1
	num_cols = len(g[0])
	max_height = 0
	tallest_col = -1
	for col in range(num_cols):
		h = find_height(g, col)
		print('h', h)
		if max_height < h:
			tallest_col = col
			max_height = h
	return tallest_col

def find_height(g, col):
	high = 0
	low = len(g) -1
	mid = (high + low)/2
	if g[low][col] != 0:
		return -1
	# import pdb; pdb.set_trace()
	while not is_top(g, mid, col):
		if g[mid][col] == 1:
			high = mid+1
		else:
			low = mid-1
		mid = (high+low)/2
	return len(g)-mid

def is_top(g, row, col):
	elem = g[row][col]
	if elem == 0 and (row-1 < 0 or g[row-1][col] == 1):
		return True
	return False

grid1 = [
	[1, 1, 1, 1, 1],
	[1, 0, 1, 1, 1],
	[1, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0],
]

grid2 = [
	[1, 0, 1, 1, 1],
	[1, 0, 1, 1, 1],
	[1, 0, 1, 1, 1],
	[1, 0, 1, 1, 1],
	[1, 0, 1, 1, 1],
]

grid3 = [
	[1, 1, 1, 1, 1],
	[1, 0, 1, 1, 1],
]

grid4 = [
	[1, 0, 1, 1, 1],
]

grid5 = [
	[1, 1, 1, 1, 1]
]

grid6 = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
# print (find_height(grid, 0))
# for i in range(len(grid3[0])):
# 	print(find_height(grid3, i))
print(tallest(grid1)) 
print(tallest(grid2)) 
print(tallest(grid3)) 
print(tallest(grid4)) 
print(tallest(grid5)) 
print(tallest(grid6)) 
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
