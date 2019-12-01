#How to find the nearest parent node of two arbitrary nodes in a binary tree?
#如何找出排序二叉树上任意两个节点的最近的共同父节点？
#分析：路径对比法

from TranslationBToL import Test
class BiTNode:
	def __init__(self):
		self.data = None
		self.lchild = None
		self.rchild = None
		
class stack:
	def __init__(self):
		self.items = []
		
	def isEmpty(self):
		return len(self.items) == 0
		
	def size(self):
		return len(self.items)
		
	def peek(self):
		if not self.isEmpty():
			return self.items[len(self.items)-1]
		else:
			return None
			
	def pop(self):
		if len(self.items) > 0:
			return self.items.pop()
		else:
			print("The stack is empty!")
			return None
			
	def push(self, item):
		self.items.append(item)
		
def getPathFromRoot(root, node, s):
	if root == None:
		return False
	if root == node:
		s.push(root)
		return True
	if getPathFromRoot(root.lchild, node, s) or getPathFromRoot(root.rchild, node, s):
		s.push(root)
		return True
	return False
	
def FindParentNode(root, node1, node2):
	stack1 = stack()
	stack2 = stack()
	getPathFromRoot(root, node1, stack1)
	getPathFromRoot(root, node2, stack2)
	commonParent = None
	while stack1.peek() == stack2.peek():
		commonParent = stack1.peek()
		stack1.pop()
		stack2.pop()
	return commonParent

def TraverseInMiddleOrder(root):
	if root == None:
		return
	TraverseInMiddleOrder(root.lchild)
	print(root.data)
	TraverseInMiddleOrder(root.rchild)
	
def TraverseInPreOrder(root):
	if root == None:
		return
	print(root.data)
	TraverseInPreOrder(root.lchild)
	TraverseInPreOrder(root.rchild)
	
def TraverseInPostOrder(root):
	if root == None:
		return
	TraverseInPostOrder(root.lchild)
	TraverseInPostOrder(root.rchild)
	print(root.data)
	
if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	test = Test()
	root = test.arraytotree(arr, 0, len(arr)-1)
	TraverseInPostOrder(root)
	node1 = root.lchild.lchild.lchild
	node2 = root.lchild.rchild
	res = None
	res = FindParentNode(root, node1, node2)
	if res != None:
		print(str(node1.data),"and", str(node2.data), "'s nearest common parent node is:", str(res.data))
	else:
		print("There is no common parent node between these two nodes.")	
	
