#假定给定链表1->2->3->4->5->6->7中指向第五个元素的指针，要求把结点5删掉，删掉后链表变为1->2->3->4->6->7
class Node:
	def __init__(self, x = None):
		self.data = x
		self.next = None
	
def printList(head):
	cur = head.next
	while cur != None:
		print(cur.data, end = ",")
		cur = cur.next
		
def RemoveNode(p):
	if p == None or p.next == None:
		return False
	p.data = p.next.data
	tmp = p.next
	p.next = tmp.next
	return True
		
if __name__ == "__main__":
	i = 1
	head = Node()
	tmp = None
	cur = head
	p = None
	while i < 8:
		tmp = Node(i)
		cur.next = tmp
		cur = tmp
		if i == 5:
			p = tmp
		i += 1
	print("The original list is:")
	printList(head)
	result = RemoveNode(p)
	if result:
		print("\nThe present list after deleting the node %d is:" %(p.data))
		printList(head)
			
			
			
			
			
			
			
			
