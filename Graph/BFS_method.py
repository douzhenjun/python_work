
VERTS = 7
class Node:
	def __init__(self):
		self.value = None
		self.next = None

class GraphLink:
	def __init__(self):
		self.first = None
		self.last = None
		self.head = [Node() for x in range(VERTS+1)]
		self.run = [0 for x in range(VERTS+1)]
		self.data = [[1,2],[1,3],[3,4],[3,5],[2,7],[7,6],[6,2]]
		
	def bfs(self, current):
		for i in range(1,VERTS+1):
			ptr = self.head[i]
			self.head[i].value = i
			for j in range(len(self.data)):
				if self.data[j][0] == i:
					newnode = Node()
					newnode.value = self.data[j][1]
					ptr.next = newnode
					ptr = ptr.next

		ptr = self.head[current]
		index = 0
		while True:
			while ptr != None:
				if self.run[ptr.value] == 0:
					print("[%d]"%ptr.value,end="")
					self.run[ptr.value] = 1
					ptr = ptr.next
					index += 1
				else:
					ptr = ptr.next
			if index == VERTS:
				break
			current += 1
			ptr = self.head[current]


print("这个无向图的广度优先遍历结果如下:")
gl = GraphLink()
gl.bfs(1)
