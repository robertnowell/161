def inorder(n):
	if n is not None:
		inorder(n['left'])
		print(n['data'])
		inorder(n['right'])

# 		5
# 	4		10
# 3				20
# 			12
	
node = {
	"data": 5,
		"left": {
				"data": 4,
				"left": {
						"data": 3,
						"left": None,
						"right": None,
				},
				"right": None,
		},
		"right": {
			"data": 10,
			"left": None,
			"right": {
				"data": 20,
				"left": {
					"data": 12,
					"left": None,
					"right": None,
				},
				"right": None,
			},
	}
}
inorder(node)