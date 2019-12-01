#给定两个单链表，链表的每个结点代表一位数，计算两个数的和.
#默认:从左到右表示从个位到更高位
class Node:
	def __init__(self, x=None):
		self.data = x
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head1 = Node()
		self.head2 = Node()



	def GetTheElement(self):
			while True:
				print("Please input the first list's elements, split by pressing space keyboard:")
				elements = input()
				cNode = self.head1
				index = 0
				num = ""
				for i in elements:
					index += 1
					if i != " ":
						num += i
						continue
					if len(num) > 1:
						break
					else:
						dNode = Node(num)
						cNode.next = dNode
						cNode = cNode.next
						num = ""
				if index == len(elements) and len(num) == 1:
					dNode = Node(num)
					cNode.next = dNode
					cNode = cNode.next
					break

			
			while True:
				print("Please input the second list's elements, split by pressing space keyboard:")
				elements = input()
				cNode = self.head2
				index = 0
				num = ""
				for i in elements:
					index += 1
					if i != " ":
						num += i
						continue
					if len(num) > 1:
						break
					else:
						dNode = Node(num)
						cNode.next = dNode
						cNode = cNode.next
						num = ""
				if index == len(elements) and len(num) == 1:
					dNode = Node(num)
					cNode.next = dNode
					cNode = cNode.next
					break


	def Plus(self):
		r1 = 0
		r2 = 0
		k = 0
		l = 0
		cNode = self.head1.next
		dNode = self.head2.next
		while cNode != None:
			x = int(cNode.data)
			r1 = r1 + x * (10**k)
			cNode = cNode.next
			k = k + 1
		while dNode != None:
			x = int(dNode.data)
			r2 = r2 + x * (10**l)
			dNode = dNode.next
			l = l + 1

		s = str(r1+r2)
		index = 0
		for i in s[:-1]:
			index += 1
			print(i, end="->")
		print(s[-1])
			
	def Traverse(self, head):
		print("The present list is:")
		pNode = head.next
		while True:
			if pNode.next == None:
				print(pNode.data)
				break
			else:
				print(pNode.data, end="->")
				pNode = pNode.next
		print()

if __name__ == "__main__":		
	ll = LinkedList()
	ll.GetTheElement()
	ll.Plus()
