from select import partition, selectMedian

a = [1, 2, 3, 4, 5,5,5, 5, 5, 2, 2, 1, 3]
# a = [3, 3, 4, 5]

NIL = None
def swap(arr, a, b):  
    temp = arr[a]  
    arr[a] = arr[b]  
    arr[b] = temp  

def selectMedian(arr):
    return kthSmallest(arr, 0, len(arr)-1, len(arr)//2)

# A simple function to find  
# median of arr[] from index l to l+n 
def findMedian(arr, l, n): 
    lis = []
    c = 0
    for i in range(l, l + n): 
    	if arr[i] != NIL:
	        lis.append(arr[i])
	        c+=1
    # Sort the array  
	lis.sort()
	# print(n)
	# print(arr)
	# print(lis)
	# print(c)

    # Return the middle element 
    return lis[c // 2] if len(lis) > 0 else None

def kthSmallest(arr, l, r, k):
    n = r - l + 1
    if k > 0 and k <= n:
        median = []

        i = 0
        while i < n // 5:
			med = findMedian(arr, l + i * 5, 5)
			if med is not None:
				median.append(med)
				i += 1
        if i * 5 < n:
			med = findMedian(arr, l+i *5, n%5)
			if med is not None:
				median.append(med)
				i+=1
        if i == 1:
            medOfMed = median[i-1]
        else:
            medOfMed = kthSmallest(median, 0, i-1, i//2)

        pos = partition(arr, l, r, medOfMed)
        if pos - l == k-1:
            return arr[pos]
        elif pos - l > k - 1:
            return kthSmallest(arr, l, pos-1, k)
        else:
            return kthSmallest(arr, pos+1, r, k-pos+l-1)
    return None

def modifiedPartition(arr, x):
	for i in range(0, len(arr)):
		if arr[i] == x:
			swap(arr, len(arr)-1, i)
	x = arr[len(arr)-1]
	i = 0
	count = 1
	for j in range(0, len(arr)-1):
		if arr[j] == x:
			arr[j] = NIL
			count += 1
		if arr[j] < x:
			swap(arr, i, j)
			i+=1
	swap(arr, i, len(arr)-1)
	return (i, count)

def allthesame(a):
	x = a[0]
	for e in a:
		if x != e:
			return False
	return True

def kOrMore(a, k):
	# print(a)
	if len(a) < k:
		return
	if len(a) == k:
		# print(allthesame(a))
		if (allthesame(a) and a[0] != None):
			print(a[0])
		return
	else:
		m = selectMedian(a)
		i, c = modifiedPartition(a, m)
		# print(m, i, c, a)
		if c >= k and m != None:
			print(m)
		kOrMore(a[:i], k)
		kOrMore(a[i+1:], k)

if __name__ == '__main__':
	kOrMore(a, 2)