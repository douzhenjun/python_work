#优化的动态规划法求数组最大连续和问题
#在getMaxSumInSubArray(2)中，每次其实只用到了End[i-1]和All[i-1]，而不是整个数组中的值，因此，可以定义两个变量来保存End[i-1]和All[i-1]的值
#并且可以反复利用。实现代码如下:
def maxSubArray(arr):
	nAll = arr[0]	#最大子数组和
	nEnd = arr[0]	#包含最后元素的最大子数组和
	i = 1
	while i < len(arr):
		nEnd = max(nEnd + arr[i], arr[i])
		nAll = max(nEnd, nAll)
		i += 1
	return nAll
	
if __name__ == "__main__":
	arr = [1, -2, 4, 8, -4, 7, -1, -5]
	print("The max sum of the subarray is", str(maxSubArray(arr)))

#这种方法在保证了时间复杂度为O(N)的基础上，把算法的空间复杂度也降到了O(1).
