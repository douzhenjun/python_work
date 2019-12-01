#判断一个数组是否是二元查找树后序遍历的序列
#分析:输入一个整数数组，判断该数组是否是二元查找树的后序遍历的结果，如果是，返回true.
#	 否则返回false.例如数组[1, 3, 2, 5, 7, 6, 4]就是二叉树4-2-6-1-3-5-7的后序遍历。
#二元查找树:一种二叉树，它满足对树中任意一个结点，它的所有左子树的结点的值都小于这个结点的值，
#			而它所有右子树的结点的值都大于这个结点的值


#判断一个数组是否是二元查找树的后序遍历序列
#输入参数:arr(数组)
#返回值:是,返回true,否则返回False
def IsAfterOrder(arr, start, end):
	if arr == None:
		return False
	#如果该数组是二元查找树的后序遍历序列，那么数组的最后一个元素一定是根结点，也就是整个二叉树的根结点root
	root = arr[end]
	
	i = start
	while i < end:
		if(arr[i] > root):
			break
		i += 1
	j = i					#找到第一个大于root结点的值的位置，将它赋给j，对j以后的元素遍历，如果出现
	while j < end:			#j以后的元素小于root的，则该序列不是，否则分别判断小于root值的序列和大于root值
		if arr[j] < root:	#的序列是否是某一个二元查找树的后序遍历
			return False
		j += 1
	left_IsAfterOrder = True
	right_IsAfterOrder = True
	if i > start:
		left_IsAfterOrder = IsAfterOrder(arr, start, i-1)
	if i < end:
		right_IsAfterOrder = IsAfterOrder(arr, i, end-1)
	return left_IsAfterOrder and right_IsAfterOrder
		

if __name__ == "__main__":
	arr = [1, 2, 4, 5, 3, 7, 8, 10, 9, 6]
	result = IsAfterOrder(arr, 0, len(arr)-1)
	i = 0
	while i < len(arr):
		print(arr[i])
		i += 1
	if result:
		print("The sequence is the post order traverse array.")
	else:
		print("The sequence is not the post order traverse array.")
		
