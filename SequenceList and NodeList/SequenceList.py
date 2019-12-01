#define a class of Node
class Node():
	def __init__(self,data):
		self.data = data
		self.next = None

#定义一个单向链表类		
class SingleLinkedList():
	def __init__(self):
		self.head = Node(None) #初始化节点函数，数据域为空，指针域为空
	
	#establish a single-linked list	
	def CreateSingleLinkedList(self):
		print("******************************")
		print("*Please input datas and ensure it with pressing 'Enter' key, if you want to end, please input '#'")
		print("******************************")
		cNode = self.head
		Element = input("Please input the present node: ")
		while Element != '#':
			nNode = Node(Element)
			cNode.next = nNode
			cNode = cNode.next
			Element = input("Please input the present node: ")

			
	#尾端插入元素函数		
	def InsertElementIntail(self):
		Element = input("Please input the value of node to be inserted in tail: ")
		if Element == '#':
			return 
		cNode = self.head
		nNode = Node(Element)
		while cNode.next != None:
			cNode = cNode.next
		cNode.next = nNode
		
		
	#尾端插入元素函数，不是依靠手动输入，而是依靠实参
	def InsertElements(self, data=None):
		tNode = Node(data)
		cNode = self.head
		while cNode.next != None:
			cNode = cNode.next
		cNode.next = tNode
	
		
	def InsertElementInHead(self):
		Element = input("Please input the value of node to be inserted in head: ")
		if Element == '#':
			return
		cNode = self.head
		nNode = Node(Element)
		nNode.next = cNode.next #记住顺序不能被颠倒，否则作为插入节点，它的前驱是头结点，但它的后继却变成了自己，这是
		cNode.next = nNode      #因为原来头结点的指针域被覆盖的缘故，所以正确的顺序应该是先确定插入节点的后继，再确定插入节点的前驱
			
	#to evaluate whether list is empty
	def IsEmpty(self):
		if self.head == None:
			return True
		else:
			return False
	
	#get the length of the list(the number of nodes)		
	def GetLength(self):
		cNode = self.head
		length = 0
		while cNode.next != None:
			length = length + 1
			cNode = cNode.next
		return length
		
				
	#to find element in the single-linked list				
	def FindElement(self):
		pos = 0
		cNode = self.head
		key = input("Please input the element you want to find: ")
		if self.head.next == None:
			print("The present single-linked list is empty!")
			return
		while cNode.next != None and cNode.data != key:
			cNode = cNode.next
			pos = pos + 1    #the index of our habit does not contain 0,so we plus 1 in the base of the normal index
		if cNode.data == key:
			print("Successfully in find, the node of which element is",key,"is located in the index number of",pos,"of the list.")
		else:
			print("Failed in find, the present single-linked list does not have the element of",key,".")
	
	#to delete elements in the single-linked list
	def DeleteElement(self):
		dElement = input("Please input the element you want to delete: ")
		cNode = self.head                                     #设置两个指针,每一次迭代指针往后走一步,一个指针先走,另一个指针跟着,
		pNode = self.head                                     #这样到跳出循环的时候,其中一个指针一定比另一个指针慢一个节点.这样做的好处
		if self.head.next == None:                            #是删除结点以后,指向该节点的指针也被删除,该节点的前驱与该节点的后继要凭借另一个
			print("The present single-linked list is empty!") #指针连在一起,而且该指针正好在我们需要它在的地方(靶节点的前驱节点处)
			return
		while cNode.next != None and cNode.data != dElement:  #遍历到倒数第二个节点为止,反证：如果遍历到最后一个节点,它包含目标函数的话，
			pNode = cNode                                     #p指向c,而c指向none,此时c.data也是none,不等于dElement,所以会输出'要删除的
			cNode = cNode.next                                #变量在这个单链表中不存在',这与基本事实矛盾.
		if cNode.data == dElement:
			pNode.next = cNode.next
			del cNode
			print("Successfully delete the code which contains the",dElement,".")
		else:
			print("Fail in delete for the present list does not have the node which has the",dElement,".")
		
	#遍历单链表
	def TraverseElement(self):
		dNode = self.head
		print("The present single-linked list is: \n")
		print("head ->",end=' ')
		while dNode.next != None:
			print(dNode.next.data,"->",end=' ')
			dNode = dNode.next
		print("None\n")
		

# l = SingleLinkedList()
# l.CreateSingleLinkedList()
# l.DeleteElement()
# # l.InsertElements("douzhenjun")
# l.TraverseElement()
		
		
		
		
		
