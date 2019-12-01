#课后习题第六题(P229)：用邻接矩阵表示这个图并给出各个顶点之间最短距离的表示矩阵

path = [[1,2,5],[1,3,6],[2,1,10],[3,2,2],[3,1,3]]
edge = [[0]*3 for x in range(3)]
for i in range(len(path)):
	start_vertex = path[i][0]-1
	end_vertex = path[i][1]-1
	distance = path[i][2]
	edge[start_vertex][end_vertex] = distance
print(edge)
