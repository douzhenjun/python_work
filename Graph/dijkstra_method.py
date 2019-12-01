VERTS = 6
INFINITE = 999
#tips:关于数组下标与顶点下标的一一对应实在是一件很繁琐的事情，这是因为数组下标从0开始，而顶点下标从1开始，所以必须搞清楚哪些数组的位置恰好就是顶点的下标，
#而哪些数组的位置是顶点下标-1.
class GraphLink:
	def __init__(self):
		# self.path = [[1,2,29], [2,3,30],[2,4,35],
					# [3,5,28],[3,6,87],[4,5,42],
					# [4,6,75],[5,6,97]]
		self.path = [[1,3,10],[1,6,100],[1,5,30],[2,3,5],[3,4,50],[5,4,20],[5,6,60],[4,6,10]]
		self.vertex_matrix = []
		self.run = [0 for x in range(VERTS+1)]
		for x in range(1, VERTS+1):
			self.vertex_matrix.append(x)
		self.edge = [[0]*(VERTS+1) for x in range(VERTS+1)]
		for i in range(1,VERTS+1):
			for j in range(1,VERTS+1):
				if j == i:
					self.edge[i][j] = 0
				else:
					self.edge[i][j] = INFINITE
		for k in range(len(self.path)):
			start_vertex = self.path[k][0]
			end_vertex = self.path[k][1]
			self.edge[start_vertex][end_vertex] = self.path[k][2]
	
	

	def Dijkstra(self, x, y):
		distance = [INFINITE] * VERTS
		total = [x]
		self.run[x] = 1
		for i in range(1, VERTS+1):
			if i == x:
				distance[i-1] = 0
		print(distance)
		
		z = x
		
		while len(total) < VERTS:
			for k in range(1, VERTS+1):
				if self.edge[z][k] < INFINITE and distance[z-1] + self.edge[z][k] < distance[k-1]:#如果这个点x到k顶点的距离不是无穷，并且加上这段
					distance[k-1] = distance[z-1] + self.edge[z][k]                             #距离后，比原来存储在d[k-1]里的距离要小，那么
			minval = INFINITE																	#d[k-1]的值被更新.
			for j in distance:
				if j < minval and self.run[distance.index(j)+1] == 0:					#从剩余顶点的距离值中找到最小的那个，存入total中
					minval = j															#如果找不到(即都是无穷),那么就把remain中第一个
					min_index = distance.index(minval)									#元素在distance中的位置作为下一个存入total中的点下标
			if minval == INFINITE:
				for j in distance:
					if self.run[distance.index(j)+1] == 0:
						min_index = distance.index(j)
						break
			z = min_index + 1
			total.append(z)
			self.run[z] = 1
			print(distance)
		if distance[y-1] == INFINITE:
			print("There is no way from vertex",x,"to vertex",y,".")
		else:
			print("The shortest way between vertex",x,"and vertex",y,"is",distance[y-1],".")

gl = GraphLink()
gl.Dijkstra(1,4)				
			
					
