#I create this file to test my understanding degree of recursion program about binary tree.
#how to tranform a binary tree(use post-order traverse)into a double linked list?

class BinaryTreeNode:
	def __init__(self):
		self.data = None
		self.lchild = None
		self.rchild = None
		
class Test:
	def __init__(self):
		self.pHead = None
		self.pEnd = None
		
	def arrayToTree(self, array, start, end):
		if start <= end:
			root = BinaryTreeNode()
			mid = (start+end+1)//2
			root.data = array[mid]
			root.lchild = self.arrayToTree(array, start, mid-1)
			root.rchild = self.arrayToTree(array, mid+1, end)
		else:
			root = None
		return root
			
	def TreeToLinkedlist(self, root):
		if root == None:
			return
		self.TreeToLinkedlist(root.lchild)
		root.lchild = self.pEnd
		if self.pEnd == None:
			self.pHead = root
		else:
			self.pEnd.rchild = root
		self.pEnd = root
		self.TreeToLinkedlist(root.rchild)
		
		
if __name__ == "__main__":
	arr = [1, 2, 4, 5, 6, 7, 8]
	test = Test()
	root = test.arrayToTree(arr, 0, len(arr)-1)
	test.TreeToLinkedlist(root)
	print("The direct traverse through the double linked list is:")
	cur = test.pHead
	while cur != None:
		print(cur.data)
		cur = cur.rchild
	print("\n")
	print("The inverse traverse through the double linked list is:")
	cur = test.pEnd
	while cur != None:
		print(cur.data)
		cur = cur.lchild
	
