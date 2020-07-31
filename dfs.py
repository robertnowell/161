v = [
	"a", "b", "c", "d", "e"
]
e = {
	"a": ['b', 'd'],
	"b": ['d', 'e', 'c'],
	"c": ['d','e'],
	"d": ['e'],
	"e": [],
}

visited = set()

global a

def dfsAlphabeticalFinishedDescending(n):
	global a
	if n not in visited:
		visited.add(n)
		for neighbor in e[n]:
			dfsAlphabeticalFinishedDescending(neighbor)
		a.append(n)

def dfsAlphabeticalStartAscending(n):
	global a
	if n not in visited:
		a.append(n)
		visited.add(n)
		for neighbor in e[n]:
			dfsAlphabeticalStartAscending(neighbor)

def dfsReversedStartAscending(n):
	global a
	if n not in visited:
		a.append(n)
		visited.add(n)
		for neighbor in reversed(e[n]):
			dfsReversedStartAscending(neighbor)

def dfsReversedFinishedDescending(n):
	global a
	if n not in visited:
		visited.add(n)
		for neighbor in reversed(e[n]):
			dfsReversedFinishedDescending(neighbor)
		a.append(n)

if __name__ == '__main__':
	global a
	a = []
	print("alphabetical start ascending")
	dfsAlphabeticalStartAscending('c')
	for n in v:
		dfsAlphabeticalStartAscending(n)
	print([n for n in a])

	visited = set()
	a = []
	print("alphabetical finished descending")
	dfsAlphabeticalFinishedDescending('c')
	for n in v:
		dfsAlphabeticalFinishedDescending(n)
	print([n for n in reversed(a)])

	visited = set()
	a = []
	print("reversed start ascending")
	dfsReversedStartAscending('c')
	for n in reversed(v):
		dfsReversedStartAscending(n)
	print([n for n in a])

	visited = set()
	a = []
	print("reversed finished descending")
	dfsReversedFinishedDescending('c')
	for n in reversed(v):
		dfsAlphabeticalFinishedDescending(n)
	print([n for n in reversed(a)])
