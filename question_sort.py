import random
import math
def genie(a, i, val):
	return a.count(i) == val

def lower(a, i, val):
	return a.count(i) < val

def question_sort(a, k, n):
	res = []
	count = 0
	for i in range(1, k+1):
		low = 0
		high = n
		mid = (low+high)/2
		count += 1
		while not genie(a, i, mid):
			count += 1
			if lower(a, i, mid):
				high = mid-1
			else:
				low = mid+1
			mid = (low+high)/2
		print (i, mid)
		if count > k*math.log(n, 2):
			print("nope: count = {}, k*log(n) = {}\nk {}, n: {}, logn: {}\n\n".format(count, k*math.log(n, 2), k, n, math.log(n, 2)))
		res += [i]*mid
	return res

print(question_sort([1, 3, 5, 5, 5], 5, 5))

# for k in range(1, 100):
# 	for n in range(k, 101):
# 		a = [ random.randint(1, k) for _n in range(n) ]
# 		print(a)
# 		qsorted =question_sort(a, k, n)
# 		print(qsorted)
# 		standardsorted = sorted(a) 
# 		print(standardsorted)
		
# 		if qsorted != standardsorted:
# 			print("whoops")
