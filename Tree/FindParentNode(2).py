import math

class BiTNode:
	def __init__(self):
		self.data = None
		self.lchild = None
		self.rchild = None
		
def arraytotree(arr, start, end):
	root = BiTNode()
	if start <= end:
		mid = (start + end + 1) // 2
		root.data = array[mid]
		root.lchild = arraytotree(arr, start, mid-1)
		root.rchild = arraytotree(arr, mid+1, end)
	else:
		return root
	
class IntRef:
	def __init__(self):
		self.num = None
		
def getNo(root, node, number):
	if root == None:
		return False
	if root == node:
		return True
	tmp = number.num
	number.num = 2 * tmp
	if getNo(root.lchild, node, number):
		return True
	else:
		number.num = tmp * 2 + 1
		return getNo(root.rchild, node, number)
		
def getNodeFromNum(root, number):
	if root == None or number < 0:
		return None
	if number == 1:
		return root
	lens = int((math.log(number)/math.log(2)))
	number -= 1 << lens
	while lens > 0:
		if (1 << (lens -1)) & number == 1:
			root = root.rchild
		else:
			root = root.lchild 
		lens -= 1
	return root 
	

def FindParentNode(root, node1, node2):
	ref1 = IntRef()
	ref1.num = 1
	ref2 = IntRef()
	ref2.num = 1
	getNo(root, node1, ref1)
	getNo(root, node2, ref2)
	num1 = ref1.num
	num2 = ref2.num
	while num1 != num2:
		if num1 > num2:
			num /= 2
		else:
			num2 /= 2
	return getNodeFromNim(root, num1)
	
