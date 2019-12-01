#print binary tree node layer by layer
from BinaryTree import BinaryTreeNode
from SequenceQueue import SequenceQueue
	
def ArrayToTree(arr, start, end):
	root = None
	if end >= start:
		root = BinaryTreeNode()
		mid = (start+end+1)//2
		root.data = arr[mid]
		root.lchild = ArrayToTree(arr, start, mid-1)
		root.rchild = ArrayToTree(arr, mid+1, end)
	else:
		root = None
	return root 

def PrintTreeLayer(root):
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
	arr = [1,2,3,4,5,6,7,8,9]
	root = ArrayToTree(arr, 0, len(arr)-1)
	print("The result of the layer-traverse is: ")
	PrintTreeLayer(root)
		
