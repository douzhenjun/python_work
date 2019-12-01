#如何找出数组中出现奇数次的数
#数组中有N+2个数，其中N个数出现了偶数次，2个数出现了奇数次，请用O(1)的空间复杂度找出这两个数

def findOdd(arr):
	for i in range(len(arr)):
		if arr[i] == None:
			continue
		flag = True
		for j in range(i+1, len(arr)):
			if arr[j] == None:
				continue
			if arr[j] == arr[i]:
				flag = not flag
				arr[j] = None
		if not flag:
			arr[i] = None

	for k in range(len(arr)):
		if arr[k] != None:
			ele1 = arr[k]
			break
	for l in range(k+1, len(arr)):
		if arr[l] != None:
			ele2 = arr[j]
			break
	return (ele1, ele2)
	
if __name__ == "__main__":
	array = [1, 1, 2, 3, 3, 2, 2, 2, 4, 4, 4, 5, 5, 6]
	print("The original array is:\n", array)
	elements = findOdd(array)
	print("The target elements which occurs in odd twice are:",elements)
				
