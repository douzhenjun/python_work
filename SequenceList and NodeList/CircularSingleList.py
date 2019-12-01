#define a class of Node
class Node():
	def __init__(self,data):
		self.data = data
		self.next = None

		
class CircularSingleLinkedList():
	def __init__(self):
		self.head = Node(None) #初始化节点函数，数据域为空，指针域为空
	
	#establish a circular single-linked list
	def CreateCircularSingleLinkedList(self):
			print("****************************************")
			print("*Please input data and ensure it by pressing 'enter',\nif you want to end, press '#'.*")
			print("****************************************")
			data = input("Please input the element of the code: ")
			cNode = self.head
			while data != '#':
				nNode = Node(int(data))
				cNode.next = nNode
				nNode.next = self.head
				cNode = cNode.next
				data = input("Please input the element of the code: ")
		
	def InsertElementInTail(self):
		Element = input("Please input the element you want to be inserted in the tail of the list: ")
		if Element == '#':
			return
		cNode = self.head
		while cNode.next != self.head:
			cNode = cNode.next
		nNode = Node(int(Element))
		cNode.next = nNode
		nNode.next = self.head
		#show the present list after inserting the element
		dNode = self.head
		print("The present single-linked list is: \n")
		print("head ->",end=' ')
		while dNode.next != self.head:
			print(dNode.next.data,"->",end=' ')
			dNode = dNode.next
		print("head\n")
		
	def InsertElementInHead(self):
		Element = input("Please input the element you want to be inserted in the head of the list: ")
		if Element == '#':
			return
		cNode = self.head
		nNode = Node(int(Element))
		nNode.next = cNode.next
		cNode.next = nNode
		#show the present list after inserting the element
		dNode = self.head
		print("The present single-linked list is: \n")
		print("head ->",end=' ')
		while dNode.next != self.head:
			print(dNode.next.data,"->",end=' ')
			dNode = dNode.next
		print("head\n")
	
	#get the length of the list(the number of nodes)		
	def GetLength(self):
		cNode = self.head
		length = 0
		while cNode.next != self.head:
			length = length + 1
			cNode = cNode.next
		return length
	
	#to find the number of i of the code in the list and output its data	
	def GetElement(self):
		i = int(input("Please input the number of code you want to find in the list: "))
		if i > self.GetLength():
			print("The i can not beyond the length of the list!")
		else:
			cNode = self.head
			n = 0
			while n < i:
				cNode = cNode.next
				n += 1
			print("The target element is",cNode.data)
	
	#to seek the target element of the list and return the index of the node 
	def FindElement(self):
		Element = int(input("Please input the element you want to find in the list: "))
		cNode = self.head
		n = 1
		while(cNode.next != self.head and cNode.data != Element):
			cNode = cNode.next	
			n += 1
		if n < self.GetLength():
			print("Successfully in find!The target element is in the number of",n-1,"of the list.")
		elif cNode.data == Element:
			print("Successfully in find!The target element is in the number of",n-1,"of the list.")
		else:
			print("Fail in find!There is not exist the element you want to find in the list.")
		
	#to delete elements in the single-linked list
	def DeleteElement(self):
		dElement = int(input("Please input the element you want to delete: "))
		cNode = self.head                                     #设置两个指针,每一次迭代指针往后走一步,一个指针先走,另一个指针跟着,
		pNode = self.head                                     #这样到跳出循环的时候,其中一个指针一定比另一个指针慢一个节点.这样做的好处
		if self.head.next == None:                            #是删除结点以后,指向该节点的指针也被删除,该节点的前驱与该节点的后继要凭借另一个
			print("The present single-linked list is empty!") #指针连在一起,而且该指针正好在我们需要它在的地方(靶节点的前驱节点处)
			return
		while cNode.next != self.head and cNode.data != dElement:   #遍历到倒数第二个节点为止,反证：如果遍历到最后一个节点,它包含目标函数的话，
			pNode = cNode                                     		#p指向c,而c指向none,此时c.data也是none,不等于dElement,所以会输出'要删除的
			cNode = cNode.next                                		#变量在这个单链表中不存在',这与基本事实矛盾.
		if cNode.data == dElement:
			pNode.next = cNode.next
			del cNode
			print("Successfully delete the code which contains the",dElement,".")
		else:
			print("Fail in delete for the present list does not have the node which has the",dElement,".")
		dNode = self.head
		print("The present single-linked list is: \n")
		print("head ->",end=' ')
		while dNode.next != self.head:
			print(dNode.next.data,"->",end=' ')
			dNode = dNode.next
		print("head\n")
					
					
					
l = CircularSingleLinkedList()
l.CreateCircularSingleLinkedList()
# l.GetElement()
# l.FindElement()
l.DeleteElement()	
	
		
		
		
		
		
		
