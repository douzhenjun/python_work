#如何对数组进行旋转，将一个n*n的二维数组逆时针旋转45度后打印，具体形式看书上第147页

def rotateArr(arr):
	lens = len(arr)
	#打印二维数组中的右上半部分
	i = lens - 1
	while i > 0:
		row = 0
		col = i
		while col < lens:
			print(arr[row][col])
			row += 1
			col += 1
		print("\n")
		i -= 1
	#打印二维数组左下半部分(包括对角线)
	i = 0
	while i < lens:
		row = i
		col = 0
		while row < lens:
			print(arr[row][col])
			row += 1
			col += 1
		print("\n")
		i += 1
if __name__ == "__main__":
	arr = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
	rotateArr(arr)
	
