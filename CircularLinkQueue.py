#创建一个链式队列
class LinkedQueueNode():
	def __init__(self,data):
		self.data = data
		self.next = None
		
	
class CircularLinkQueue():
	def __init__(self):
		self.head = LinkedQueueNode(None)
		# self.front = self.head
		self.rear = self.head

	
	def IsEmptyQueue(self):
		if self.rear == self.head:
			flag = True
		else:
			flag = False
		return flag
	
	
	def EnQueue(self, x):
		if self.IsEmptyQueue():
			Element = LinkedQueueNode(x)
			self.rear.next = Element
			Element.next = self.head
			self.rear = self.rear.next
		else:
			self.rear = self.head.next
			while self.rear.next != self.head:
				self.rear = self.rear.next
			Element = LinkedQueueNode(x)
			self.rear.next = Element
			Element.next = self.head
		
		
	def DeQueue(self):
		if self.IsEmptyQueue():
			print("The Queue is empty.")
			return
		else:
			tNode = self.head.next
			self.head.next = tNode.next
			if tNode.next == self.head:
				self.rear = self.head
			return tNode.data
			
	def GetHead(self):
		if self.IsEmptyQueue():
			print("The Queue is empty.")
			return
		else:
			return self.head.next.data
		
	def GetLength(self):
		tNode = self.head
		n = 0
		while tNode.next != self.head:
			tNode = tNode.next
			n += 1
		return n	
	
	def TraverseInQueue(self):
		if self.IsEmptyQueue():
			print("The Queue is empty.")
			return
		else:
			print("head->", end="")
			tNode = self.head
			while tNode.next != self.head:
				tNode = tNode.next
				print(tNode.data, end="->")
			print("head")


cl = CircularLinkQueue()
cl.EnQueue(1)
cl.EnQueue(2)
cl.DeQueue()
cl.DeQueue()
cl.TraverseInQueue()
			
				
			
				
			
		
		
		
		
