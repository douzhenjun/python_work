#编写一个顺序表实现一些基本操作

#编写一个顺序表的类
class SequenceList():
	def __init__(self):
		self.SeqList = []
	
	def CreateSequenceList(self):
		print("Pleas input the element and press '#' to end.")
		element = input("Please input the element: ")
		while element != '#':
			self.SeqList.append(element)
			element = input("Please input the element: ")
	
	def IsEmpty(self):
		if self.SeqList == []:
			print("The list is empty.")
		else:
			print("The list is not empty.")
			
	def NumberOfElements(self):
		n = 0
		if self.SeqList == []:
			print("There is no element in this list.")
		else:
			for i in self.SeqList:
				n += 1	
			print("The nunmber of elements is",n)			
	
	def GetIndexOfElement(self):
		if self.SeqList == []:
			print("Invalid operating!")
		else:
			element = input("Please input the element: ")
			index = []
			for i in range(0,len(self.SeqList)):
				if self.SeqList[i] == element:
					index.append(i)
			print("The index of target element is: ")
			if index != []:
					for j in index:
						print(j+1,end=' ')
					print("\n")
			else:
				print("There is no target element exists.")
	
	def InsertElement(self):
		element = input("Please input the element which is to be inserted: ")
		index = int(input("Please input the index of the element: "))
		if index >= len(self.SeqList):
			self.SeqList.append(element)
		else:
			self.SeqList.insert(index-1, element)
		print("The contemporary sequencelist is \n",self.SeqList)
			
	def DeleteElement(self):
		element = input("Please input the element you want to delete: ")
		for i in self.SeqList:
			if i == element:
				self.SeqList.remove(i)
		print("The contemporary sequencelist is \n",self.SeqList)
		
		
	def TraverseElement(self):
		SeqListLen = len(self.SeqList)
		for i in range (0,SeqListLen):
			print("The index number of which",i+1,"is",self.SeqList[i])
			
	 #destroy sequencelist
	def DestroySequenceList(self):
		del self.SeqList
		try:
			print(self.SeqList)
		except AttributeError:
			print("You have destroyed the list now!")		
				
SL = SequenceList()
SL.CreateSequenceList()
# SL.IsEmpty()
# SL.NumberOfElements()			
# SL.GetIndexOfElement()
# SL.InsertElement()
# SL.DeleteElement()
# SL.TraverseElement()
SL.DestroySequenceList()		
			
			
			
			
