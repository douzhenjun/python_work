#K链表翻转是指把每K个相邻的结点看成一组进行翻转,如果剩余结点不足K个，则保持不变。
#举例:1->2->3->4->5->6->7和一个数K=2,那么翻转过后的链表为:2->1->4->3->6->5->7
#如果K=3,那么翻转后的链表为:3->2->1->6->5->4->7.
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
		
	def FlipPerKNodes(self, k):
		cNode = self.head
		LENGTH = 0
		while cNode.next != None:
			cNode = cNode.next
			LENGTH += 1				#LENGTH标记链表的长度，一般来说它应该大于等于k
		
		tmp = self.head
		while LENGTH >= k:
			p = tmp
			q = tmp
			index = 0
			
			while index != k:		#p指针指向从tmp后继节点开始第k个结点,然后q指针指向p的前驱结点,进行翻转操作,再将q指向q的前驱结点,p类似循环
				p = p.next			#直到p指向tmp的后继节点(或者说原本的第1个结点),循环结束.
				index += 1
			dmp = p
			lmp = p.next
			
			while tmp.next != p:
				q = tmp
				while q.next != p:
					q = q.next
				p.next = q
				p = p.next
								
			tmp.next = dmp			#实现一次k翻转以后,tmp应该和原本第k个结点建立连接,并且原本的第1个结点(头结点除外)变成了第k个结点,它要跟原本的
			p.next = lmp			#第k+1个结点建立连接.最后,将此时的第k个结点标记为tmp,下一次循环前的准备工作已经完成.
			tmp = p
			LENGTH -= k

		print("The present linkedlist is: ")
		self.Traverse()
		
			
if __name__ == "__main__":
	ll = LinkedList()
	ll.ConstructLinkedList()
	ll.FlipPerKNodes(7)			
			
