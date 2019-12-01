#a class of DoubleLinkedList双链表类
#判断这个链表是不是对称的

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prior = None

class DoubleLinkedList():
	def __init__(self):
		self.head = Node(None)
		
		
		
	def CreateDoubleLinkedList(self):
		print("****************************************")
		print("Please input the element, press 'Enter' \n to end the input.")
		print("****************************************")
		Element = input("Please input the element: ")
		cNode = self.head
		while Element != '#':
			nNode = Node(Element)
			cNode.next = nNode
			nNode.prior = cNode
			cNode = cNode.next
			Element = input("Please input the element: ")
		
	def GetLength(self):
		cNode = self.head
		n = 0
		while cNode.next != None:
			cNode = cNode.next
			n += 1
		return n
	
	def IsEmpty(self):
		if self.GetLength() == 1:
			return False
		else:
			return True
	
	def InsertElementInTail(self):
		Element = input("Please input the element which is to be inserted in the tail of the list: ")
		cNode = self.head
		while cNode.next != None:
			cNode = cNode.next
		cNode.next = Node(Element)
		Node(Element).prior = cNode
		
		dNode = self.head
		print("The present list is: \n")
		print("Head <->", end = ' ')
		while dNode.next != None:
			dNode = dNode.next
			print(dNode.data,"<->",end = ' ')
		print("None\n")
		
	
	def InsertElement(self):
		i = int(input("Please input the index of the node which to be inserted: "))
		Element = input("Please input the element of this node: ")
		cNode = self.head
		nNode = Node(Element)
		j = 0
		while cNode.next != None and j<i:
			cNode = cNode.next
			j += 1
		nNode.next = cNode
		nNode.prior = cNode.prior
		cNode.prior.next = nNode 
		cNode.prior = nNode
		
		dNode = self.head
		print("The present list is: \n")
		print("Head <->", end = ' ')
		while dNode.next != None:
			dNode = dNode.next
			print(dNode.data,"<->",end = ' ')
		print("None\n")
		
		
	#delete nodes which have the target element	
	def DeleteElement(self):
		Element = input("Please input the element to be deleted: ")
		cNode = self.head
		pNode = self.head
		n = self.GetLength()
		while cNode.next != None:
			pNode = cNode
			cNode = cNode.next
			if cNode.data == Element:
				pNode.next = cNode.next
				cNode.next.prior = pNode
				cNode = cNode.prior	
		if self.GetLength() == n:
			print("There is no target element to be deleted in this list!")
					
		dNode = self.head
		print("The present list is: \n")
		print("Head <->", end = ' ')
		while dNode.next != None:
			dNode = dNode.next
			print(dNode.data,"<->",end = ' ')
		print("None\n")
	
	def TraverseElement(self):
		dNode = self.head
		print("The present list is: \n")
		print("Head <->", end = ' ')
		while dNode.next != None:
			dNode = dNode.next
			print(dNode.data,"<->",end = ' ')
		print("None\n")

#To judge whether the list is symmetry
	def JudgeSymmetry(self):
		cNode = self.head.next
		dNode = self.head
		while dNode.next != None:
			dNode = dNode.next
		n = 0
		m = self.GetLength()-1
		if self.GetLength()%2 == 0:
			while(n<=m):
				if cNode.data != dNode.data:
					print("The list is unsymmetry.")
					break
				else:
					cNode = cNode.next
					n +=1
					dNode = dNode.prior
					m -= 1
		if n>m:
			print("The list is symmetry.")

		elif self.GetLength()%2 == 1:
			while(n!=m):
				if cNode.data != dNode.data:
					print("The list is unsymmetry.")
					break
				else:
					cNode = cNode.next
					n +=1
					dNode = dNode.prior
					m -= 1
		if n==m:
			print("The list is symmetry.")
			
A = DoubleLinkedList()
A.CreateDoubleLinkedList()
A.JudgeSymmetry()
B = DoubleLinkedList()	
B.CreateDoubleLinkedList()							
B.JudgeSymmetry()




			
