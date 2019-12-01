#建立一个链式栈并实现其基本操作(进栈出栈，取栈顶元素，取元素个数，判断是否为空)
#设计一个岗哨top指针，规定它始终指向栈顶元素，在这里实际上就是尾部结点，弹栈操作从栈顶进行，入栈操作也从栈顶进行
class LNode:
	def __init__(self, x = None):
		self.data = x
		self.next = None
		

class MyLinkedListStack:
	def __init__(self):
		self.head = LNode()
		self.top = self.head
		
	def IsEmpty(self):
		if self.top == self.head:
			return True
		else:
			return False
	
	def GetSize(self):
		size = 0
		pNode = self.head.next
		while pNode != None:
			pNode = pNode.next
			size += 1
		return size
		
	def PushInStack(self, e):
		dNode = LNode(e)
		self.top.next = dNode
		self.top = self.top.next
		
	def PopInStack(self):
		if self.IsEmpty():
			print("The stack is empty!")
			return
		data = self.top.data
		cNode = self.head
		while cNode.next != self.top:
			cNode = cNode.next
		cNode.next = None
		self.top = cNode
		return data

		
	def GetTopElement(self):
		if self.IsEmpty():
			print("The stack is empty!")
			return
		return self.top.data
		
if __name__ == "__main__":
	stack = MyLinkedListStack()
	stack.PushInStack(1)
	stack.PushInStack(2)
	print("The top element of the stack is:", str(stack.GetTopElement()))
	print("The size of the stack is:", str(stack.GetSize()))
	print(stack.PopInStack())
	print("The stack is succefully poped!")
	print(stack.PopInStack())
