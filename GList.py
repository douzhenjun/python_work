#创建一个广义表

class GLNode:

#initialize the GList Node
	def __init__(self):
		self.tag = 1                                                    #self.tag:if tag=0,the node is ListNode,else if tag =1, the node   
		self.union = None                                               #is AtomNode,if the prior stands,self.union stores the address                                             
		self.next = None                                                #of the head of GList(广义表表头),self.next stores the tail of 
		                                                                #GList(广义表表尾),if the latter stands, self.union stores the 
	                                                                    #atom(原子).
	def CreateGList(self, Table):                                       
		if len(Table) > 0:                                              #这是一个递归过程
			tTable = Table.pop(0)                                       #一个广义表可以看作是一堆圆括号的嵌套,如果没有任何原子在里面,
			tGLNode = GLNode()                                          #我们说广义表是空的,无论它里面有多少括号.最终会返回NOne(tGLNode=None),
			tGLNode.tag = 1											    #否则,它最终会返回原子节点(tGLNode.tag=0,tGLNode.union=tTable).
			tGLNode.union = self.CreateGList(Table)                     #这是获取表头的过程,建立一个广义表相当于从广义表中一层一层地获得其中所有的表头,
			if tTable == '(':											#或者表头为空,或者表头为原子结点.
				tGLNode.tag = 1
				tGLNode.union = self.CreateGList(Table)                 	
			elif tTable == ')' or tTable == '#':						    
				tGLNode = None
			else:
				tGLNode.tag = 0
				tGLNode.union = tTable
		else:
			tGLNode = None
		if len(Table) > 0:                                              
			tTable = Table.pop(0)	
		if tGLNode != None:
			if tTable == ',':
				tGLNode.next = self.CreateGList(Table)
			else:
				tGLNode.next = None
		return tGLNode
		
	#traverseGList
	def TraverseGList(self, GList):
		if GList != None:
			if GList.tag == 0:
				print(GList.union, end=' ')
			else:
				print('(', end=' ')
				if GList.union == None:
					print('#', end='')
					if GList.union == None:
						print('#', end=' ')
					else:
						self.TraverseGList(GList.union)
					print(')', end=' ')
			if GList.next != None:
				print(',', end=' ')
				self.TraverseGList(GList.next)
	
	#Get the head and tail
	def GetGListHead(self, GList):
		if GList != None and GList.union != None:
			head = copy.deepcopy(GList.union)
			head.next = None
			return head
		else:
			print("There is no way to get the head of the GList!")
			
	def GetGListTail(self, GList):
		if GList != None and GList.union != None:
			tail = copy.deepcopy(GList.union.next)
			return tail
		else:
			print("There is no way to get the tail of the GList!")
	
gl = GLNode()
gl.CreateGList(('b',('c','d','e')))
GList = gl.CreateGList(('b',('c','d','e')))
print(gl.TraverseGList(GList))
print(gl.GetGListHead(GList))		
		
		
		
	
