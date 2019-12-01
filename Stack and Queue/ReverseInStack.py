#翻转栈的所有元素，例如输入{1，2，3，4，5},1在栈顶，翻转后的栈为{5，4，3，2，1},5在栈顶。
#分析：可以把原栈中元素1，2，3，4，5依次出栈，再将出栈的元素依次进入到另一个空栈中，这样第二个栈中元素就相当于第一个栈中元素的翻转.
#但这样的方法会额外分配内存空间，如果只允许在一个栈上操作，应该怎么做？
#我们采用递归思想，这里有两个递归。第一个递归，把栈底元素移到栈顶位置。再对去掉栈顶元素的子栈进行相同的操作。第一个递归结束标志着目的达到。
#第一个递归的终止条件是子栈为空。在第一个递归，把栈底元素移到栈顶位置的细节上，由于栈只能通过栈顶操作，需要另一个递归，这个递归要求不断执行出栈操作，每一次
#出栈获取栈顶元素并标记，直到这个栈为空递归终止，第二个递归的终止条件是操作的栈为空。这个时候让栈底元素5的上一个元素4先进栈，再让栈底元素5进栈，
#这就实现了最下面两个元素5，4的交换，然后子栈的栈顶元素5再与它的上一个元素3交换......
#最后栈中的元素顺序就变为:5,1,2,3,4(自顶而下)。再对1，2，3，4进行第二个递归，直到第一个递归结束。
import SequenceStack as ssk

def moveBottomToTop(s):
	if s.IsEmptyStack():
		return
	top1 = s.GetTopStack()
	s.PopStack()
	if not s.IsEmptyStack():
		moveBottomToTop(s)
		top2 = s.GetTopStack()
		s.PopStack()
		s.PushStack(top1)
		s.PushStack(top2)
	else:
		s.PushStack(top1)
		
def ReverseStack(s):
	if s.IsEmptyStack():
		return
	moveBottomToTop(s)
	top = s.GetTopStack()
	s.PopStack()
	ReverseStack(s)
	s.PushStack(top)
	
if __name__ == "__main__":
	s = ssk.SequenceStack()
	s.PushStack(5)
	s.PushStack(4)
	s.PushStack(3)
	s.PushStack(2)
	s.PushStack(1)
	ReverseStack(s)
	print("The stack sequence after reversing is:")
	while not s.IsEmptyStack():
		print(s.GetTopStack())
		s.PopStack()
		
