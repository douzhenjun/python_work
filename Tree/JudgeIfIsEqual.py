#如何判断两个二叉树相等

class BiTNode:
	def __init__(self):
		self.data = None
		self.lchild = None
		self.rchild = None
		
	
def isEqual(root1, root2):
	if root1 == None and root2 == None:
		return True
	if root1 == None and root2 != None:
		return False
	if root1 != None and root2 == None:
		return False
	if root1.data == root2.data:
		return isEqual(root1.lchild, root2.lchild) and isEqual(root1.rchild, root2.rchild)
	else:
		return False
		
def constructTree1():
	root = BiTNode()
	node1 = BiTNode()
	node2 = BiTNode()
	node3 = BiTNode()
	node4 = BiTNode()
	root.data = 5
	node1.data = 3
	node2.data = -7
	node3.data = -1
	node4.data = 9
	root.lchild = node1
	root.rchild = node2
	node1.lchild = node3
	node1.rchild = node4
	return root

def constructTree2():
	root = BiTNode()
	node1 = BiTNode()
	node2 = BiTNode()
	node3 = BiTNode()
	node4 = BiTNode()
	root.data = 5
	node1.data = 3
	node2.data = -7
	node3.data = -1
	node4.data = 9
	root.lchild = node1
	root.rchild = node2
	node1.lchild = node3
	node1.rchild = node4
	return root

def TraverseInPreOrder(root):
	if root == None:
		return
	print(root.data)
	TraverseInPreOrder(root.lchild)
	TraverseInPreOrder(root.rchild)

if __name__ == "__main__":
	root1 = constructTree1()
	root2 = constructTree2()
	TraverseInPreOrder(root1)
	print("\n")
	TraverseInPreOrder(root2)
	equal = isEqual(root1, root2)
	if equal:
		print("These two trees are equal.")
	else:
		print("These two trees are not equal.")		
