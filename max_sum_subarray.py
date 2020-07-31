def max_subarray(a):
	current_sum = 0
	max_sum = a[0]
	for n in a:
		print current_sum, max_sum, n
		current_sum += n
		if current_sum > max_sum:
			max_sum = current_sum
		if current_sum < 0:
			current_sum = 0
	return max_sum

a = [-98, 20, 46,-50]
ab = [72, 92,-49,-54,-33 ]
abc = [ 79,-66,-36, 38, 58, 84, 36, -1000]
abcd = [ -5, -4, -3, -2, -10]
# abc = [ 3, -5, 3, -1, 2, -5]
print(max_subarray(abcd))
