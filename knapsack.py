from pprint import pprint


"""
for every column (each column represents an item)
	and for every row (which represents a possible capacity)
		if size of item i is greater than capacity
			optimal solution is the previous item, same capacity
		otherwise (size of item i is less than capacity)
			optimal solution is either
				previous item, same capacity
			or
				previous item, capacity reduced by current item size
"""
def knapsack(v, s, C):
	a = [[0 for i in range(len(v)+1)] for j in range(C+1)] 
	# a = [[0] * (len(v)+1)] * (C+1)
	# import pdb; pdb.set_traCe()
	pprint(a)
	for i in range(C):
		a[i][0] = 0
	for index in range(1, len(v)+1):
		i = index-1
		pprint(a)
		# import pdb; pdb.set_traCe()
		for c in range(C+1):
			if s[i] > c:
				a[c][index] = a[c][index-1]
			else:
				a[c][index] = max(a[c][index-1], a[c-s[i]][index-1] + v[i])
	pprint(a)
	return a[C][len(v)]

def merge_by_v(t1, t2):
	res = []
	i = 0
	j = 0
	while i < len(t1) and j < len(t2):
		if t1[i][0] < t2[j][0]:
			res.append(t1[i])
			i+=1
		else:
			res.append(t2[j])
			j+=1
	while i < len(t1):
		res.append(t1[i])
		i+=1
	while j < len(t2):
		res.append(t2[j])
		j+=1
	return res

def mergesort_by_v(T):
	if len(T) == 1:
		return T
	else:
		mid = len(T) / 2
		l = mergesort_by_v(T[0:mid])
		r = mergesort_by_v(T[mid:])
		return merge_by_v(l, r)

def greedy_knapsack(Q, T):
    tuples = []
    T = mergesort_by_v(T)
    T.reverse()
    print(T)
    i = 0
    while Q > 0:
    	q = T[i][1]
        if q >= Q:
            tuples.append((i, Q))
        else:
            tuples.append((i, q))
        Q -= q
        i+=1
    return tuples

if __name__ == '__main__':
	print(greedy_knapsack(8, [
		(3, 5),
		(10, 2),
		(6, 3),
		(20, .5),
	]))





"""
subproblems
	knapsacks of smaller size

recursive relationship
	for a given capacity:
		for every item
			find the max value attainable
				max value for a particular item = memo[capacity - item weight] + item value

"""
def unboundedKnapsack(v, s, C):
	memo = [ 0 for i in range(C+1) ]
	minweight = min(s)
	for c in range(1, C+1):
		if c >= minweight:
			best = memo[c]
			for i in range(len(v)):
				# import pdb; pdb.set_trace()
				candidate = memo[c-s[i]] + v[i]
				best = best if best > candidate else candidate
			memo[c] = best
	pprint(memo)


"""
subproblems
	knapsacks of smaller size and fewer available elements

recursive relationship
	for a given capacity:
		for a given item
			find best value given capacity and available items
			if item weight exceeds capacity
				same capacity previous item
			else
				max of (same capacity, previous item) and (capacity - weight of item, previous value + item value)
"""
def boundedKnapsack(v, s, C):
	memo = [ [ None for i in range(len(v) + 1)] for i in range(C+1) ]
	minweight = min(s)
	for i in range(len(v) + 1):
		memo[0][i] = 0
	for i in range(C+1):
		memo[i][0] = 0
	for c in range(1, C+1):
		for i in range(1, len(v)+1):
			if s[i-1] > c:
				memo[c][i] = memo[c][i-1]
			else:
				memo[c][i] = max(memo[c][i-1], memo[c-s[i-1]][i-1] + v[i-1])
	pprint(memo)
	return memo[C][len(v)]
v = [3, 2, 4, 4]
s = [4, 3, 2, 3]

# # v = [1, 4, 6]
# # s = [1, 2, 3]
# if __name__ == '__main__':
# 	pprint(boundedKnapsack(v, s, 7))
