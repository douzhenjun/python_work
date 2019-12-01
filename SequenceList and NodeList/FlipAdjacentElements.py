#把链表的相邻元素翻转
#1->2->3->4->5->6->7转换为2->1->4->3->6->5->7
class Node:
	def __init__(self, x=None):
		self.data = x
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = Node()
		
	
	def Traverse(self):
		pNode = self.head.next
		while True:
			if pNode.next == None:
				print(pNode.data)
				return
			else:
				print(pNode.data, end="->")
				pNode = pNode.next
				
	def ConstructLinkedList(self):
		cNode = self.head
		for i in range(1, 9):
			dNode = Node(i)
			cNode.next = dNode
			cNode = cNode.next
		print("The original linkedlist is: ")
		self.Traverse()
		
	def FlipAdjacentElements(self):
		aNode = self.head
		bNode = self.head.next
		cNode = None
		dNode = None
		while  bNode != None and bNode.next != None:
			cNode = bNode.next
			dNode = cNode.next
			aNode.next = cNode
			cNode.next = bNode
			bNode.next = dNode
			aNode = cNode.next
			bNode = aNode.next
		print("The present linkedlist is: ")
		self.Traverse()
		
if __name__ == "__main__":
	ll = LinkedList()
	ll.ConstructLinkedList()
	ll.FlipAdjacentElements()
