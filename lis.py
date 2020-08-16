def increasingSubsequence(A):
    D = [ [] for i in range(len(A)) ]
    longestOverallSubsequence = []
    for i in range(len(A)):
        import pdb; pdb.set_trace()
        longestEarlierSubsequence = []
        for k in range(i):
            if len(D[k]) > len(longestEarlierSubsequence) and A[k] < A[i]:
                longestEarlierSubsequence = D[k]
        D[i] = longestEarlierSubsequence + [A[i]]
        if len(D[i]) > len(longestOverallSubsequence):
            longestOverallSubsequence = D[i]
    return longestOverallSubsequence

def numberincreasingsubsequence(A):
    D = [ 0 for i in range(len(A)) ]
    for i in range(len(A)):
        longestEarlierSubsequence = 0
        for k in range(i):
            if D[k] > longestEarlierSubsequence and A[k] < A[i]:
                longestEarlierSubsequence = D[k]
        D[i] = longestEarlierSubsequence + 1
    print(D)

    for i in range(len(A)-1, -1, -1):
    	print(A[i])
    return max(D)

if __name__ == '__main__':
	print(numberincreasingsubsequence([6, 3, 2, 5, 6, 4, 8]))
