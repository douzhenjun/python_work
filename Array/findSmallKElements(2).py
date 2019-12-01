def findSmallK(arr, k):
	if k > len(arr):
		print("The k's value is out the range of the array!")
		return
	for i in range(k):
		for j in range(i+1, len(arr)):
			if arr[j] < arr[i]:
				arr[j],arr[i] = arr[i], arr[j]
	print("The",k,"-th smallest number in this array is", arr[k-1])

if __name__ == "__main__":
	array = [12, 22, 14, 2, 55, 3, 22, 4, 45, 63, 33]
	findSmallK(array, 8)
				
