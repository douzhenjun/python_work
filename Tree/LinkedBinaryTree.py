#链表表示二叉树
class tree():
	def __init__(self):
		self.data = 0 
		self.left = None
		self.right = None
	
def create_tree(root, val):
	newnode = tree()
	newnode.data = val
	newnode.left = None
	newnode.right = None
	if root == None:
		root = newnode
		return root
	else:
		current = root
	while current != None:
		backup = current
		if current.data > val:
			current = current.left
		else:
			current = current.right
	if backup.data > val:
		backup.left = newnode
	else:
		backup.right = newnode
	return root 

def inorder(ptr):
	if ptr != None:
		inorder(ptr.left)
		print("[%2d]"%ptr.data, end='')
		inorder(ptr.right)
	
# data = [5,6,24,8,12,3,17,1,9]
# ptr = None
# root = None
# for i in range(9):
	# ptr = create_tree(ptr, data[i])
# print("The leftchild is:")
# root = ptr.left
# while root != None:
	# print("%d"%root.data)
	# root = root.left
# print('----------------------------------------')
# print("The rightchild is:")
# while root != None:
	# print("%d"%root.data)
	# root = root.right
# print()

data = [5,6,24,8,12,3,17,1,9]
ptr = None
root = None
for i in range(9):
	ptr = create_tree(ptr, data[i])
print("------------------------------------")
print("The result after in rank: ")
inorder(ptr)
print("")












	
