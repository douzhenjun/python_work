#归并排序法(Merge Sort)
'''对于给定的一组记录，长度为n，首先将每两个相邻的长度为1的子序列进行归并，得到n/2个长度为2或1
   的子序列，再将其两两归并，反复执行此过程，直到得到一个有序序列为止。
'''
def merge(left, right):
	i, j = 0, 0
	result = []
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result
	
def merge_sort(lists):
	if len(lists) <= 1:
		return lists
	num = len(lists)//2
	left = merge_sort(lists[:num])
	right = merge_sort(lists[num:])
	return merge(left, right)
	
if __name__ == "__main__":
	lists = [3,4,2,8,9,5,1]
	print("排序前序列为: ")
	for i in lists:
		print(i, end=" ")
	print("\n 排序后的结果为: ")
	for i in (merge_sort(lists)):
		print(i, end=" ")
