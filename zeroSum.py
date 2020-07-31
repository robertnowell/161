"""
	in o(n), check if dict contains running sum from start.
	If not, store index at hash
	if so, calculate whether distance between start and i is greater than current max
		if so, new max
"""
def maxLengthZeroSumSubarray(a):
	sums = {}
	sumsofar = 0
	maxlength = 0
	for i in range(len(a)+1):
		# import pdb; pdb.set_trace()
		if sumsofar in sums:
			length = i - sums[sumsofar]
			if length > maxlength:
				maxlength = length
				print("new max: ", a[sums[sumsofar]:i])
		else:
			sums[sumsofar] = i
		if i < len(a):
			sumsofar += a[i]
	return maxlength

if __name__ == '__main__':
	print(maxLengthZeroSumSubarray([50, -5, 1, 2, -3, 3, -1, -2, 3, -3]))
