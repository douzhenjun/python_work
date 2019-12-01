#给定一棵二叉树，它的每个结点都是正整数和负整数，如何找到一棵子树，使得它的所有借结点的和最大？
class BiTNode:
	def __init__(self):
		self.data = None
		self.lchild = None
		self.rchild = None
	
class Test:
	def __init__(self):
		self.maxSum = -2**31

#方法功能:求最大子树；输入参数:root:根结点；maxRoot最大子树的根结点
#返回值:以root为根结点子树的所有结点的和

	def findMaxSubTree(self, root, maxRoot):
		if root == None:
			return 0
		lmax = self.findMaxSubTree(root.lchild, maxRoot)#左边子树结点和
		rmax = self.findMaxSubTree(root.rchild, maxRoot)#右边子树结点和
		sums = lmax + rmax + root.data
		if sums > self.maxSum:
			self.maxSum = sums
			maxRoot.data = root.data
		return sums

	def constructTree(self):
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
	test = Test()
	root = test.constructTree()
	maxRoot = BiTNode()
	test.findMaxSubTree(root, maxRoot)
	print("The sum of the biggest childtree is:", str(test.maxSum))
	print("The root node corresponding to the childtree is:", str(maxRoot.data))
	
