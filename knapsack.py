from pprint import pprint

def knapsack(v, s, c):
	a = [[0] * (len(v)+1)] * (c+1)
	# import pdb; pdb.set_trace()
	pprint(a)
	for i in range(c):
		a[i][0] = 0
	# import pdb; pdb.set_trace()
	for i in range(len(v)+1):
		pprint(a)
		# import pdb; pdb.set_trace()
		for j in range(c):
			if s[i] > j:
				a[j][i] = a[j][i-1]
			else:
				a[j][i] = max(a[j][i-1], a[j-s[i] + v[i]][i-1])
	return a[c][len(v)]

v = [3, 2, 4, 4]
s = [4, 3, 2, 3]
if __name__ == '__main__':
	pprint(knapsack(v, s, 6))
