from pprint import pprint

def lcs(memo, a, b, aleft, bleft):
	pprint(memo)
	pprint("recursive call")
	# import pdb; pdb.set_trace()
	if len(a)-aleft == 0 or len(b)-bleft == 0:
		return 0
	if memo[aleft][bleft] >= 0:
		pprint("cache hit")
		return memo[aleft][bleft]
	if a[aleft] == b[bleft]:
		memo[aleft][bleft] = 1+lcs(memo, a, b, aleft+1, bleft+1)
		return memo[aleft][bleft] 
	memo[aleft][bleft] = max(lcs(memo, a, b, aleft+1, bleft), lcs(memo, a, b, aleft, bleft+1))
	return memo[aleft][bleft] 

# def lcs(a, b):
# 	pprint("recursive call")
# 	if len(a) == 0 or len(b) == 0:
# 		return 0
# 	if a[0] == b[0]:
# 		return 1+lcs(a[1:], b[1:])
# 	return max(lcs(a[1:], b), lcs(a, b[1:]))

"""
common subproblems:
	common subsequence ending at earlier index
     if two are equal
		1 + previous of i-1, j-1
	else
		max(previous i, previous j)
"""			

def lcs(a, b):
	memo = [ [ None for i in range(len(b) + 1) ] for i in range(len(a) + 1) ]
	for i in range(len(a)+1):
		memo[i][0] = 0
	for j in range(len(b)+1):
		memo[0][j] = 0
	pprint(memo)
	# bottom up strategy
	for i in range(1, len(a)+1):
		for j in range(1,len(b) + 1):
			if a[i-1] == b[j-1]:
				memo[i][j] = 1 + memo[i-1][j-1]
			else:
				memo[i][j] = max(memo[i-1][j], memo[i][j-1])
	pprint(memo)

if __name__ == '__main__':
	# a = "abcde" 
	# b = "ace"
	# a = "AGGTAB"
	# b = "GXTXAYB"
	a = "ACTG"
	b = "ACGGA"
	# memo = [ [ -1 for i in range(len(b)+1) ] for i in range(len(a)+1) ]
	# pprint(lcs(memo, a,b, 0, 0))
	# pprint(memo)
	print(lcs(a,b))
