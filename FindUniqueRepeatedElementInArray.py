#数字1-1000放在含有1001个元素的数组中，要求1-1000均出现一次，剩余一个位置也得是1-1000中的一个数，问在不借助辅助
#存储空间的情况下，如何找出这个重复的元素。
import random

def constructArray():
	array = []
	for i in range(1, 1001):
		array.append(i)
	j = random.randint(1, 1001)
	array.append(j)
	return array

def findElement(array):
	sum1 = 0
	for i in array:
		sum1 += i
	sum2 = 0
	for k in range(1, 1001):
		sum2 += k
	t = sum1 - sum2
	return t

if __name__ == "__main__":
	array = constructArray()
	print("The array is:\n")
	for i in array:
		print("%3d"%i, end = " ")
		if i % 20 == 0:
			print()
	element = findElement(array)
	print("The unique repeated element in this array is", element,".")
