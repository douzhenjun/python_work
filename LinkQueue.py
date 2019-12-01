#To get the free Travelling quality, Josephus has to play a game.A group of 
#visitors(number of people is 40)stand in a circle and speak number from 1 in begin,
#if one has spoken 3,he or she will exit the queue, then the next one speak from 1
#in begin, so as before.
#Each round exit one until there is only one ramain,which can travel in free.
#Josephus chooses to stand in the number of 31, will he get the free quality?
class QueueNode():
	def __init__(self):
		self.data = None
		self.next = None

class LinkQueue():
	def __init__(self):
		self.head = QueueNode()
		self.front = self.head
		self.rear = self.head
		
	def IsEmptyQueue(self):
		if self.front == self.rear:
			iQueue = True
		else:
			iQueue = False
		return iQueue
		
	def EnQueue(self, da):
		cNode = self.head
		while cNode.next != None:
			cNode = cNode.next
		cNode.next = QueueNode()
		cNode.next.data = da
		self.rear = cNode.next
		
		
	def DeQueue(self):
		if self.IsEmptyQueue():
			print("The Queue is empty!")
			return
		else:
			cNode = self.front.next
			self.front.next = cNode.next
			if self.rear == cNode:
				self.rear = self.front
			return cNode.data
			
	def GetHead(self):
		if self.IsEmptyQueue():
			print("The queue is empty.")
			return
		else:
			return self.front.next.data
	
	def GetQueueLength(self):
		if self.IsEmptyQueue():
			print("The queue is empty.")
			return
		else:
			length = 0
			tNode = self.front
			while tNode != self.rear:
				tNode = tNode.next
				length += 1
			return length
	
	def QueueTraverse(self):
		if self.IsEmptyQueue():
			print("The queue is empty.")
			return
		else:
			tNode = self.front
			while tNode != self.rear:
				tNode = tNode.next
				print(tNode.data,end=" ")
			print()
	
	def Josephus(self, n, k):
		qu = LinkQueue()
		i = 1
		while i <= n:
			qu.EnQueue(i)
			i = i + 1
		print("The rank of number in queue is:")
		qu.QueueTraverse()
		print("\nThe rank of number in exiting the queue is: ")
		count = 0
		while qu.GetQueueLength() != 1:
			iNum = 1
			while iNum != k:
				tData = qu.DeQueue()
				qu.EnQueue(tData)
				iNum = iNum + 1
			print(qu.DeQueue(), end=" ")
			count = count + 1
			if count%10 == 0:
				print()
		print("\nThe number be remained in final is: ", end=" ")
		qu.QueueTraverse()




	def TestJosephus(self):
		PeopleNum = int(input("Please input the number of total people: "))
		Gap = int(input("Please input the number of which is to be out of the Queue: "))
		if PeopleNum > 0 and Gap > 0 and Gap <= PeopleNum:
			self.Josephus(PeopleNum, Gap)
		else:
			print("The input does not fit the requirement.")
			
			
jp = LinkQueue()
jp.TestJosephus()
