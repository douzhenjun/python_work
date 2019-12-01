#汉诺塔函数实现
#将编号为n的金片从NA上移到NC上的函数
class TestHanoi():
	def __init__(self):
		self.count = 0
		
	def move(self, NA, n, NC):
		self.count = self.count + 1
		print("第",self.count,"次移动:将第",n,"号金片从",NA,"移到",NC)
		
	def HanoiTower(self, n, NA, NB, NC):
		if n == 1:
			self.move(NA, 1, NC)
		else:
			self.HanoiTower(n-1, NA, NC, NB)
			self.move(NA, n, NC)
			self.HanoiTower(n-1, NB, NA, NC)

	def TestHT(self):
		N = int(input("请输入第一根针上有多少个金片: "))
		while N<=0:
			N = int(input("请重新输入第一针上有多少个金片: "))
		Num1 = input("请输入第一根针的编号为: ")
		Num2 = input("请输入第二根针的编号为: ")
		Num3 = input("请输入第三根针的编号为: ")
		print("移动过程如下: ")
		self.HanoiTower(N,Num1,Num2,Num3)
	
	
TH = TestHanoi()
TH.TestHT()	
	
	
	
	
	
