#判断两个单链表是否交叉
#如果相交，找到第一次相交时候的结点
class Node:
	def __init__(self, x = None):
		self.data = x
		self.next = None
		
	
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
		return head1
	else:						#否则没有相交部分
		return None
	
if __name__ == "__main__":
	i = 1
	head1 = Node()
	head2 = Node()
	tmp = None
	cur1 = head1
	p = None
	#构造第一个链表
	while i < 8:
		tmp = Node(i)
		cur1.next = tmp
		cur1 = tmp
		if(i==5):
			p = tmp
		i += 1
		
	cur2 = head2
	#构造第二个链表
	i = 1
	while i < 5:
		tmp = Node(i)
		tmp.data = i
		tmp.next = None
		cur2.next = tmp
		cur2 = tmp
		i += 1
	#使它们相交于结点5
	cur2.next = p
	interNode = IsIntersect(head1, head2)
	if interNode == None:
		print("These two linkedlists are not overlap.")
	else:
		print("These two linkedlists' overlapped node is",str(interNode.data))
		
