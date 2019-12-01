#如何对二叉树进行镜像翻转
#要实现这个事，需要交换二叉树的所有结点的左右孩子。可以用递归的方法去实现。
#思路：首先建立一个二叉树，采用中间元素作为根结点的方法，再设计一个函数将二叉树的所有左子树与右子树的元素互换。为了达到所有，
#采用递归，首先找到最小的左子树(距离根结点最远的左子树),再找到它的父结点的右子树,交换。递归终止条件为root==None,只有这样可以先把最小的两个子树交换位置，从而将
#所有的子树交换位置。最外层函数当根结点的左子树与右子树交换位置以后，函数结束。然后设计一个逐层打印结点函数，采用队列。
from SequenceQueue import SequenceQueue

class BiTNode:
	def __init__(self):
		self.data = None
		self.lchild = None
		self.rchild = None
		
def reverseTree(root):
	if root == None:
		return 
	reverseTree(root.lchild)
	reverseTree(root.rchild)
	tmp = root.lchild
	root.lchild = root.rchild
	root.rchild = tmp
	
def arraytotree(arr, start, end):
	root = None
	if end >= start:
		root = BiTNode()
		mid = (start+end+1)//2
		root.data = arr[mid]
		root.lchild = arraytotree(arr, start, mid-1)
		root.rchild = arraytotree(arr, mid+1, end)
	else:
		root = None
	return root
	
def printTreeLayer(root):
	if root == None:
		return 
	queue = SequenceQueue()
	queue.EnQueue(root)
	while queue.GetQueueLength() > 0:
		p = queue.ExQueue()
		print(p.data)
		if p.lchild != None:
			queue.EnQueue(p.lchild)
		if p.rchild != None:
			queue.EnQueue(p.rchild)
				
if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6, 7]
	root = arraytotree(arr, 0, len(arr)-1)
	print("The result of the binary-tree layer traverse is: ")
	printTreeLayer(root)
	print("\n")
	reverseTree(root)
	print("The result of the after-traversed binary-tree layer traverse is: ")
	printTreeLayer(root)
