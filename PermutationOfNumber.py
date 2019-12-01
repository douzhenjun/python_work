#针对不同的个数n，输出从1到n的所有排列

maxn = 11

hashTable = [False for x in range(maxn)]
p = [0 for x in range(maxn)]

def generateP(index, n):
	if index == n + 1:
		for i in range(1, n+1):
			print(p[i], end=" ")
		print()
		return

	for x in range(1, n+1):
		if hashTable[x] == False:
			p[index] = x
			hashTable[x] = True
			generateP(index+1, n)
			hashTable[x] = False
if __name__ == "__main__":
	generateP(1, 7)
	

	
	
