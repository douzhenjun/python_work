#如何用O(1)的时间复杂度求栈中的最小元素？
from SequenceStack import SequenceStack

def GetMin(stack):
	minStack = SequenceStack()
	if stack.IsEmptyStack():
		return
	while not stack.IsEmptyStack():
		popElement = stack.PopStack()
		if minStack.IsEmptyStack():
			minElement = popElement
			minStack.PushStack(minElement)
		else:
			if popElement < minElement:
				minElement = popElement
				minStack.PushStack(minElement)
	return minStack.GetTopStack()

def GetMin2(stack):
	if stack.IsEmptyStack():
		return
	else:
		minElement = stack.PopStack()
	while not stack.IsEmptyStack():
		popElement = stack.PopStack()
		if popElement < minElement:
			minElement = popElement
	return minElement


if __name__ == "__main__":	
	ss = SequenceStack()
	for i in range(10):
		if i % 3 == 1:
			ss.PushStack(i-1)
		else:
			ss.PushStack(i)
	ss.StackTraverse()
	print("The minimum element in the stack is:", GetMin2(ss))
	ss.StackTraverse()

