#打印九九乘法表
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = [None for k in range(0, 45)]
for i in range(9):
	for j in range(9):
		if j <= i:
			k = int((i*(i+1)/2)+j)
			list3[k] = list1[i] * list2[j]

for i in range(1, 10):
	for j in range(1, 10):
		if j <= i:
			print(j,"*",i,"=",list3[0], end=' ')
			list3.pop(0)
		if j % 9 == 0:
			print()
