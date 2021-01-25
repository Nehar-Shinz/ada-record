def printsol(cost, N):
	for i in range(N):
		for j in range(N):
			if(cost[i][j] == M):
				print("INF", end=" ")
			else:
				print(cost[i][j], end=" ")
		print(" ")


def floyd(adjmat, N):
	cost = adjmat.copy()
	for k in range(N):
		for v in range(N):
			for u in range(N):
				if cost[v][k] != float('inf') and cost[k][u] != float('inf') and (cost[k][u] < cost[v][u]):
					cost[v][u] = cost[v][k] + cost[k][u]
				if cost[v][v] < 0:
					print("negative cycle found")
					return
	printsol(cost, N)

if __name__ == '__main__':
	N = 4
	M = float('inf')
	adjmat = [[0, M, 3, M],
				[2, 0, M, M],
				[M, 7, 0, 1],
				[6, M, M, 0]
				]
	floyd(adjmat, N)
