#有理数加法
class Rational:
	@staticmethod
	def _gcd(m,n):
		while n != 0:
			m,n = n,m%n
		m,n = n,m
		return n 	
		
	def __init__(self, num, den=1):
		if not isinstance(num, int) or not isinstance(den, int):
			raise TypeError
		if den == 0:
			raise ZeroDivisionError
		sign = 1
		if num < 0:
			num, sign = -num, -sign
		if den < 0:
			den, sign = -den, -sign
		g = Rational._gcd(num, den)
		self._num = sign * (num//g)#self._num 表示分子,self._den表示分母,它们都只能在类内部使用,不能从类外部引用
		self._den = den//g


#定义一对解析操作(也是实例方法)
	def num(self): return self._num
	def den(self): return self._den
    
#展示
	def show_rational(self):
		if self.den() == 1:
			print(self.num())
		else:
			print(self.num(),"/",self.den())

	#加法
	def __add__(self, another):
		if not isinstance(another, Rational):
			raise TypeError
		den = self._den * another.den()
		num = (self._num * another.den() + self._den * another.num())
		return Rational(num, den)

	#乘法	
	def __mul__(self, another):
		return Rational(self._num * another.num(), self._den * another.den())

	#除法
	def __floordiv__(self, another):
		if another.num() == 0:
			raise ZeroDivisionError
		return Rational(self._num * another.den(), self._den * another.num())
		
r = Rational(6, 4)
r.show_rational()	
u = r.__add__(Rational(1, 2))
u.show_rational()		

	
	
	
	
	
		
