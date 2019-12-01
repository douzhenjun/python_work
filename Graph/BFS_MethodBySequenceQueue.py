#bfs_method by queue
VERTS = 6
ROWNUMBER = 5

class Node:
	def __init__(self):
		self.value = None
		self.next = None


class SequenceQueue:
	def __init__(self):
		self.front = -1
		self.rear = -1
		self.MAXSIZE = 10
		self.queue = [None for x in range(self.MAXSIZE)]
		
	def enqueue(self, value):
		if self.rear > self.MAXSIZE:
			return
		self.rear += 1
		self.queue[self.rear] = value
		
	def IsEmptyQueue(self):
		if self.rear == self.front:
			return True
		return False
		
	def dequeue(self):
		if self.IsEmptyQueue():
			return
		self.front += 1
		return self.queue[self.front]
	
		
	def TraverseInQueue(self):
		if self.IsEmptyQueue():
			return
		ptr = -1
		while ptr != self.rear:
			ptr += 1
			if ptr > self.front:
				print(self.queue[ptr], end="")

				
class GraphLink:
	def __init__(self):
		self.head = [Node() for x in range(VERTS+1)]
		self.run = [0 for x in range(VERTS+1)]
		# self.data = [[1,2],[2,1],[1,3],[3,1],
					# [4,2],[2,4],[2,5],[5,2],
					# [3,6],[6,3],[3,7],[7,3],
					# [4,5],[5,4],[6,7],[7,6],
					# [5,8],[8,5],[6,8],[8,6]]
		self.data = [[1,6],[1,2],[2,3],[2,4],[6,5]]
# '''		
# 建立一个线性队列,一开始将current存入队列,如果队列非空,每次出列一个元素,并且把这个
# 元素的邻接元素存入这个队列(如果这个邻接元素被遍历输出过,就不用再存入队列中了),这样
# 一定在有限步以后,不再有元素进列.而出列是每次都有的操作,所以最终队列一定为空,循环也
# 就此结束,打印出所有的元素.
# '''
	
	def bfs(self, current):
		#通过链表将各个顶点及其邻接点存储在self.head[i]中
		for i in range(1, VERTS+1):
			self.head[i].value = i
			ptr = self.head[i]
			for j in range(ROWNUMBER):
				if self.data[j][0] == i:
					newNode = Node()
					newNode.value = self.data[j][1]
					ptr.next = newNode
					ptr = ptr.next										
		#建立一个线性队列，开始广度优先遍历			
		q = SequenceQueue()					
		q.enqueue(current)												
		print("[%d]"%current, end="")		
		while q.front != q.rear:
			current = q.dequeue()
			self.run[current] = 1
			tempnode = self.head[current]
			while tempnode != None:
				if self.run[tempnode.value] == 0:
					q.enqueue(tempnode.value)
					self.run[tempnode.value] = 1
					print("[%d]" %tempnode.value, end="")
				tempnode = tempnode.next
				
		
if __name__ == "__main__":
	print("广度优先遍历的顶点:")
	gl = GraphLink()
	gl.bfs(1)			
			
