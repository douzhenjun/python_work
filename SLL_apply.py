#创建单链表LA,LB,LC.其中LA拆分成LB和LC,用来分别存储LA中男生和女生部分
from ex020302 import Node
from ex020302 import SingleLinkedList
#Experience: we can not take the statement such as "LB=LA,LC=LA",it is because
#when we use above statement, we define two pointers rather than two new objects.
#Hence, when we enter the following iteration, we aim to insert elements from LB and 
#LC,but because they are not new objects, operating upon them equals to operationg on
#LA,so LA's length is longer 1 code with each increasement of iteration times,
#that is why the iteration can not end forever.
#Remember: When we say "A=B",if B is a number(type such as int,float,string...),A is B's 
#transcript(副本),but when B is an object,A is B's pointer.When we change B, A changes meanwhile.
#(conclusion stands when is on the contrary)
	
LA = SingleLinkedList()
LB = SingleLinkedList()
LC = SingleLinkedList()
LA.CreateSingleLinkedList()
dNode = LA.head
n = 0
while dNode.next != None:
	dNode = dNode.next
	n += 1
	if n%2 == 1:
		LB.InsertElements(dNode.data)
	elif n%2 == 0:
		LC.InsertElements(dNode.data)

LA.TraverseElement()
LB.TraverseElement()
LC.TraverseElement()


