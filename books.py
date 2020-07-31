import random

def are_the_same(a, b):
	return a == b

def books(a):
	if len(a) == 1:
		return a[0]
	mid = len(a)/2
	left = books(a[0:mid])
	right = books(a[mid:])
	lcount = 0
	rcount = 0
	for b in a:
		if are_the_same(left, b):
			lcount +=1
		if are_the_same(right, b):
			rcount +=1
	if lcount > rcount:
		return left
	else:
		return right

arr = [0, 1, 2, 3, 1, 2, 4, 1, 3, 1, 2, 1, 1, 1, 2, 1]

for i in range(100):
	random.shuffle(arr)
	print(arr)
	print(books(arr))