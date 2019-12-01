#利用栈把十进制转化为二进制数

from SequenceStack import SequenceStack

sq = SequenceStack()
m = 0
list = []
while True:
	n = input("Please input a non-negative integer: ")
	n = eval(n)
	if int(n) != n:
		print("You cannot input a float type!")
		continue

	elif n < 0:
		print("You can not input a negative number! ")
		continue
			
	else:
		print("The binary system of this integer is:", end=' ')
		if n == 0:
			print("0")
			break	
		elif n == 1:
			print("1")
			break
		else:
			while n > 1:
				l = n
				while l > 1:
					l = l // 2
					m = m + 1
				list.append(m)
				n = n - 2**m
				m = 0
			if n == 1:
				m = 0
				list.append(m)
			list = list[::-1]
			for j in range(list[-1]+1):
				if j in list:
					sq.PushStack("1")
				else:	
					sq.PushStack("0")
			while not sq.IsEmptyStack():
				a = sq.PopStack()
				print(a, end="")
			break
		
	
