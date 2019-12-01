class Factorial():
	def __init__(self):
		self.LabelN = None
		self.N = None
		self.F = None

	def Factorial(self, n):
		FE = FactElements()
		FE.LabelN = 2
		FE.N = n
		st = SequenceStack()
		st.PushStack(FE)
		while True:
			tFE = st.GetTopStack()
			if tFE.N >= 1:
				temp = FactElements()
				temp.LabelN = 1
				temp.N = tFE.N - 1
				st.PushStack(temp)
			else:
				tFE.F = 1
				break
		while True:
			tFE = st.GetTopStack()
			if tFE.LableN == 1:
				st.PopStack()
				temp = st.GetTopStack()
				temp.F = tFE.F * temp.N
			tFE = st.GetTopStack()
			if tFE.LabelN == 2:
				tFE = st.PopStack()
				f = tFE.F
				break
		print("The result of the solving is:",tFE.N,"!=",f)
	
			
