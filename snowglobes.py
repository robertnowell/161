from select import partition, selectMedian

a = [(2007, 40), (2002, 30), (2018, 50), (2003, 100), (2011, 60)]

def selectMedianYear(a):
	years = [ e[0] for e in a]
	y = selectMedian(years)
	if y == None:
		return a[0][0]
	return [year for year in years if year == y][0]

def swap(arr, a, b):  
    temp = arr[a]  
    arr[a] = arr[b]  
    arr[b] = temp  

def modifiedPartition(arr, x):
	for i in range(0, len(arr)):
		if arr[i][0] == x:
			swap(arr, len(arr)-1, i)
	x = arr[len(arr)-1]
	i = 0
	count = 0
	for j in range(0, len(arr)-1):
		if arr[j][0] <= x[0]:
			count += arr[j][1]
			swap(arr, i, j)
			i+=1
	swap(arr, i, len(arr)-1)
	return (i, count)

def kthSnowglobe(a, k):
	print(a, k)
	n = len(a)
	y = selectMedianYear(a)
	print(y)
	medi, c= modifiedPartition(a, y)
	print(medi)
	print(a)
	print(c)
	if c > k:
		return kthSnowglobe(a[:medi], k)
	elif c+a[medi][1] >= k:
		return a[medi][0]
	else:
		return kthSnowglobe(a[medi+1:], k-c-a[medi][1])

if __name__ == '__main__':
	print(kthSnowglobe(a, 171))