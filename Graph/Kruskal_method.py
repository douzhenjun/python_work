#Kruskal算法
VERTS = 6 #顶点数
class edge:
	def __init__(self):
		self.start = 0	#边的起点
		self.to = 0		#边的终点
		self.find = 0	#记录边是否被遍历过
		self.val = 0	#记录权值
		self.next = None#存储下一个链表的地址

v = [0]*(VERTS+1)

def findmincost(head):  #搜索成本最小的边，其中head表示从这个顶点开始寻找最小成本的边
	minval = 100		#初始化一个最小权值
	ptr = head			#初始化一个指针(pointer)
	while ptr != None:
		if ptr.val < minval and ptr.find == 0:
			minval = ptr.val
			retptr = ptr
		ptr = ptr.next
	retptr.find = 1		#将retptr设为已找到的边
	return retptr		#返回retptr
	
def mintree(head):		#最小生成树函数
	global VERTS
	result = 0
	ptr = head
	for i in range(VERTS):
		v[i] = 0
	while ptr != None:
		mceptr = findmincost(head)
		v[mceptr.start] = v[mceptr.start] + 1
		v[mceptr.to] = v[mceptr.to] + 1
		if v[mceptr.start] > 1 and v[mceptr.to] > 1:
			v[mceptr.start] = v[mceptr.start] - 1
			v[mceptr.to] = v[mceptr.to] - 1
			result = 1
		else:
			result = 0
		if result == 0:
			print("start vertex [%d] -> eventual vertex [%d] -> routine length [%d]"
					%(mceptr.start, mceptr.to, mceptr.val))
		ptr = ptr.next

#成本表数组
# data = [[1,2,6],[1,6,12],[1,5,10],[2,3,3],
		# [2,4,5],[2,6,8],[3,4,7],[4,6,11],
		# [4,5,9],[5,6,16]]
data = [[1,2,6],[2,3,3],[2,4,5],[2,6,8],[3,4,7],[1,6,12],[1,5,10],[4,5,9],[4,6,11],[5,6,16]]
head = None
#建立新的链表

for j in range(1,VERTS+1):
	for i in range(len(data)):
		if data[i][0] == j:
			newnode = edge()
			newnode.start = data[i][0]
			newnode.to = data[i][1]
			newnode.val = data[i][2]
			newnode.find = 0
			newnode.next = None
			if head == None:
				head = newnode
				head.next = None
				ptr = head
			else:
				ptr.next = newnode
				ptr = ptr.next
print("-----------------------------------")
print("建立最小生成树:")
print("-----------------------------------")
mintree(head)
