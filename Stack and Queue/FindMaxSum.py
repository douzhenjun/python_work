class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		

class IntRef:
	def __init__(self):
		self.val = None
		
def Max(a, b, c):
	maxs = a if a>b else b
	maxs = maxs if maxs > c else c
	return maxs
	
def findMaxPathRecursive(root, maxs):
	if None == root:
		return 0
	else:
		sumLeft = findMaxPathRecursive(root.left, maxs)
		sumRight = findMaxPathRecursive(root.right, maxs)
		allMax = root.val + sumLeft + sumRight
		leftMax = root.val + sumLeft
		rightMax = root.val + sumRight
		tmpMax = Max(allMax, leftMax, rightMax)
		if tmpMax > maxs.val:
			maxs.val = tmpMax
		subMax = sumLeft if sumLeft > sumRight else sumRight
		return root.val + subMax
		
def findMaxPath(root):
	maxs = IntRef()
	maxs.val = -2 ** 31
	findMaxPathRecursive(root, maxs)
	return maxs.val
	
if __name__ == "__main__":
	root = TreeNode(2)
	left = TreeNode(3)
	right = TreeNode(5)
	root.left = left
	root.right = right
	print(findMaxPath(root))
		
