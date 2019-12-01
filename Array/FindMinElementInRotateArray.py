#采用二分算法找到旋转数组的最小值
#要求输入的元素一定是两两不相同的，否则不合法

def findMin(arr, low, high):
	if arr[low] < arr[high]:
		return arr[low]
	mid = (low+high) // 2
	if arr[mid] < arr[mid-1]:
		return arr[mid]
	else:
		if arr[mid] < arr[high]:
			return findMin(arr, low, mid-1)
		if arr[mid] > arr[high]:
			return findMin(arr, mid+1, high)
		else:
			print("The array is not illegal!")
			return
			
if __name__ == "__main__":
	array = [7, 8, 12, 14, 17, 2, 3, 5, 6, 6.5]	#默认它是一个旋转数组，下面只能筛选出元素各不相同的，并不能识别是否是旋转数组
	run = []
	flag = False
	for i in range(len(array)):
		if array[i] not in run:
			run.append(array[i])
		else:
			print("The array is illegal!")
			flag = True
			break
	if not flag:	
		print("The original rotate array is\n", array)
		minn = findMin(array, 0, len(array)-1)
		print("The minimum element in this array is",minn)
				
