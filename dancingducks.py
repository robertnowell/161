"""
if one spot available, return point value for that spot
otherwise
	check if avail in memo
		if so, return that amount
	else
		play green
		play white
		recurse?
"""
greenpoints = 0
whitepoints = 0
memo = {}
# def dancingducks(a, b, avail, greenTurn):
# 	# print('')
# 	# print(a)
# 	# print(b)
# 	# print(avail)
# 	# print(memo)
# 	if avail == (0, 1, 2, 3):
# 		import pdb; pdb.set_trace()
# 	if avail in memo:
# 		# print("return from cache", avail, memo[avail])
# 		return memo[avail]
# 	if len(avail) == 1:
# 		# print("base case: ", avail)
# 		return a[avail[0]]
# 	if len(avail) == 0:
# 		return 0
# 	left = avail[0]
# 	right = avail[-1]
# 	# choose left
# 	b[left] = 'G' if greenTurn else 'W'
# 	leftavail = avail[1:]
# 	# explore
# 	b[left+1] = 'G' if not greenTurn else 'W'
# 	option1 = dancingducks(a, b, leftavail[1:], greenTurn)
# 	b[left+1] = None
# 	b[right] = 'G' if not greenTurn else 'W'
# 	option2 = dancingducks(a, b, leftavail[:-1], greenTurn)
# 	b[right] = None
# 	leftScore = a[left] + min(option1, option2)
# 	# unchoose left
# 	b[left] = None

# 	# choose right
# 	b[right] = 'G' if greenTurn else 'W'
# 	rightavail = avail[:-1]
# 	# explore
# 	b[right-1] = 'G' if not greenTurn else 'W'
# 	option1 = dancingducks(a, b, rightavail[:-1], greenTurn)
# 	b[right-1] = None
# 	b[left] = 'G' if not greenTurn else 'W'
# 	option2 = dancingducks(a, b, rightavail[1:], greenTurn)
# 	b[left] = None
# 	rightScore = a[right] + min(option1, option2)
# 	# unchoose right
# 	b[right] = None

# 	memo[avail] = max(leftScore, rightScore)
# 	print(memo)
# 	return memo[avail]

# memo = {}
def dancingducks(D, low, high):
	if (low, high) in memo:
		return memo[(low, high)]
	if high-low == 1:
		return max(D[low], D[high])
	if low == high:
		return D[low]
	left = low
	right = high

	# choose left
	opponentLeft = dancingducks(D, low+2, high)
	opponentMiddle = dancingducks(D, low+1, high-1)
	leftScore = D[left] + min(opponentLeft, opponentMiddle)

	# choose right
	opponentRight = dancingducks(D, low, high-2)
	rightScore = D[right] + min(opponentMiddle, opponentRight)

	memo[(low, high)] = max(leftScore, rightScore)
	return memo[(low, high)]

memo = []
def _dancingducks(D, low, high):
	if memo[low][high] != None:
		return memo[low][high]
	if high-low == 1:
		return max(D[low], D[high])
	if low == high:
		return D[low]
	left = low
	right = high

	# choose left
	opponentLeft = _dancingducks(D, low+2, high)
	opponentMiddle = _dancingducks(D, low+1, high-1)
	leftScore = D[left] + min(opponentLeft, opponentMiddle)

	# choose right
	opponentRight = _dancingducks(D, low, high-2)
	rightScore = D[right] + min(opponentMiddle, opponentRight)

	memo[low][high] = max(leftScore, rightScore)
	return memo[low][high]


def bottoms_up(D):
	memo = [ [ 0 for i in range(len(D)) ] for i in range(len(D)) ]
	for interval in range(len(D)):
		for j in range(interval, len(D)):
			i = 0
			a = b = c = -float("inf")
			if i + 2 <= j:
				a = memo[i+2][j]
			else:
				a = 0

			if i+1 <= j-1:
				b = memo[i+1][j-1]
			else:
				b = 0

			if i <= j-2:
				c = memo[i][j-2]
			else:
				c = 0

			memo[i][j] = max(D[i] + min(a, b), D[j] + min(b, c))
			i += 1
	return memo[0][-1]
if __name__ == '__main__':
	global memo
	memo = [ [ None for i in range(6) ] for i in range(6) ]
	# print(dancingducks([5, 7, 3, 4, 4, 6], [None]*6, (0, 1, 2, 3, 4, 5), True))
	# print(dancingducks([5, 7, 3, 4, 4, 6], 0, 5))
	print(_dancingducks([ 6, 9, 1, 2, 16, 8], 0, 5))
	print(bottoms_up([ 6, 9, 1, 2, 16, 8]))

	# print(dancingducks([3, 4, 4, 6], [None]*4, (0,1,2,3), True))