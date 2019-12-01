#如何在二叉排序树中找出第一个大于中间值的结点
#对于一个二叉树，令f=(最大值+最小值)/2,设计一个算法，找出距离f最近，大于f值的结点。
#分析：首先需要找出二叉排序树中的最大值和最小值。由于二叉排序树的特点是：对于任何一个结点，它的左子树的所有结点都小于这个结点的值，
#它的右子树的所有结点都大于这个结点的值。因此，在二叉排序树中最小值一定是最左下的结点，最大值一定是最右下的结点。根据最大值与最小值
#很容易就可以求出f的值。接下来对二叉树进行中序遍历。如果当前结点的值小于f，那么在这个结点的右子树中接着遍历，否则遍历这个结点的左子树。

class BiTNode:
	def __init__(self):
		self.data = None
		self.lchild = None
		self.rchild = None
		
def getMinNode(root):
	if root == None:
		return root
	while root.lchild != None:
		root = root.lchild
	return root
	
def getMaxNode(root):
	if root == None:
		return root
	while root.rchild != None:
		root = root.rchild
	return root
	
def getNode(root):
	maxNode = getMaxNode(root)
	minNode = getMinNode(root)
	mid = (maxNode.data + minNode.data)//2
	result = None
	while root != None:
		if root.data <= mid:
			root = root.rchild
		else:
			result = root
			root = root.lchild
	return result
	
def arraytotree(array, start, end):
	root = None
	if start <= end:
		root = BiTNode()
		mid = (start+end+1)//2
		root.data = array[mid]
		root.lchild = arraytotree(arr, start, mid-1)
		root.rchild = arraytotree(arr, mid+1, end)
	else:
		root = None
	return root	
		
if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6, 7]
	root = arraytotree(arr, 0, len(arr)-1)
	print(getNode(root).data)

