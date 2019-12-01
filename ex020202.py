class SequenceList():
	def __init__(self):
	#初始化顺序表函数

		self.SeqList=[]
	
	#创建顺序表函数
	def CreateSequenceList(self):
		print("*********************************************************")
		print("*Please input datas and press 'Enter' key to ensure, if you want to end, please input '#'.*")
		print("*********************************************************")
		Element = input("Please input elements: ")
		while Element != '#':
			self.SeqList.append(int(Element))
			Element = input("Please input elements: ")
			
    #destroy sequencelist
	def DestroySequenceList(self):
		del self.Seqlist
		# while self.SeqList != []:
			# for i in self.SeqList:
				# self.SeqList.remove(i)
	
	#evaluate if sequencelist is empty			
	def IsEmpty(self):
		if self.SeqList == []:
			print("The sequencelist is empty!")
		else:
			print("The sequencelist is not empty!")
			
	#find value of sequenlist
	def FindElement(self):
		key = int(input('Please input what element you want to seek: '))
		if key in self.SeqList:
			ipos = self.SeqList.index(key)
			print("Successfully in seek! The element is ",self.SeqList[ipos],",and is located in the ",ipos+1,"nd of sequencelist.")
		else:
			print("Unsuccessfully in seek,sorry!")
	
	#insert element		
	def InsertElement(self):
		ipos = int(input('Please input the location of element which is to be insert: '))
		Element = int(input('Please input the value of element which is to be insert: '))
		self.SeqList.insert(ipos, Element)
		print("The contemporary sequencelist is \n", self.SeqList)
		
	#delete element
	def DeleteElement(self):
		dpos = int(input("Please input the index of which element you want to delete: "))
		self.SeqList.remove(self.SeqList[dpos])
		print("The contemporary sequencelist is \n",self.SeqList)
		
	#遍历顺序表元素
	def TraverseElement(self):
		SeqListLen = len(self.SeqList)
		for i in range (0,SeqListLen):
			print("The index number of which",i+1,"is",self.SeqList[i])
			
	#seek for maximum or minimum of the sequencelist
	def GetExtremum(self):
		while True:
			print("******************************")
			print("*1:seek maximum")
			print("*2:seek minimum")
			print("*3:seek maximum and minimum")
			print("*0:exit the program")
			print("******************************")
			i = int(input("Please input: "))
			if i==1:
				print("The maximum of the SeqList is : ",max(self.SeqList))
			elif i==2:
				print("The minimum of the SeqList is : ",min(self.SeqList))
			elif i==3:
				print("the maximum and minimum of SeqList is :",max(self.SeqList),"and",min(self.SeqList))
			elif i==0:
				break
			else:
				pass
		
lst = SequenceList()
lst.CreateSequenceList()
# lst.InsertElement()
# lst.FindElement()
# lst.DeleteElement()
# lst.IsEmpty()
# lst.TraverseElement()
lst.GetExtremum() 

		
			
			
			
			
			
