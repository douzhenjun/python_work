#给定一个数组，数组中含有重复元素，给定两个数字num1和num2，求这两个数字在数组中出现的位置的最小距离

def minDistance(arr, num1, num2):
	if arr == None or len(arr) <= 0:
		print("参数不合理.")
		return 2**32
	lastPos1 = -1		#上次遍历到num1的位置
	lastPos2 = -1		#上次遍历到num2的位置
	minDis = 2 ** 30
	i = 0
	while i < len(arr):
		if arr[i] == num1:
			lastPost1 = i
			if lastPos2 >= 0:
				minDis = min(minDis, lastPos1-lastPos2)
		if arr[i] == num2:
			lastPos2 = i
			if lastPos1 >= 0:
				minDis = min(minDis, lastPos2-lastPos1)
		i += 1
	return minDis
	
if __name__ == "__main__":
	arr = [4, 5, 6, 4, 7, 4, 6, 4, 7, 8, 5, 6, 4, 3, 10, 8]
	num1 = 4
	num2 = 8
	print(minDistance(arr, num1, num2))
