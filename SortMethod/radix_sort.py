#基数排序法:基数排序法不需要进行元素之间的比较，它是按照最低位优先或最高位优先分配元素的位置，然后按照0~9的自然顺序从左到右打印输出
#当最高位的元素位置确定时，排序完成，算法结束。由于每次排序基本保留了前面的排列顺序结果，所以它是一种稳定排序
import random

def show(data, size):
	for i in range(size):
		data[i] = random.randint(0, 999)
	return data
		


def radix(data, size):
	n = 1
	while n <= 100:
		tmp = [[] for x in range(10)]
		for i in range(size):
			m = (data[i]//n) % 10
			tmp[m].append(data[i])
			print(tmp)
		k = 0
		while k < size:
			for j in range(10):
				while len(tmp[j]) != 0:
					data[k] = tmp[j][0]
					del tmp[j][0]
					k += 1
		print("The data is", data)				
		n = n * 10
	return data
		
				
if __name__ == "__main__":
	size = 10			#the number of the elements
	data = [0] * size	#initial the list which store the elements
	print("The original elements to be sorted are:\n ", show(data, size)) 
	print("The sorted elements by radix method are:\n ", radix(data, size))
