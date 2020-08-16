from pprint import pprint

def bst(g):
	n = len(g)
	memo = [ [None for i in range(n)] for j in range(n) ]
	pprint(memo)
	for i in range(n):
		for j in range(n):
			cell = g[i][j]
			if i == 0 or j == 0:
				memo[i][j] = 1 if cell == 1 else 0
			else:
				one = memo[i-1][j-1]
				two = memo[i-1][j]
				three = memo[i][j-1]
				best = max(one, two, three)
				if cell == g[i][j-1] == g[i-1][j] == g[i-1][j-1] == 1:
					if one == two == three:
						memo[i][j] = best+1
						bestcell = (i, j)
					else:
						memo[i][j] = best
				else:
					memo[i][j] = best
	pprint(memo)
	print(memo[n-1][n-1])
	pprint(grid)
	print(bestcell)
grid = [
		[0,1,1,1,1],
		[1,1,1,1,1],
		[0,1,1,1,1],
		[0,1,1,0,1],
		[1,0,0,0,0],
	]
bst(grid)