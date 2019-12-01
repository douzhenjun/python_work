#单链表有环指的是单链表中某个结点next域指向的是链表中在它之前的某一个结点，这样在链表的尾部形成一个环形结构
#判断它的存在性:
#如果fast指针与slow指针相遇了，说明链表里有环存在。
#寻找环的入口位置(第d0个结点，head.next是第一个结点):
#首先，可以确定如果fast跟slow相遇了，相遇的地点一定是在环内。
#其次，如果fast跟slow从同一地点出发，后面相遇了，那么fast一定比slow多走了1个周期s(环的结点个数)，
#否则，fast比slow多走了1个周期s减去fast跟low的距离:s-d。(d是fast与slow的距离)
#所以，当slow第一次走到环入口d0时，fast要么也在环入口，要么在环的其他位置，因为此时fast比slow多走了d0个距离，
#又fast跟slow的距离为d，所以这d0个距离就等于ks+d(k>=1,0<=d<s).
#总之，当相遇时，fast比slow多走了d0+s-d(s>d>=0,s>=2)个结点的距离(也就是(k+1)s)。相遇的地点在d0+s-d个结点处。
#设计两个指针p,q每次都走一步,p从相遇的地点出发，q从head出发，当p走到d0个结点时，q走到第(do+s-d+d0)个结点,也就是第d0+(k+1)s个结点,
#由环的周期性，也就是q会走到第d0个结点。从而p=q,当满足这个条件时，q所指的结点就是环的入口结点.
#假设p1,p2相距为d0，p1速度为v1，p2速度为v2，同时出发，问第一次相遇时，p1和p2共走了多少次？
#(v2-v1)*n = k*cycle - d0,其中n表示次数，k>=1, cycle表示周期，d0表示一开始的步距(d0>cycle时则对cycle求余)，
#v2,v1分别表示两指针的速度.
from LinkedList_Resort import Node, LinkedList

class LNode:
	def __init__(self, x = None):
		self.data = x
		self.next = None
		
def constructList():
	i = 1
	head = LNode()
	tmp = None
	cur = head
	while i < 8:
		tmp = LNode(i)
		cur.next = tmp
		cur = tmp
		i += 1 
	cur.next = head.next.next.next
	return head
	
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

if __name__ == "__main__":
	head = constructList()
	meetNode = isLoop(head)
	if meetNode != None:
		print("Loop exists!")
		index = findLoopNode(head, meetNode)
		print("The entrance point' index is: ", index)
	else:
		print("No Loop!")
