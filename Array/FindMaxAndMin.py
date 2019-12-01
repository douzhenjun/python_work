class MaxMin:
	#返回值列表中有两个元素，第一个元素为子数组的最小值，第二个元素为最大值
	def getMaxMin(self, arr, l, r):
		if arr == None:
			print("The parameter is illegal!")
			return 
		lst = []
		m = (l+r) // 2							#求中点
		if l == r:								#l与r之间只有一个元素
			lst.append(arr[l])
			lst.append(arr[l])
			return lst
		if l+1 == r:							#l与r之间只有两个元素
			if arr[l] >= arr[r]:
				maxx = arr[l]
				minn = arr[r]
			else:
				maxx = arr[r]
				minn = arr[l]
			lst.append(minn)
			lst.append(maxx)
			return lst
		lList = self.getMaxMin(arr, l, m)		#递归计算左半部分
		rList = self.getMaxMin(arr, m+1, r)		#递归计算右半部分
		maxx = lList[1] if(lList[1]>rList[1])else rList[1]#总的最大值
		minn = lList[0] if(lList[1]<rList[0])else rList[0]#总的最小值
		lst.append(minn)
		lst.append(maxx)
		return lst

if __name__ == "__main__":
	array = [7, 3, 19, 40, 7, 1]
	m = MaxMin()
	result = m.getMaxMin(array, 0, len(array)-1)
	print("max=" + str(result[1]))
	print("min=" + str(result[0]))
		
