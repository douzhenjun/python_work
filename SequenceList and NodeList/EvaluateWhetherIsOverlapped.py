#判断有环单链表是否相交
'''类似于无环单链表相交的情况，如果相交，那么一定尾结点相同。而有环单链表是没有尾结点的，所有只要
	相交，就一定共享环。所以思路是，首先判断head1,head2是否有环，再找出head1的环的入口，看它是否也在
	head2中，若是，则head1与head2有相交部分，否则没有。
'''
class LNode:
	def __init__(self, x = None):
		self.data = x
		self.next = None

class LinkedList:
	def __init__(self):
		self.head1 = LNode()
		self.head2 = LNode()
		
	def constructList(self):
		i = 1
		tmp = None
		cur = self.head1
		while i < 8:
			tmp = LNode(i)
			cur.next = tmp
			cur = tmp
			i += 1 
		cur.next = self.head1.next.next.next

		j = 1
		tmp = None
		cur = self.head2
		while j < 6:
			tmp = LNode(j)
			cur.next = tmp
			cur = tmp
			j += 1
		cur.next = self.head1.next.next
	
	
def Traverse(head):
	pNode = head.next
	index = 1
	while index < 15:
		if pNode.next == None:
			print(pNode.data)
			return
		else:
			print(pNode.data, end="->")
			pNode = pNode.next
			index += 1

	
def isLoop(head):
	slow = head.next
	fast = head.next
	while fast != None and fast.next != None:
		fast = fast.next.next
		slow = slow.next
		if slow == fast:
			return slow
	return None

def findLoopNode(head, meetNode):
	p = head
	q = meetNode
	num = 1
	while p != q:
		p = p.next
		q = q.next
		num += 1
	return num

#单链表无环时，判断是否相交
def IsIntersect(head1, head2):
	temp1 = head1.next
	temp2 = head2.next
	n1,n2 = 0,0
	while temp1.next != None:
		temp1 = temp1.next
		n1 += 1
	while temp2.next != None:
		temp2 = temp2.next
		n2 += 1
	if temp1 == temp2:			#如果head1和head2有相同的尾结点,说明有相交部分
		if n1 > n2:
			while n1 - n2 > 0:
				head1 = head1.next
				n1 -= 1
		if n2 > n1:
			while n2 - n1 > 0:
				head2 = head2.next
				n2 -= 1
		while head1 != head2:
			head1 = head1.next
			head2 = head2.next
		print("These two LinkedLists are overlapped from the node",head1.data,".")
	else:						#否则没有相交部分
		print("These two LinkedLists have no overlapped part.")

	
if __name__ == "__main__":
	ll = LinkedList()
	head1 = ll.head1
	head2 = ll.head2
	Traverse(head1)
	Traverse(head2)
	meetNode1 = isLoop(head1)
	index = 0
	MAXSIZE = 100
	if meetNode1 == None:												#分类讨论：首先判断第一个链表是否有环。分两种情况：
		meetNode2 = isLoop(head2)
		print(meetNode2)												#(1)如果第一个链表无环，分两种情况：
		if meetNode2 == None:											#(1.1)如果第二个链表有环，则不相交；
			IsIntersect(head1, head2)									#(1.2)如果第二个链表无环，按照无环的isIntersect()函数判断是否相交。
		else:															#(2)如果第一个链表有环，分两种情况：
			print("These two LinkedLists have no overlapped part.")		#(2.1)如果第二个链表有环，分两种情况：
	else:																#(2.1.1)如果第一个链表的环的某一个节点包含在第二个链表中，则相交；
		meetNode2 = isLoop(head2)										#(2.1.2)如果第一个链表的环的某一个节点不在第二个链表中，则不相交；
		if meetNode2 == None:											#(2.2)如果第二个链表无环，则不相交。
			print("These two LinkedLists have no overlapped part.")
		else:
			pNode = self.head2
			while pNode != meetNode1:
				pNode = pNode.next
				index += 1
				if index > MAXSIZE:
					print("These two LinkedLists have no overlapped part.")
					break
			if index < MAXSIZE:
				print("These two LinkedLists are overlapped from the node",pNode.data,".")
