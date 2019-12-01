#从链表中移除重复项
#方法一：设置三个指针:outerptr,innerptr,innerpre,两个循环，outerptr每次向后移一位，同时innerptr从outerptr的下一位开始遍历一次链表，
#innerpre始终跟着innerptr,如果innerptr.data == outerptr.data,让innerpre跟innerptr的下一个结点连起来（跳过innerptr所指结点），
#同时innerptr继续向后遍历。outerptr遍历完链表，算法结束。
class Node:
	def __init__(self, x=None):
		self.data = x
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = Node()


	def CreateByInput(self):
		dNode = self.head
		while True:
			data = input("Please input the data:")
			if data != "#":
				cNode = Node(data)
				dNode.next = cNode
				dNode = dNode.next
			else:
				print("The present list is:")
				pNode = self.head.next
				while True:
					if pNode.next == None:
						print(pNode.data)
						return
					else:
						print(pNode.data, end="->")
						pNode = pNode.next

	def RemoveDuplicateItem(self):
		if self.head.next == None:
			return
		outerptr = self.head.next
		innerptr = None
		innerpre = None
		while outerptr != None:
			innerptr = outerptr.next
			innerpre = outerptr
			while innerptr != None:
				if innerptr.data == outerptr.data:
					tmp = innerptr
					innerptr = innerptr.next
					innerpre.next = innerptr
					del tmp
				else:
					innerptr = innerptr.next
					innerpre = innerpre.next 
			outerptr = outerptr.next

		print("The present list is:")
		pNode = self.head.next
		while True:
			if pNode.next == None:
				print(pNode.data)
				return
			else:
				print(pNode.data, end="->")
				pNode = pNode.next

#方法二：递归方法
#设置两个指针cur和pointer，其中cur指向head，pointer指向它下一位结点，这两个指针每次向后移一位，
#遇到重复项跟方法一类似，每次的head都是子链表的头结点，当head是最后一个结点时，程序结束。
def RemoveDuplicationRecursion(head):
	if head.next == None:							 #最内部，此时head表示链表的尾部结点
		return head
	pointer = None
	cur = head
	head.next = RemoveDuplicationRecursion(head.next)#子链表
	pointer = head.next
	while pointer != None:
		if head.data == pointer.data:
			cur.next = pointer.next
			pointer = cur.next
		else:
			pointer = pointer.next
			cur = cur.next
	return head


def RemoveDup(head):
	if head == None:
		return
	head.next = RemoveDuplicationRecursion()
					
				
i = 1
head = Node()
tmp = None
cur = head
while i < 7:
	tmp = Node()
	if i % 2 == 0:
		tmp.data = i + 1
	elif i % 3 == 0:
		tmp.data = i - 2
	else:
		tmp.data = i
	cur.next = tmp
	cur = tmp
	i += 1
print("删除重复节点前: ")
cur = head.next
while cur != None:
	print(cur.data, end=" ")
	cur = cur.next
print()
RemoveDuplicationRecursion(head)
print("删除重复节点后: ")
cur = head.next
while cur != None:
	print(cur.data, end=" ")
	cur = cur.next
print()
