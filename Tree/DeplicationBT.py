#复制二叉树
#问题描述：给定一个二叉树结点，复制该树，返回新建树的根结点。
#分析：用给定的二叉树的根结点root来构造新的二叉树的方法为：首先创建新的结点dupTree,然后根据root结点来构造dupTree结点

class BiTNode:
	def __init__(self):
		self.data = None
		self.lchild = None
		self.rchild = None
	
def createDupTree(root):
	if root == None:
		return None
	dupTree = BiTNode()
	dupTree.data = root.data
	dupTree.lchild = createDupTree(root.lchild)
	dupTree.rchild = createDupTree(root.rchild)
	return dupTree
	
def printTreeMidOrder(root):
	if root == None:
		return
	if root.lchild != None:
		printTreeMidOrder(root.lchild)
	print(root.data)
	if root.rchild != None:
		printTreeMidOrder(root.rchild)

def constructTree():
		root = BiTNode()
		node1 = BiTNode()
		node2 = BiTNode()
		node3 = BiTNode()
		node4 = BiTNode()
		root.data = 6
		node1.data = 3
		node2.data = -7
		node3.data = -1
		node4.data = -9
		root.lchild = node1
		root.rchild = node2
		node1.lchild = node3
		node1.rchild = node4
		node2.lchild = node2.rchild = node3.lchild = node3.rchild=\
		node4.lchild = node4.rchild = None
		return root			
			
if __name__ == "__main__":
	root1 = constructTree()
	root2 = createDupTree(root1)
	print("The original binary tree's traverse in mid-order is:")
	printTreeMidOrder(root1)
	print("\n")
	print("The new binary tree's traverse in mid-order is:")
	printTreeMidOrder(root2)
