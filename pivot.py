"""
0 is partition element
i marks border between low and high
j marks border between high and unchecked
"""
def partition(a, p):
	val = a[p]
	a[p] = a[0]
	a[0] = val
	i = 1
	for index in range(1, len(a)):
		if a[index] < val:
			tmp = a[index]
			a[index] = a[i]
			a[i] = tmp
			i += 1
	a[0] = a[i-1]
	a[i-1] = val
	return i-1

a = [6, 3, 1, 7, 23, 57, 8, 2]
print(partition(a, 3))
print(a)
