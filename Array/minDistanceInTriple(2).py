#如何求解三元组的最小距离
#假设有三个升序整数数组a,b,c,长度分别为l,m,n.
#利用暴力法可以得到三元组的最小距离，但是时间复杂度是O(l*m*n),而且没有用到升序数组的特点，所以一定不是最优解法。
#考虑到他们都是升序数组，假设某一时刻有a[i] <= b[i] <= c[i],显然Distance(i)=c[i]-a[i],
#(1)若c数组向后遍历一位，其余不变，那么显然Distance(i+1)=c[i+1]-a[i] > Distance(i),也就是说遍历c不会找到更小的距离；
#(2)若b数组向后遍历一位，其余不变，那么要么b[i+1]>c[i],要么b[i+1]<=c[i]。如果是前者，那么Distance(i+1)=b[i+1]-a[i]>Distance(i),
#	如果是后者，那么Distance(i+1)=Distance(i)=c[i]-a[i],因而也不会出现更小距离的可能。
#(3)若a数组向后遍历一位，其余不变，那么分情况，(a)如果a[i+1]<b[i],那么Distance(i+1)=c[i]-a[i+1]<Distance(i);(b)如果c[i]>a[i+1]>=b[i],那么
#	Distance(i+1)=c[i]-b[i]<Distance(i);(c)如果a[i+1]>=c[i],那么Distance(i+1)=a[i+1]-b[i],这个距离可能大于c[i]-a[i]，也可能
#	小于c[i]-a[i]:如果a[i+1]-c[i]<b[i]-a[i],那么Distance(i+1)<Distance(i),否则Distance[i+1]>=Distance(i).
#综上，只要考虑最小元素所在数组的向后遍历即可。
#因此，可以这样设计算法，首先初始化minDist=max(abs(a[0]-b[0]),abs(b[0]-c[0]),abs(c[0]-a[0])),假设a[0]<=b[0]<=c[0],所以向后遍历a
#计算max(abs(a[1]-b[0]),abs(...),...),得到的结果与minDist比较，若小，则赋给minDist,依次类推，直到某个当前最小元素已经是所在数组的最后一个元素时，
#算法停止。这种算法，最坏的情况是a,b,c数组全都遍历了一遍，时间复杂度为O(l+m+n)，但即便如此，也比暴力法的O(l*m*n)要快多了。

def maxs(a, b, c):
	if a > b:
		maxs = a
	else:
		maxs = b
	if c > maxs:
		maxs = c
	return maxs
	
def mins(a, b, c):
	if a < b:
		mins = a
	else:
		mins = b
	if c < mins:
		mins = c
	return mins
	
def getMinDist(arr1, arr2, arr3):
	minDist = maxs(abs(arr1[0]-arr2[0]), abs(arr2[0]-arr3[0]), abs(arr3[0]-arr1[0]))
	i = 0
	j = 0
	k = 0
	while True:
		element =  mins(arr1[i], arr2[j], arr3[k])
		if element in arr1:
			i += 1
		elif element in arr2 and element not in arr1:
			j += 1
		elif element in arr3 and element not in arr1 and element not in arr2:
			k += 1
		if i == len(arr1) or j == len(arr2) or k == len(arr3):
			break
		dist = maxs(abs(arr1[i]-arr2[j]), abs(arr2[j]-arr3[k]), abs(arr3[k]-arr1[i]))
		if dist < minDist:
			minDist = dist
	return minDist
	
if __name__ == "__main__":
	a = [3, 4, 5, 7, 15]
	b = [10, 12, 14, 18, 20]
	c = [11, 13, 23, 24, 27, 30]
	print("The minimum distance is:", getMinDist(a,b,c))
	
		
	
	
	
	
	
	
