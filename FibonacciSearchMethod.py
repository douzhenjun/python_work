#设计一个斐波那契数列查找法的python程序，然后实现斐波那契查找法的过程与步骤，所查找的内容如下:
#data = [5, 7, 12, 23, 25, 37, 48, 54, 68, 77, 99, 102, 110, 118, 120, 130, 135, 136, 150]

#斐波那契数列
def fib(n):
	if n == 1 or n == 0:
		return n
	else:
		return fib(n-1) + fib(n-2)

#斐波那契查找法		
def fibSearch(arr, key):
	twice = 0					#记录次数
	n = len(arr)-1				#获得数组最后一个元素的下标
	low = 0
	high = len(arr)-1
	k = 0
	while fib(k) - 1 < n:		#获得使得f[k] -1 >= n的最小k值，因为西方人习惯左闭右开的范围风格，所以右边最大就达到f[k]-1,事实上就是[0,f[k])
		k += 1
	for i in range(n, fib(k)): 	#如果数组最后的元素下标小于f[k]，那么填充最后一个数组元素arr[high]直到下标为f[k]-1
		arr.append(arr[high])
	
	while low <= high:			#循环条件跟二分法，插值法是一样的，即判断数组的左端是否不大于右端
		mid = low + fib(k-1) - 1
		print(mid)
		if key > arr[mid]:		#如果key>arr[mid], 因为f[k] = f[k-1]+f[k-2] > f[k-1]+f[k-3],所以k-=2才能保证下一次得到的mid不会溢出
			low = mid + 1		
			k -= 2
		elif key < arr[mid]:	#如果key<arr[mid], 因为f[k] = f[k-1]+f[k-2], mid = low+f[k-2]-1 = f[k-2]-1,这正是斐波那契数列的前一个元素
			high = mid - 1
			# high = fib(k-1)
			k -= 1
		else:					#如果在0到n范围内找到key==arr[mid],说明找到了返回index即可，否则，就是在n到fib[k]-1范围内找到key==arr[mid],
			if mid <= n:		#说明目标元素位于数组的最后位置。
				print("The total twice of the search is", twice+1)
				return mid
			else:
				print("The total twice of the search is", twice+1)
				return n
		twice += 1			
	return -1

#二分查找法		
def BisectionMethod(arr, key):
	twice = 0
	n = len(arr) - 1
	low = 0
	high = n
	while low <= high:
		mid = low + (high - low)//2
		if key < arr[mid]:
			high = mid - 1
		elif key > arr[mid]:
			low = mid + 1
		else:
			print("The total twice of the search is", twice+1)
			return mid
		twice += 1
	return -1

#插值查找法
def DifferenceMethod(arr, key):
	twice = 0
	n = len(arr) - 1
	low = 0
	high = n
	while low <= high:
		mid = low + ((key-arr[low])//(arr[high]-arr[low]))*(high-low)
		if key < arr[mid]:
			high = mid - 1
		elif key > arr[mid]:
			low = mid + 1
		else:
			print("The total twice of the search is", twice+1)
			return mid
		twice += 1
	return -1


if __name__ == "__main__":
	data = [5, 7, 12, 23, 25, 37, 48, 54, 68, 77, 91, 99, 102, 110, 118, 120,\
	130, 135, 136, 150]
	# data = [4, 5, 10, 45, 67, 78, 98, 145, 156]
	j = 0
	for i in data:
		print("%3d" % i, end = " ")
		j += 1
		if j%10 == 0:
			print()
	while True:
		element = int(input("Please input the value you want to search for:"))
		if element == -1:
			break
		index = fibSearch(data, element)
		# index = BisectionMethod(data, element)
		# index = DifferenceMethod(data, element)
		if index < 0:
			print("We can not find the element in this array.")
		else:
			print("The element", element, "is located in the", index+1, "_th seat of the array.")
		
