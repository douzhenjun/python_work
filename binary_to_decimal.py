#二进制转十进制

from ex030102 import SequenceStack

while True:
	string = input("Please input a binary number: ")
	u = 0
	for i in string:
		if i != "0" and i != "1":
			break
		else:
			u = u + 1
			continue
	if u == len(string):
		break
	else:
		print("TypeError")
		continue				
print("The decimal of the number",string,"is: ", end='')
n = 0
sq = SequenceStack()
for j in string:
	sq.PushStack(j)
m = 0
while not sq.IsEmptyStack():
	k = sq.PopStack()
	n = n + eval(k) * (2**m)
	m = m + 1
print(n)
	
