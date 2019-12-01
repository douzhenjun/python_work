#对链表进行重新排序
#给定链表L0->L1->L2...->Ln-1->Ln,重新排序为L0->Ln->L1->Ln-1->L2...
#要求:1.不能申请新的结点 2.只能修改节点的next域,不能修改data域
SIZE = 8

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
	
	def ResortLinkedList(self):
		cNode = self.head
		for i in range(1, SIZE+1):
			dNode = Node(i)
			cNode.next = dNode
			cNode = cNode.next
		print("The initial element in linkedlist is: ")
		self.Traverse()
		
		dNode = self.head
		num = 0
		while dNode.next != None:
			dNode = dNode.next
			num += 1
			if num == SIZE//2:
				tmp = dNode
		dmp = dNode
		for i in range(SIZE//2, 1, -1):
			num = 1
			tNode = tmp
			while num < i:
				tNode = tNode.next
				num += 1
			dNode.next = tNode
			dNode = dNode.next
		dNode.next = None
		tmp.next = None		

		pNode = self.head.next
		qNode = dmp
		cNode = qNode
		while qNode != None:
			qNode = qNode.next
			cNode.next = pNode.next
			pNode.next = cNode
			pNode = cNode.next
			cNode = qNode
		print("The present linklist which is resorted is: ")
		self.Traverse()

if __name__ == "__main__":

	ll = LinkedList()
	ll.ResortLinkedList()
