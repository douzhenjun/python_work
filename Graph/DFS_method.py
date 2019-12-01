#Depth-First Search
VERTS = 7
class list_node:
	def __init__(self):
		self.val = 0
		self.next = None
		
head = [list_node()]*9
run = [0]*9

def dfs(current):
	run[current] = 1
	print('[%d]' %current, end='')
	ptr = head[current].next
	while ptr != None:
		if run[ptr.val] == 0:
			dfs(ptr.val)
		ptr = ptr.next
		
# data = [[1,2],[2,1],[1,3],[3,1],
		# [2,4],[4,2],[2,5],[5,2],
		# [3,6],[6,3],[3,7],[7,3],
		# [4,8],[8,4],[5,8],[8,5],
		# [6,8],[8,6],[8,7],[7,8]]
data = [[1,3],[1,2],[2,7],[3,4],[3,5],[7,6],[6,2]]
for i in range(1,VERTS+1):
	run[i] = 0                                                          #记录是否已被遍历过
	head[i] = list_node()
	head[i].val = i
	head[i].next = None
	ptr = head[i]
	for j in range(len(data)):
		if data[j][0] == i:
			newnode = list_node()
			newnode.val = data[j][1]
			ptr.next = newnode
			ptr = ptr.next
print("The detail in graph's adjacentlist is:")
for i in range(1,VERTS+1):
	ptr = head[i]
	print('vertex %d=>'%i, end='')
	ptr = ptr.next
	while ptr != None:
		print('[%d]'%ptr.val, end='')
		ptr = ptr.next
	print()
print("The vertex by depth-first search is:")
dfs(1)
print()
