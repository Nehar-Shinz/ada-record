def sol(a, n, v, s):
	if (s == 0):
		for val in v:
			print(val, end=" ")
		print()
		return
	if (n == 0):
		return
	sol(a, n - 1, v, s)
	v1 = [] + v
	v1.append(a[n - 1])
	sol(a, n - 1, v1, s - a[n - 1])

def solprint(arr, n, sum):
	v = []
	sol(arr, n, v, sum)

a = []
num = int(input("enter total number elements"))
for i in range(0, num):
	e = int(input("enter element:"))
	a.append(e)
sum = int(input("enter sum"))
n = len(a)
solprint(a, n, sum)