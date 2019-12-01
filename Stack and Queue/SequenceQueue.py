#构造一个线性队列及其相关操作

class SequenceQueue():
	
	def __init__(self):
		self.MaxQueueSize = 10
		self.s = [None for x in range(0, self.MaxQueueSize)]
		self.front = 0
		self.rear = 0
		self.fsq = []
		
	def IsEmptyQueue(self):
		if self.front == self.rear:
			iQueue = True
		else:
			iQueue = False
		return iQueue
		
	#Enter the SequeceQueue
	def EnQueue(self, x):
		if self.rear == self.MaxQueueSize-1:
			print("The SequenceQueue is full.")
			return
		else:
			self.rear = self.rear + 1
			self.s[self.rear] = x
			# print("The contemporary element is",x)
			self.fsq.append(x)
			
	#Exit the SequenceQueue
	def ExQueue(self):
		if self.IsEmptyQueue():
			print("The SequenceQueue is empty.")
			return
		else:
			self.front = self.front + 1
			self.fsq.pop(0)
			return self.s[self.front]
			
	
	#get the head of sequencequeue
	def GetHead(self):
		if self.IsEmptyQueue():
			if self.IsEmptyQueue():
				print("The SequeceQueue is empty.")
				return
			else:
				return self.s[self.front+1]
				
	def CreateQueueByInput(self):
		data = input("Please input the element(to end the input by pressing '#'): ")
		while data != '#':
			self.EnQueue(data)
			data = input("Please input the element: ")
		print(self.s)
		
		
	def GetQueueLength(self):
		print("The present SequenceQueue's length is:",self.rear - self.front)
		return self.rear - self.front
		
		
	def QueueTraverse(self):
		if self.IsEmptyQueue():
			print("The final SequenceQueue is empty.")
			return
		else:
			print("The final SequenceQueue is: ", end='')
			for i in range(self.front+1, self.rear+1):
				print(self.s[i], end=' ')
	
	
	def QueueVisit(self, element):
		j = 0
		k = 0
		for i in self.fsq:
			j = j + 1
			if i == element:
				print("The target element is in the index of",j,"in the SequenceQueue.")
			else:
				k = k + 1
		if k >= len(self.fsq):
			print("There is no target element in the SequenceQueue.")
if __name__ == "__main__":				
	sq = SequenceQueue()
	sq.CreateQueueByInput()
	sq.QueueVisit("20")			
			
			
			
			
			
			
			
			
			
			
			
			
			
