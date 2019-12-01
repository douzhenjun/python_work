#StringNode

class StringNode():
	def __init__(self):
		self.data = None
		self.next = None
		
class StringLink():
	def __init__(self):
		self.head = StringNode()
		self.tail = self.head
		self.length = 0
		
	def CreateString(self):
		stringSH = input("\nPlease input the string: ")
		while self.length < len(stringSH):
			Tstring = StringNode()
			Tstring.data = stringSH[self.length]
			self.tail = Tstring
			self.length = self.length + 1
	
	def GetStringLength(self):
		return self.length
			
	def StringCopy(self, strSrc):
		self.head = strSrc.head
		self.tail = strSrc.tail
		self.length = strSrc.length
		
	def StringConcat(self, strSrc):
		self.tail.next = strSrc.head.next
		self.tail = strSrc.tail
		self.length = self.length + strSrc.length
	
	def GetString(self):
		string = ''
		cNode = self.head
		while cNode.next != None:
			cNode = cNode.next
			string = string + cNode.data
		print(string)
		
				
					
					
					
					
					
					












