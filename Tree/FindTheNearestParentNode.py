#给定一个给定的排序二叉树，求两个结点a,b的最近共同父结点。
#方法：路径对比法。对于一棵二叉树的两个结点，如果知道了从根结点到这两个结点的路径，就可以很容易地求出他们最近的公共父结点。
#		比如这样一个二叉树(层序遍历):6->3->9->2->5->8->10->1->None->4->None->7->None->None->None.
#		从根结点到结点1的路径为6->3->2->1,从根结点到结点5的路径为6->3->5,然后遍历这两条路径，只要是相等的结点就是他们的公共
#		父结点，找到最后一个相等的结点，也就是第一个不相等的结点的上一个结点，就是我们这里需要的最近公共父结点。
#分析：建立两个线性栈，分别存储从根结点到结点a以及从根结点到结点b的路径，(这里用一个函数去实现)再分别执行出栈操作，出栈条件为栈顶元素相同，
#	当停止出栈时，栈顶元素不相同，也就是此时的出栈元素(无论是stack1还是stack2的出栈元素，总之是一样的)c就是我们需要的最近公共父结点。

from SequenceQueue import SequenceQueue

class BinaryTreeNode:
	def __init__(self, data = None):
		self.data = data
		self.lchild = None
		self.rchild = None
		
def constructTree(root):
	root = BinaryTreeNode(6)
	node1 = BinaryTreeNode(3)
	node2 = BinaryTreeNode(9)
	node3 = BinaryTreeNode(2)
	node4 = BinaryTreeNode(5)
	node5 = BinaryTreeNode(8)
	node6 = BinaryTreeNode(10)
	node7 = BinaryTreeNode(1)
	node8 = BinaryTreeNode(4)
	node9 = BinaryTreeNode(7)
	root.lchild = node1
	root.rchild = node2
	node1.lchild = node3
	node1.rchild = node4
	node2.lchild = node5
	node2.rchild = node6
	node3.lchild = node7
	node4.lchild = node8
	node5.lchild = node9
	return root


def TraverseInPreOrder(root):
	if root == None:
		return
	print(root.data)
	TraverseInPreOrder(root.lchild)
	TraverseInPreOrder(root.rchild)
	
	
def storePathMethod(root, data, queue):
	if root == None:
		return False
	if root.data == data:
		queue.EnQueue(root.data)
		return True
	if storePathMethod(root.lchild, data, queue) or storePathMethod(root.rchild, data, queue):
		queue.EnQueue(root.data)
		return True
	return False

		
		
if __name__ == "__main__":
	root = BinaryTreeNode()
	root = constructTree(root)
	TraverseInPreOrder(root)
	queue1 = SequenceQueue()
	queue2 = SequenceQueue()
	node1 = 1
	node2 = 5
	print("Two target nodes are", node1,"and", node2,".")
	storePathMethod(root, node1, queue1)
	storePathMethod(root, node2, queue2)
	queue1.QueueTraverse()
	queue2.QueueTraverse()
	node = None
	while queue1.GetHead() == queue2.GetHead():
		node = queue1.ExQueue()
		queue2.ExQueue()
		print(node)
	print("The nearest parent node between these two nodes is", node,".")

