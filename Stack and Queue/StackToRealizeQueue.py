#用两个栈来模拟线性队列的操作
#唯一的难点在于实现先进先出的队列特点，利用元素经过两次进栈后的栈内顺序与首次进入队列是的队内顺序是一样的这一特点
from SequenceStack import SequenceStack

class StackToQueue():
	def __init__(self):
		self.stackOne = SequenceStack()
		self.stackTwo = SequenceStack()

		
	def IsEmptyQueue(self):
		if self.stackOne.IsEmptyStack() and self.stackTwo.IsEmptyStack():
			return True
		return False
		
	def PushQueue(self, data):
		if self.stackOne.IsEmptyStack() and self.stackTwo.IsEmptyStack():
			self.stackOne.PushStack(data)
		else:
			if self.stackOne.IsEmptyStack():
				stackA = self.stackOne
				stackB = self.stackTwo
			else:
				stackB = self.stackOne
				stackA = self.stackTwo
			while not stackB.IsEmptyStack():
				popElement = stackB.PopStack()
				stackA.PushStack(popElement)
			stackA.PushStack(data)
			while not stackA.IsEmptyStack():
				popElement = stackA.PopStack()
				stackB.PushStack(popElement)

		
	def PopQueue(self):
		if self.stackOne.IsEmptyStack() and self.stackTwo.IsEmptyStack():
			return
		if not self.stackOne.IsEmptyStack():
			self.stackOne.PopStack()
		if not self.stackTwo.IsEmptyStack():
			self.stackTwo.PopStack()
	
	def GetLen(self):
		if self.stackOne.IsEmptyStack() and self.stackTwo.IsEmptyStack():
			return 0
		elif not self.stackOne.IsEmptyStack():
			return self.stackOne.top + 1
		else:
			return self.stackTwo.top + 1
			
	def QueueTraverse(self):
		if self.stackOne.IsEmptyStack() and self.stackTwo.IsEmptyStack():
			return
		elif not self.stackOne.IsEmptyStack():
			while not self.stackOne.IsEmptyStack():
				popElement = self.stackOne.PopStack()
				self.stackTwo.PushStack(popElement)
				print(popElement, end = ",")
			return
		else:
			while not self.stackTwo.IsEmptyStack():
				popElement = self.stackTwo.PopStack()
				self.stackOne.PushStack(popElement)
				print(popElement, end = ",")
			return
	
if __name__ == "__main__":
	stq = StackToQueue()
	stq.IsEmptyQueue()
	stq.PushQueue(3)
	stq.PushQueue(5)
	stq.PushQueue(7)
	stq.PopQueue()
	print(stq.GetLen())
	stq.QueueTraverse()
		
	
