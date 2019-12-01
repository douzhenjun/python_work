#如何从数组中找出满足a+b=c+d的两个数对.
#采用双重循环，两指针，固定一个指针i而遍历另一个指针j(也就是下标)直到j=len(arr)，定义一个字典sumPair，其键是数对的和，其值是
#数对，为此定义一个数对类，一开始存入一个键值对，然后固定i,遍历j,如果和sums是字典sumPair的键,就打印找到的语句，停止查找，函数结束。
#否则把新的和作为键放到字典中，继续遍历，如果循环都结束了还是没有找到合适的key，那么打印没有找到的语句。两次循环时间复杂度为O(n^2),字典的插入和查找
#时间复杂度都是O(1)。所以算法的时间复杂度为O(n^2)。
class pair:
	def __init__(self, first, second):
		self.first = first
		self.second = second
		
def findPairs(arr):
	sumPair = dict()
	n = len(arr)
	
	i = 0
	while i < n:
		j = i + 1
		while j < n:
			sums = arr[i] + arr[j]
			if sums not in sumPair:
				sumPair[sums] = pair(i, j)
			else:
				p = sumPair[sums]
				print("(" + str(arr[p.first]) + "," + str(arr[p.second]) + "),("\
				+ str(arr[i]) + "," + str(arr[j]) + ")")
				return True
			j += 1
		i += 1
	return False
	
if __name__ == "__main__":
	arr = [3, 4, 7, 10, 20, 9, 8]
	findPairs(arr)
