#插入排序法
#思路：
SIZE = 8
def showdata(data):
	for i in range(SIZE):
		print(data[i], end=" ")
	print()

def insert(data):
	for i in range(len(data)-1):
		for j in range(i+1, 0, -1):
			if data[j] < data[j-1]:
				data[j],data[j-1] = data[j-1],data[j]
	return data
				
	
					
if __name__ == "__main__":
	data = [16, 25, 39, 27, 12, 8, 45, 63]
	print("初始数组为: ")
	showdata(data)
	print("经过插入排序后的数组为: ")
	showdata(insert(data))
