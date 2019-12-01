#实现二叉树的各种基本操作
class BinaryTreeNode():
	def __init__(self):
		self.data = '#'
		self.LeftChild = None
		self.RightChild = None
	
class BinaryTree():
	def __init__(self):
		self.root = BinaryTreeNode()
		self.List = []

	def CreateBinaryTree(self):
		stackTreeNode = []
		cNode = self.root
		bNode = self.root
		while True:
			data = input("Please input the original root node: ")
			self.root.data = data
			if self.root.data == '#':
				print("You can not let the original root be empty!")
			else:
				stackTreeNode.append(self.root)
				self.List.append(self.root)
				break
		while True:
			print("Please input the data of ",stackTreeNode[-1].data,"(in LeftChild): ")
			data = input()
			dNode = BinaryTreeNode()
			cNode.LeftChild = dNode
			cNode = cNode.LeftChild
			cNode.data = data
			bNode = cNode
			stackTreeNode.append(cNode)
			self.List.append(cNode)
			if cNode.data == "#":
				stackTreeNode.pop()
				bNode = stackTreeNode[-1]
				print("Please input the data of",stackTreeNode[-1].data,"(in RightChild): ")
				data = input()
				dNode = BinaryTreeNode()
				bNode.RightChild = dNode
				bNode = bNode.RightChild
				bNode.data = data
				cNode = bNode
				stackTreeNode.append(bNode)
				self.List.append(bNode)
				while bNode.data == "#" :
					while True:
						stackTreeNode.pop()
						OperandOne = stackTreeNode[-1]
						OperandTwo = stackTreeNode[-2]
						if OperandTwo.RightChild == OperandOne:
							if len(stackTreeNode) == 2:
								print("The binary is successfully be created!")
								print("The present binary tree is:")
								for i in self.List:
									print(i.data, end=',')
								print()
								return
							else:
								continue
						break
					stackTreeNode.pop()
					bNode = stackTreeNode[-1]
					print("Please input the data of",stackTreeNode[-1].data,"(in RightChild): ")
					data = input()
					dNode = BinaryTreeNode()
					bNode.RightChild = dNode
					bNode = bNode.RightChild
					bNode.data = data
					cNode = bNode
					stackTreeNode.append(bNode)
					self.List.append(bNode)
								
	
	def PreOrder(self, Root):
		if Root is not None:
			self.VisitBinaryTreeNode(Root)
			self.PreOrder(Root.LeftChild)
			self.PreOrder(Root.RightChild)	
	
	
	def VisitBinaryTreeNode(self, BinaryTreeNode):
		if BinaryTreeNode.data != '#':
			print(BinaryTreeNode.data, end=",")


	
	def ModifyTreeNode(self):
		Element = input("Please input the data you want to modify: ")
		Value = input("Please input the data after be modified: ")
		index = 1
		for i in self.List:
			if i.data == Element:
				i.data = Value
				break
			index += 1
		if index < len(self.List):
			print("We succeed in finding the target data, the binary tree after modifying is:")
			print(self.PreOrder(self.root))
		else:
			print("sorry, we don't find the target data in contemporary binary tree!")
	
	
	def TraverseInPreOrder(self):
		for i in self.List:
			print(i.data,end=',')
		print()
	
	def AddRightChild(self):
		dList = []
		for i in self.List:
			if i.data != '#':
				dList.append(i)
		while True:	
			index = input("Please input the index of the tree node to be added: ")
			index = eval(index)
			if index > len(dList) or index <= 0:
				print("The index can not be more than the number of treeNodes or <=0!")
				continue
			elif dList[index-1].RightChild.data != '#':
				print("The node has the rightchild!")
				continue
			data = input("Please input the data of the treenode: ")
			dNode = BinaryTreeNode()
			dNode.data = data
			dList[index-1].RightChild = dNode
			print("We succeed in adding the node, the present binary tree is:")
			print(self.PreOrder(self.root))
			break
bt = BinaryTree()
bt.CreateBinaryTree()
# bt.TraverseInPreOrder()
# bt.PreOrder(bt.root)
# bt.ModifyTreeNode()
bt.AddRightChild()
			
			
		
