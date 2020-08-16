def get_parity(n):
	return "even" if n % 2 == 0 else "odd"

def memosplits(x, p, i, j, second):
	# import pdb; pdb.set_trace()
	if i == len(x) and j == len(p):
		return 1
	if (i == len(x) and j != len(p)) or (i != len(x) and j == len(p)):
		return 0
	key = (i, j, second)
	if key in memo:
		return memo[key]

	if second == True:
		if get_parity(x[i]) != p[j]:
			memo[key] = 0
		else:
		 	memo[key] = memosplits(x, p, i+1, j+1, False)
	elif get_parity(x[i] == p[j]):
		memo[key] = memosplits(x, p, i+1, j+1, False) + memosplits(x, p, i+1, j, True)
	else:
		memo[key] = memosplits(x, p, i+1, j, True)

	return memo[key]

# def splits(x, p, i, j, second):
# 	if i == len(x) and j == len(p):
# 		return 1
# 	if (i == len(x) and j != len(p)) or (i != len(x) and j == len(p)):
# 		return 0
# 	if second == True:
# 		if get_parity(x[i]) != p[j]:
# 			return 0
# 		return splits(x, p, i+1, j+1, False)
# 	if get_parity(x[i] == p[j]):
# 		return splits(x, p, i+1, j+1, False) + splits(x, p, i+1, j, True)
# 	return splits(x, p, i+1, j, True)
memo = {}

_x = [4, 1, 3, 2]
_p = ["even", "odd", "even"]
print(memosplits(_x, _p, 0, 0, False))


memo = {}
_x = [4]
_p = ["even", "odd"]
print(memosplits(_x, _p, 0, 0, False))


memo = {}
_x = [3, 5]
_p = ["odd"]
print(memosplits(_x, _p, 0, 0, False))


memo = {}
_x = [3, 5, 1, 7]
_p = ["odd", "odd", "odd"]
print(memosplits(_x, _p, 0, 0, False))
