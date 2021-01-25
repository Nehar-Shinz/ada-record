def binomial(n, k):
	c = [[0 for x in range(k + 1)] for x in range(n + 1)]
	for i in range(n + 1):
		for j in range(min(i, k) + 1):
			if j == 0 or j == i:
				c[i][j] = 1
			else:
				c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
	return c[n][k]


n = int(input("enter 1st number"))
k = int(input("enter 2nd number"))
print("value of c [" + str(n) + "] [" + str(k) + "] is " + str(binomial(n, k)))
