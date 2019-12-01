#把二叉树转化为双向链表
#问题描述:输入一个二叉树，将该二叉树转换成一个排序的双向链表。要求不能创建新的结点，只能调整结点的指向。
#分析:由于转换后的双向链表中节点的顺序与二叉树中的中序遍历的顺序相同，因此，可以对二叉树的中序遍历进行修改。
#	通过在中序遍历的过程中修改节点的指向来转换成一个排序的双向链表。假设当前的遍历结点为root,root的左子树已经
#	被转换成双向链表，使用两个变量pHead, pEnd分别指向链表的头结点和尾结点。现在在遍历root结点的时候，只需要将
#	root结点的lchild指向pEnd，把pEnd的rchild指向root，此时root结点就被加入到双向链表中了。因此，root变成了
#	双向链表的尾结点。对于所有的结点都可以通过这种方法来修改节点的指向。因此可以用递归的方法来求解。

class BiTNode:
	def __init__(self):
		self.data = None
		self.lchild = None
		self.rchild = None

class Test:
	def __init__(self):
		self.pHead = None
		self.pEnd = None
		
	def arraytotree(self, arr, start, end):
		root = None
		if end >= start:
			root = BiTNode()
			mid = (start+end+1)//2
			root.data = arr[mid]
			root.lchild = self.arraytotree(arr, start, mid-1)
			root.rchild = self.arraytotree(arr, mid+1, end)
		else:
			root = None
		return root
		
	def inOrderBSTree(self, root):
		if root == None:
			return
		
		self.inOrderBSTree(root.lchild)
		root.lchild = self.pEnd
		if None == self.pEnd:
			self.pHead = root
		else:
			self.pEnd.rchild = root
		self.pEnd = root
		self.inOrderBSTree(root.rchild)
		
		
if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6, 7]
	test = Test()
	root = test.arraytotree(arr, 0, len(arr)-1)
	test.inOrderBSTree(root)
	print("The direct traverse in the double linked list which is transformed is:")
	cur = test.pHead
	while cur != None:
		print(cur.data)
		cur = cur.rchild
	print("\n")
	print("The inverse traverse in the double linked list which is transformed is:")
	cur = test.pEnd
	while cur != None:
		print(cur.data)
		cur = cur.lchild
