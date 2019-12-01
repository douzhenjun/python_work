#已知两个链表head1和head2各自有序,请把他们合并成一个链表,要求合并后的链表依然有有序.
#分别用head1,head2来遍历两个链表,如果当前head1指向的数据小于head2指向的数据,则将
#head1指向的结点归入合并后的链表中,否则,将head2指向的结点归入合并后的链表中.如果有
#一个链表遍历结束,则把未结束的链表连接到合并后的链表尾部.
class Node:
	def __init__(self, x=None):
		self.data = x
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head1 = Node()
		self.head2 = Node()
		
	def Traverse(self, head):
		pNode = head.next
		while True:
			if pNode.next == None:
				print(pNode.data)
				return
			else:
				print(pNode.data, end="->")
				pNode = pNode.next
	
	def ConstructLinkedList(self):
		cNode = self.head1
		for i in range(2, 9, 2):
			dNode = Node(i)
			cNode.next = dNode
			cNode = cNode.next
		print("The original linkedlist is: ")
		head = self.head1
		self.Traverse(head)
		
		cNode = self.head2
		for i in range(4, 8, 2):
			dNode = Node(i)
			cNode.next = dNode
			cNode = cNode.next
		print("The original linkedlist is: ")
		head = self.head2
		self.Traverse(head)
	
	def MergeTwoOrderedLinkedList(self):
		p1 = self.head1.next
		p2 = self.head2.next
		if p1.data < p2.data:
			p = self.head1
		else:
			p = self.head2
			
		while p1 != None and p2 != None:
			if p1.data < p2.data:
				p.next = p1
				p = p.next
				p1 = p1.next
			else:
				p.next = p2
				p = p.next
				p2 = p2.next
			
		if p1 == None and p2 != None:
			p.next = p2
		if p2 == None and p1 != None:
			p.next = p1
			
		if self.head1.next.data < self.head2.next.data:
			head = self.head1
		else:
			head = self.head2
		print("The present linkedlist is: ")
		self.Traverse(head)

if __name__ == "__main__":
	ll = LinkedList()
	ll.ConstructLinkedList()
	ll.MergeTwoOrderedLinkedList()
