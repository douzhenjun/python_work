#如何在二叉树中找出与输入整数相等的所有路径
#从树的根结点开始往下访问一直到叶子节点经过的所有结点形成一条路径。找出所有的这些路径，
#使其满足这条路径上的所有结点数据的和等于给定的整数。

import random
from SequenceStack import SequenceStack

SIZE = 10

#建立一个随机二叉树
class BTNode:
	def __init__(self):
		self.data = None
		self.lchild = None
		self.rchild = None

def constructBT(arr, start, end):
	root = None
	if end >= start:
		root = BTNode()
		mid = (start+end+1) // 2
		root.data = arr[mid]
		root.lchild = constructBT(arr, start, mid-1)
		root.rchild = constructBT(arr, mid+1, end)
	else:
		root = None
	return root

def constructBT2(arr):
	root = BTNode()
	index = 0
	root.data = arr[index]
	index += 1
	while index < len(arr):
		root.lchild.data = arr[index]
		index += 1
		root.rchild.data = arr[index]
		index += 1
	
def TraverseInPreOrder(root):
	if root == None:
		return
	print(root.data)
	TraverseInPreOrder(root.lchild)
	TraverseInPreOrder(root.rchild)

def random_int_list(length):
	i = 0
	lst = []
	while i < length :
		data = random.randint(-10, 10)
		if data not in lst:
			lst.append(data)
		else:
			continue
		i += 1
	return lst

def searchPath(root, stack, dictt, summ = 0):			
	if root != None:
		stack.PushStack(root.data)
		summ += root.data
		searchPath(root.lchild, stack, dictt, summ)
		searchPath(root.rchild, stack, dictt, summ)
		if root.lchild == None and root.rchild == None:
			dictt[root.data] = summ
			stack.StackTraverse()
		stack.PopStack()
		return dictt									#这个函数最终在这里终止计算
	else:
		return dictt

#判断路径是否存在，若存在，打印出所有这样的路径，若不存在，输出路径不存在字样
def EvaluatePath(root, num, dictt, stack):
	flag = False
	for key in dictt.keys():
		if dictt[key] == num:
			print("The target path is:")
			flag = True
			getPath(root, key, stack)
	if flag == False: 
		print("There is no path that satisfies its sum is", num, ".")

#寻找满足叶子节点为k的路径，并打印出来，利用栈存储沿途经过的结点		
def getPath(root, k, stack):
	if root != None:
		stack.PushStack(root.data)
		if root.data == k:
			stack.StackTraverse()
			return
		else:
			getPath(root.lchild, k, stack)
			getPath(root.rchild, k, stack)
			stack.PopStack()
	else:
		return


if __name__ == "__main__":
	# arr = random_int_list(10)
	arr = [1, 2, 3, -1, 4, 6, -11, 8, 9, -3]
	print(arr)
	root = constructBT(arr, 0, len(arr)-1)
	TraverseInPreOrder(root)
	print()
	stack = SequenceStack()
	dictt = dict()
	new_dict = searchPath(root, stack, dictt)
	print(new_dict)
	stack = SequenceStack()
	EvaluatePath(root, 12, new_dict, stack)
	
	
	
	
