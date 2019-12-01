#改进的冒泡排序法
def dubble_sort(d):
	for i in range(5):
		flag = 0
		for j in range(5-i):
			if d[j] > d[j+1]:
				d[j],d[j+1] = d[j+1],d[j]
				flag += 1
		if flag == 0:
			break
		print("第 %d 次排序结果:" %(i+1), end=" ")
		for k in d:
			print("%2d" %k, end="")
		print()
# data = [4, 2, 6, 7, 8, 9]
# dubble_sort(data)

#选择排序法
def select_sort(data):
	for i in range(len(data)-1):
		for j in range(i+1, len(data)):
			if data[i] > data[j]:
				data[i], data[j] = data[j], data[i]
		print("第 %d 次排序结果:" %(i+1), end=" ")
		for k in data:
			print(k, end=" ")
		print()
data = [55, 23, 87, 62, 16]
select_sort(data)
