# умножение двух матриц
def multiply(a, b):
	c = [[0] * len(b[0]) for i in range(len(a))]
	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(a[0])):
				c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % 2
	return c
