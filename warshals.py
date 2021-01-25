class Graph:
	def __init__(self, vertices):
		self.V = vertices


	def printsol(self, reach):
		print("transitive closure of the given graph")
		for i in range(self.V):
			for j in range(self.V):
				print("%7d\t" % (reach[i][j]))
			print("")


	def transitive(self, graph):
		reach = [i[:] for i in graph]
		for k in range(self.V):
			for i in range(self.V):
				for j in range(self.V):
					reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
		self.printsol(reach)

g = Graph(4)

graph = [
	[0, 1, 0, 0],
	[0, 0, 0, 1],
	[0, 0, 0, 0],
	[1, 0, 1, 0]
]

g.transitive(graph)
