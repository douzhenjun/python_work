#利用递归求解阶梯问题
class Floor():
	
	def __init__(self):
		self.m = 1
		self.num = 0
	
	
	def move(self, n):
		print("->",n+1, end='')
		self.m += 1
	
	
	def move_another(self, n):
		print("->",n+2, end='')
		self.m += 1

		
	def FloorSteps(self, n):
		if n == 0:
			print("1", end='')
		elif n == 1:
			print("1", end='')
			self.move(1)
		elif n > 1:
			self.FloorSteps(n-1)
			self.move(n)
	
	
	def TestFloorSteps(self, n):
		self.FloorSteps(n)
		if self.m == n+1:
			self.num += 1
			print()
			self.m = 1
			
		for k in range(1, n-1):
			self.FloorSteps(k-1)
			self.move_another(k)
			if k+2 < n:
				for j in range(k+2, n+1):
					self.move(j)
				self.num += 1
				print()
			elif k+2 == n:
				self.move(k+2)
				self.num += 1
				print()

		for k in range(1, n-2):
			self.FloorSteps(k-1)
			self.move_another(k)
			if k+2 < n-1:
				for j in range(k+2, n-1):
					self.move(j)
				self.move_another(n-1)
				self.num += 1
				print()
			elif k+2 == n-1:
				self.move_another(k+2)
				self.num += 1
				print()

fl = Floor()
fl.TestFloorSteps(7)
print("共有",fl.num,"种上楼梯的走法")



