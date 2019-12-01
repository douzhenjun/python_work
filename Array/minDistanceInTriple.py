#如何求解最小三元组距离
#已知三个升序整数数组a[l],b[m],c[n],请在三个数组中各找一个元素，使得组成的三元组的距离最小。三元组的距离的定义是:
#假设a[i],b[j],c[k]是一个三元组，那么距离为distance = max(|a[i]-b[j]|,|b[j]-c[k]|,|c[k]-a[i]|),请你设计一个
#求最小三元组距离的最优算法.

#蛮力法
#最容易想到的办法就是分别遍历三个数组中的元素，对遍历到的元素分别求出它们的距离然后从这些值里面查找最小值。
def max(a, b, c):
	if a >= b:
		maxs = a
	else:
		maxs = b
	if c >= maxs:
		maxs = c

	return maxs
		
def minDistance(a, b, c):
	aLen = len(a)
	bLen = len(b)
	cLen = len(c)
	minDist = maxs(abs(a[0]-b[0]), abs(a[0]-c[0]), abs(b[0]-c[0]))
	dist = 0
	i = 0
	while i < aLen:
		j = 0
		while j < bLen:
			k = 0
			while k < cLen:
				dist = maxs(abs(a[i]-b[j]), abs(a[i]-c[k]), abs(b[j]-c[k]))
				if minDist > dist:
					minDist = dist
				k += 1
			j += 1
		i += 1
	return minDist

if __name__ == "__main__":
	a = [3, 4, 5, 7, 15]
	b = [10, 12, 14, 16, 17]
	c = [20, 21, 23, 24, 37, 30]
	print("The minimum distance is", str(minDistance(a, b, c)))
