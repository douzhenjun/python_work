#如何找出数组中第k小的数？
#采用快速排序法平均意义上是最快的，时间复杂度为O(N*log2N)

def findSmallK(arr, low, high, k):
	if k > len(arr):
		print("The k's value is out of the range of the array.")
		return
	if low <= high:
		i = low
		j = high
		tmp = arr[low]
		while i < j:
			while i < j and arr[i] <= tmp:
				i += 1
			print(i)
			while j >= i and arr[j] >= tmp:
				j -= 1
			print(j)
			if i < j:
				arr[i],arr[j] = arr[j],arr[i]
				print(array)
		arr[low] = arr[j]
		arr[j] = tmp
		print(arr)
		print()
		
		#记录分点在arr【low-high】中下标的偏移量
		index = j - low
		if index == k - 1:
			return arr[j]
		elif index > k - 1:
			return findSmallK(arr, low, j-1, k)
		elif index < k - 1:
			return findSmallK(arr, j+1, high, k-(index+1))
	
	
def fastSortMethod(arr, low, high):
	if low < high:
		i = low
		j = high
		tmp = arr[low]
		while i < j:
			while i < j and arr[i] <= tmp:
				i += 1
			print(i)
			while j > i and arr[j] >= tmp:
				j -= 1
			print(j)
			if i < j:
				arr[i],arr[j] = arr[j],arr[i]
				print(array)
		arr[low] = arr[j]
		arr[j] = tmp
		print(arr)
		print()
		fastSortMethod(arr, low, j-1)
		fastSortMethod(arr, j+1, high)
					
if __name__ == "__main__":
	array = [11, 10, 2]
	print("The original array is\n", array)
	k = 2		#第k小的数，注意k不能超过数组的长度
	element = findSmallK(array, 0, len(array)-1, k)
	print("The present array is\n", array)
	print("The",k,"-th smallest number in this array is",element,".")
				
