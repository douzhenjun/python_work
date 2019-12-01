#输入两个整数序列，其中一个序列表示栈的push顺序，判断另一个序列有没有可能是对应的pop顺序。
#分析：首先分别输入push元素和pop元素，并分别存入push数组跟pop数组中。再建立一个栈对象，将push元素逐一入栈，每次入栈将栈顶元素与pop当前位置元素进行比较，
#如果相等，则停止入栈，将栈顶元素出栈，pop后移，再比较栈顶元素与pop当前位置元素是否相等，若相等，继续出栈，若不相等，继续从push入栈。基本的while循环就是这样。
#条件判断：当出栈次数等于pop数组的长度时，pop可能是push的pop；当出栈次数小于pop数组的长度时，pop一定不是push的pop；因为这里的push元素一定要进栈而且只能进栈
#一次，所以无论什么结果，一定有出栈次数小于等于pop数组长度，因为有进栈才会有出栈，所以如果出栈次数等于pop数组的长度，那么栈一定为空(反之不一定成立)，所以不
#用担心出现pop已经遍历完了但是栈还没空的情况。因为出栈条件比较严格，所以有可能push这边元素全部遍历完了，pop元素还没有遍历完，或者说这个时候栈还没有空，一旦
#push这边元素已经遍历完了，而pop那边元素至少还有一个没有被遍历，(只有经过了比较并且满足出栈条件了才称作被遍历完了，只有比较，没有pop后移就叫未遍历)，说明出栈
#次数一定小于pop数组长度，也就是pop一定不是push的pop。
from SequenceStack import SequenceStack

def Evaluate(push, pop):
	ss = SequenceStack(10)
	pushindex = 0
	popindex = 0
	ss.PushStack(push[pushindex])
	while True:
		while ss.GetTopStack() != pop[popindex]:
			pushindex += 1
			if pushindex == len(push):
				print("The latter is not the pop of the former!")
				return
			ss.PushStack(push[pushindex])
		while ss.GetTopStack() == pop[popindex]:
			ss.PopStack()
			popindex += 1
			# if ss.IsEmptyStack() and popindex == len(pop):
			if popindex == len(pop):
				print("The latter is the pop of the former!")
				return
				
if __name__ == "__main__":
	push = []
	flag = True
	while flag:
		epush = input("Please input the element: ")
		if epush!= '#':
			push.append(epush)
		else:
			flag = False
	print("The rank of elements which are pushed in stack is: ", push)
	pop = []
	flag = True
	while flag:
		epop = input("Please input the element: ")
		if epop != '#':
			pop.append(epop)
		else:
			flag = False
	print("The rank of elements to be tested whether are might be poped by the former is: ", pop)
	
	Evaluate(push, pop)
	

			
				
				
	
