#BF算法
#检查主串中是否包含模式串序列，如果是，返回其首次出现的头位置，否则，返回未找到的消息
#创建一个线性字符串表

class StringList():
	def __init__(self):
		self.MaxStringSize = 256
		self.chars = ""
		self.length = 0
		
	def CreateStringByInput(self):
		stringSH = input("Please input the string: ")
		if len(stringSH) > self.MaxStringSize:
			print("String is longer than the compact of the assign space")
		else:
			self.chars = stringSH
			self.length = len(self.chars)
	
	
	def CreateString(self, x):
		if len(x) > self.MaxStringSize:
			print("String is longer than the compact of the assign space")
		else:
			self.chars = x
			self.length = len(x)
	
	def GetLength(self):
		return self.length
		
	def StringConcat(self, strSrc):
		lengthSrc = strSrc.length
		stringSrc = strSrc.chars
		if lengthSrc + len(self.chars) <= self.MaxStringSize:
			self.chars = self.chars + stringSrc
			self.length = len(self.chars)
		else:
			print("String is longer than the compact of the assign space")
			size = self.MaxStringSize - len(self.chars)
			self.chars = self.chars + stringSrc[0:size]
			self.length = len(self.chars)
		print("The string linked is:",self.chars)
	
	def GetString(self):
		return self.chars
		
	def BF_method(self, T, pos):
		if self.GetLength() < T.GetLength():
			print("Fail in match the target string",T.GetString(),"in string",self.GetString(),"!")
		else:
			while pos <= (self.GetLength() - T.GetLength()):
				iM = pos
				iT = 0
				flag = False
				while iT < T.GetLength():
					if T.chars[iT] == M.chars[iM]:
						iT = iT + 1
						iM = iM + 1
					else:
						break
				if iT == T.GetLength():
					flag = True
					print("Successfully in match!The target string",T.GetString(),
					"is in the seat of the number",pos,".")
					break
				else:
					pos = pos + 1
			if flag == False:		
				print("Fail in match the target string",T.GetString(),"in string",self.GetString(),"!")
			
	
	
	def KMP_method(self, T, pos):
		if self.GetLength() < T.GetLength():
			print("Fail in match the target string",T.GetString(),"in string",self.GetString(),"!")
		else:
			while pos <= (self.GetLength() - T.GetLength()):
				iM = pos
				iT = 0
				flag = False
				while iT < T.GetLength():
					if T.chars[iT] == M.chars[iM]:
						iT = iT + 1
						iM = iM + 1
					else:
						break
				if iT == T.GetLength():
					flag = True
					print("Successfully in match!The target string",T.GetString(),
					"is in the seat of the number",pos,".")
					break
				elif iT == 0:
					iT = iT + 1
				else:
					for k in range(1, iT+1):
						if T.chars[0:k-1] == T.chars[iT-k:iT-1]:
							continue
						else:
							iT = iT - k + 1
							break
				pos = pos + iT
			if flag == False:		
				print("Fail in match the target string",T.GetString(),"in string",self.GetString(),"!")
	
	def IndexKMP(self, pos, T, ListNext_ListNextValue):
		i = pos
		j = 0
		length = T.GetLength()
		string = T.GetString()
		while i < len(self.chars) and j < length:
			if j == -1 or self.chars[i] == string[j]:
				i = i + 1
				j = j + 1
			else:
				j = ListNext_ListNextValue[j]
		if j == length:
			print("Successfully in match!The target string is firstly occured in the index of",i-length)
		else:
			print("Fail in match!")

		
	def GetListNext(self):
		ListNext = [None for x in range(0, 100)]
		ListNext[0] = -1
		k = -1
		j = 0
		while j < len(self.chars):
			if k == -1 or self.chars[j] == self.chars[k]:
				k = k + 1
				j = j + 1
				ListNext[j] = k
			else:
				k = ListNext[k]
		return ListNext
			
			
	def GetListNextValue(self):
		ListNextValue = [None for x in range(0, 100)]
		ListNextValue[0] = -1
		k = -1
		j = 0
		while j < len(self.chars) - 1:
			if k == -1 or self.chars[j] == self.chars[k]:
				k = k + 1
				j = j + 1
				if self.chars[j] != self.chars[k]:
					ListNextValue[j] = k
				else:
					ListNextValue[j] = ListNextValue[k]
			else:
				k = ListNextValue[k]
		return ListNextValue		

		
				
M = StringList()
M.CreateStringByInput()
print("The main string is:",M.GetString())
T = StringList()
T.CreateStringByInput()
print("The target string is:",T.GetString())
pos = int(input("Please input the index of seats from where to seek first: "))
print("The result of the match: ", end="")
M.KMP_method(T,pos)
				
		
		
		
		
		
