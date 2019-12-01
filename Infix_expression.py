#Apply of binary tree:binary tree and stack to calculate the infix expression
#1.transform the infix expression into the postfix expression
#2.establish a binary tree by the form of postfix expression
#3.traverse the binary tree in preorder and get the prefix expression
#4.get the value of the prefix expression

class LinkedBinaryTreeNode():
	def __init__(self):
		self.data = '#'
		self.LeftChild = None
		self.RightChild = None
		
			

class InfixExpression():
	def __init__(self, expression):
		self.InfixExpression = expression
		self.PostfixExpression = []
		
	def InfixToPostfix(self):
		operator = []
		index = 0
		for item in self.InfixExpression:
			if index <= len(self.InfixExpression) - 1:
				item = self.InfixExpression[index]
				if item in ['+', '-', '*', '/']:
					while len(operator) >= 0:
						if len(operator) == 0:
							operator.append(item)
							break
						tmp = operator.pop()
						if tmp == '(' or self.Grade(item) > self.Grade(tmp):
							operator.append(tmp)
							operator.append(item)
							break
						else:
							self.PostfixExpression.append(tmp)
				elif item == '(':
					operator.append(item)
				elif item == ')':
					while len(operator) > 0:
						tmp = operator.pop()
						if tmp != '(':
							self.PostfixExpression.append(tmp)
						else:
							break
				elif item in "0123456789":
					if index < len(self.InfixExpression) - 1:
						for k in self.InfixExpression[index+1:]:
							if k in "0123456789":
								item = item + k
								index += 1
							else:
								break
					self.PostfixExpression.append(item)
				index = index + 1
			else:
				break
		while len(operator) > 0:
			self.PostfixExpression.append(operator.pop())
				
	def Grade(self, operator):
		if operator == '+':
			return 1
		elif operator == '-':
			return 1 
		elif operator == '*':
			return 2
		else:
			return 2
			
			
class BinaryTree():
	
	def __init__(self, PostfixExpression):
		self.PostfixExpression = PostfixExpression
		
	#By the format of Postfix expression to create the corresponding binary tree			
	def CreatePostfixBinaryTree(self, Root):
		StackTreeNode = []
		for  item in self.PostfixExpression:
			if item in ['+', '-', '*', '/']:
				OperandTwo = StackTreeNode.pop()
				OperandOne = StackTreeNode.pop()
				RootNode = LinkedBinaryTreeNode()						#初始化一个根节点,用来存储运算符,且孩子非空
				RootNode.data = item
				RootNode.LeftChild = OperandOne                         #the object out from the stackTreeNode in prior will
				RootNode.RightChild = OperandTwo                        #be the rootNode's LeftChild, and the object out from 
				StackTreeNode.append(RootNode)
				for i in StackTreeNode:
					print(i.data, end='')
				print()
																		#the stackTreeNode in next will be the rootNode's RightChild.
			else:
				TreeNode = LinkedBinaryTreeNode()						#初始化一个二叉树节点,用来存储数字或者运算符,如果存储运算符,则它实际上也是
				TreeNode.data = item									#前面所定义的根节点
				StackTreeNode.append(TreeNode)
				for i in StackTreeNode:
					print(i.data, end='')
				print()
		TreeNode = StackTreeNode.pop()
		Root.data = TreeNode.data
		Root.LeftChild = TreeNode.LeftChild
		Root.RightChild = TreeNode.RightChild
		print('Succeed in establishing the binary tree!')
		

	#To get the prefix expression of the given format
	def GetPrefixExpression(self, BinaryTree, expression):              #BinaryTree is a tree node which is introduced 
		if BinaryTree is not None:										#in the class:LinkedBinaryTreeNode.
			self.VisitBinaryTree(BinaryTree, expression)
			self.GetPrefixExpression(BinaryTree.LeftChild, expression)
			self.GetPrefixExpression(BinaryTree.RightChild, expression)
			
	def VisitBinaryTree(self, BinaryTree, expression):
		print(BinaryTree.data, end=' ')
		expression = expression.append(BinaryTree.data)

class PrefixExpression():
	
	def __init__(self):
		self.result = 0
								
	def GetValue(self, expression):
		StackValue = []
		index = len(expression) - 1
		while index >= 0:
			if expression[index] in ['+', '-', '*', '/']:
				OperandOne = StackValue.pop()
				OperandTwo = StackValue.pop()
				print(OperandOne, OperandTwo)
				result = self.Calculation(OperandOne, OperandTwo, expression[index])
				if result is 'error':
					print("The divisor can not be zero!")
					return
				StackValue.append(result)
				index = index - 1
			else:
				StackValue.append(int(expression[index]))
				index = index - 1
		result = StackValue.pop()
		self.result = result

	def Calculation(self, OperandOne, OperandTwo, operator):
		# OperandOne = eval(OperandOne)
		# OperandTwo = eval(OperandTwo)
		if operator == '+':
			return (OperandOne + OperandTwo)
		elif operator == '-':
			return (OperandOne - OperandTwo)
		elif operator == '*':
			return (OperandOne * OperandTwo)
		elif operator == '/':
			if OperandTwo == 0:
				return 'error'
			else:
				return (OperandOne/OperandTwo)

if __name__ == "__main__":		
	expression = '9+(3-1)*3+10/2'
	print("The infix expression is:", expression)
	#1.transform the infix expression into the postfix expression
	iexpression = InfixExpression(expression)
	iexpression.InfixToPostfix()
	print("The corresponding postfix expression is:", " ".join(iexpression.PostfixExpression))
	#2.establish a binary tree by the form of postfix expression
	print("Establish the binary tree by the postfix expression!")
	bt = BinaryTree(iexpression.PostfixExpression)
	root = LinkedBinaryTreeNode()
	bt.CreatePostfixBinaryTree(root)
	#3.traverse the binary tree in preorder and get the prefix expression
	expression = []
	print("The infix expression by traversing the binary in preorder is in the following: ")
	bt.GetPrefixExpression(root, expression)
	print(expression)
	#4.get the value of the prefix expression
	pexpression = PrefixExpression()
	pexpression.GetValue(expression)
	print('\n'+'Caluculating result:'+str(pexpression.result))
				
				
				
				
				
				
				
