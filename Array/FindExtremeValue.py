#Find Extreme Value in  Array
#给定数组a1,a2,...an,要求找出数组中的最大值和最小值。假设数组中的值两两各不相同。
import random

def createArray():
	array = []
	for i in range(100):
		k = random.randint(-100, 101)
		array.append(k)
		if k in array:
			i -= 1
			continue
	return array
	
def getExtremeValue(array):
	if len(array) % 2 == 1:
		
