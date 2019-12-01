#找出单链表的倒数第k个元素
#分析：快慢指针方法，建立两个指针，其中一个指针走到前面，跟后面的指针相隔k个结点的距离，
#这样，当前面的指针走到表尾时，后面的指针所指元素就是链表的倒数第k个元素。
from LinkedList_CalculateInPlus import Node, LinkedList

LENGTH = 7
def FindElements(k, lst):
	if k > LENGTH:
		return
	fptr = lst.head1
	lptr = lst.head1
	index = 0
	while fptr.next != None:
		fptr = fptr.next 
		index += 1
		if index >= k:
			lptr = lptr.next
	return lptr.data

lst = LinkedList()
cNode = lst.head1
for i in range(1, 8):
	dNode = Node(i)
	cNode.next = dNode
	cNode = cNode.next
lst.Traverse(lst.head1)
print(FindElements(3, lst))
	
