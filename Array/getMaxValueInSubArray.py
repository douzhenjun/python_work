#获得数组连续最大和
#有一个整数数组，正负数都有，如何找到一组连续的子数组，使得该子数组的元素的和是最大的？

def getMax(array):
	negative = 0
	minimum = -2**30
	for i in range(len(array)):
		if array[i] <= 0:
			negative += 1
			if array[i] > minimum:
				minimum = array[i]
	if negative == len(array):
		return minimum
	else:
		summ = 0
		summ1 = 0
		permit = False
		for j in range(len(array)):
			if array[j] < 0 and not permit:
				continue
			elif array[j] >= 0:
				summ1 += array[j]
				permit = True
				continue
			elif array[j] < 0 and permit:
				summ2 = summ1
				print(summ1)
				for k in range(j, len(array)):
					if summ2 >= 0:
						summ2 += array[k]
						if summ2 > summ1:
							summ1 = summ2
					else:
						break
				print(summ2)
				if summ1 > summ:
					summ = summ1
				summ1 = 0
				summ2 = 0
				print(summ)
				print()
				permit = False
		return summ
				
if __name__ == "__main__":
	array = [3, -2, -4, -7, 5, 2, 12, -1, -3, -5, -9, 0]
	print("The original array is\n", array)
	maxSum = getMax(array)
	print("The maxsum of the subarray in this array is:", maxSum)	
