# 建立一个循环队列

class CircularSequenceQueue():
	
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

	def EnQueue(self, x):
		if (self.rear+1) % self.MaxQueueSize != self.front:
			self.rear = (self.rear+1) % self.MaxQueueSize
			self.s[self.rear] = x
		else:
			print("The Queue is full.")
			return


	def ExQueue(self):
		if self.IsEmptyQueue():
			print("The Queue is empty.")
			return 
		else:
			self.front = (self.front+1) % self.MaxQueueSize #将front后面的下标赋给front
			return self.s[self.front]
	
			
	def CreateQueueByInput(self):
		data = input("Please input the element(to end the input by pressing '#'): ")
		while data != '#':
			self.EnQueue(data)
			data = input("Please input the element: ")		
			

	def GetHead(self):
		if self.IsEmptyQueue():
			print("The SequeceQueue is empty.")
			return
		else:
			return self.s[(self.front+1)%self.MaxQueueSize]
	
	
	def GetQueueLength(self):
		print("The present SequenceQueue's length is:",self.rear - self.front)
		return (self.rear-self.front+self.MaxQueueSize) % self.MaxQueueSize
	
#These two functions are not the basic operational functions of sequencequeue, but the adding-part to solve the Fibonacci problem				
	def CouplesOfRabbits(self, month):
		sq =  CircularSequenceQueue()
		if month == 0:
			print("the initial couples of rabbits is",1)
			return
		if month == 1:
			print("the couples of rabbits in first month is",2)
			return
		if month > 1:
			sq.EnQueue(1)
			sq.EnQueue(2)
			imonth = 1
			while imonth < month:
				NumHead = sq.ExQueue()
				NumRear = sq.GetHead()
				TotalNumber = NumHead + NumRear
				sq.EnQueue(TotalNumber)
				imonth = imonth + 1
			while sq.GetQueueLength() != 1:
				sq.ExQueue()
			print("the couples of rabbits in the number of",month,"month is",sq.GetHead())
					

	def TestRabbits(self):
		n = int(input("Please input the month: "))
		while n < 0:
			n = int(input("Please input the month: "))
		self.CouplesOfRabbits(n)
	
			
