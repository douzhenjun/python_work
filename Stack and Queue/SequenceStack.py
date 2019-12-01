#定义一个用于顺序栈的基本操作的SequenceStack类

#initial
class SequenceStack():

	def __init__(self, Max=100):
		self.MaxStackSize = Max                                         #栈容量
		self.s = [None for x in range(0, self.MaxStackSize)]
		self.top = -1                                                   #栈指针
		
	def IsEmptyStack(self):
		if self.top == -1:
			iTop = True
		else:
			iTop = False
		return iTop

	#pushstack function	
	def PushStack(self, x):
		if self.top < self.MaxStackSize - 1:
			self.top = self.top + 1
			self.s[self.top] = x
		else:
			print("The stack is full.")
			return
			
	#return popstack element function
	def PopStack(self):
		if self.IsEmptyStack():
			return
		else:
			iTop = self.top
			self.top = self.top - 1
			return self.s[iTop]

	#get stack-top element		
	def GetTopStack(self):
		if self.IsEmptyStack():
			return
		else:
			return self.s[self.top]
			
		
	def StackTraverse(self):
		if self.IsEmptyStack():
			return
		else:
			for i in range(self.top, -1, -1):
				print(self.s[i], end=',')
			print()	
			
	def CreateStackByInput(self):
		data = input("Please input the element, press '#' to end the operation: ")
		while data != '#':
			self.PushStack(data)
			data = input("Please input the element: ")
			

if __name__ == "__main__":
	ss1 = SequenceStack()
	ss2 = SequenceStack()				
	string =input("Please input the string: ")		
	for i in range(0,len(string)):
		ss1.PushStack(string[i])

	for j in range(len(string)-1,-1,-1):
		ss2.PushStack(string[j])

	while not ss1.IsEmptyStack():
		if ss1.PopStack() != ss2.PopStack():
			print("It is not a palindrome(回文诗).")
			break
		else:
			continue
	if ss1.IsEmptyStack():
		print("It is a palidrome(回文诗).")









