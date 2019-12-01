from BinaryTree import BinaryTreeNode

def CreateBinaryTree(root, i):
	if i == 10:
		return root
	else:
		flag = True
		root.data = i
		if flag:
			root = root.lchild
			flag = -flag
			i += 1
			CreateBinaryTree(root, i)
		elif not flag:
			root = root.rchild
			flag = -flag
			i += 1
			CreateBinaryTree(root, i)

def printTreeMidOrder(root):
	if root == None:
		return 
	if root.lchild != None:
		printTreeMidOrder(root.lchild)
	print(root.data)
	if root.rchild != None:
		printTreeMidOrder(root.rchild)
		
if __name__ == "__main__":
	root = BinaryTreeNode()
	CreateBinaryTree(root, 1)
	printTreeMidOrder(root) 
			
