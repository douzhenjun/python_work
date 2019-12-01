class BinaryTreeNode:
	def __init__(self):
		self.data = None
		self.lchild = None
		self.rchild = None
		
	
def ArrayToTree(array, start, end):
	if end >= start:
		root = BinaryTreeNode()
		mid = (start + end + 1)//2
		root.data = array[mid]
		root.lchild = ArrayToTree(array, start, mid-1)
		root.rchild = ArrayToTree(array, mid+1, end)
	else:
		root = None
	return root

def printTreeMidOrder(root):
	if root == None:
		return 
	if root.lchild != None:
		printTreeMidOrder(root.lchild)
	print(root.data)
	if root.rchild != None:
		printTreeMidOrder(root.rchild)
		
if __name__ == "__main__":
	array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	print("The original list is :\n", array)
	print("\n")
	root = ArrayToTree(array, 0, len(array)-1)
	print("转换成树的中序遍历为: \n")
	printTreeMidOrder(root)

	
