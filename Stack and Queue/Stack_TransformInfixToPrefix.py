#Infix expression to Prefix expression
#Question:Assume that there is an infix expression, how to transform it to the prefix expression by stack method?
#Analysis:To set two stacks which store operator(运算符) and operand(操作数).from right to left, when meet operand, push
#		it in operand stack, when meet operator, discuss its priority(优先级):if operator stack is empty, push in;if operator stack
#		is prior to(or equals to) the top of the stack, push in;else, pop the pop element of the operator stack, and push it in the
#		operand stack.Notice that operator "(" has the highest priority, that means when meet "(", pop the top of the operator stack,
#		when meet ")" ,push it to the operator stack undoubtedly, any other operator is prior to the ")" which means it can be push in 
#		the operator stack when the top is ")". When meet the "(", pop the element until the top is the ")", "(" and ")" will not be 
#		pushed in the operand operator.
#The feature of the prefix expression: Operator's seat is before the operand's seat,  
#									The two closest operands(操作数) to the operator perform the operator's computation.
#									The prefix expression does not display the parenthesis characters.(前序表达式不显示括号字符)

from SequenceStack import SequenceStack


def priority(x):
	if str(x) in "+-":
		return 1
	if str(x) in "*/":
		return 2
	else:
		return 0 

def InToPre(expression):
	operatorStack = SequenceStack()
	operandStack = SequenceStack()
	for i in expression[::-1]:
		if i in "0123456789":
			operandStack.PushStack(i)
		else:
			if i in "+-*/":
				while priority(i) < priority(operatorStack.GetTopStack()):
					x = operatorStack.PopStack()
					operandStack.PushStack(x)
					if operatorStack.IsEmptyStack():
						break
				operatorStack.PushStack(i)
			if i == ")":
				operatorStack.PushStack(i)
			if i == "(":
				while operatorStack.GetTopStack() != ")":
					x = operatorStack.PopStack()
					operandStack.PushStack(x)
				operatorStack.PopStack()
				
	while not operatorStack.IsEmptyStack():
		x = operatorStack.PopStack()
		operandStack.PushStack(x)

	y = ""
	while not operandStack.IsEmptyStack():
		x = operandStack.PopStack()
		y += x
	return y
	
if __name__ == "__main__":
	expression = "(3+4)*5+6/(7+8*9)+8"
	print("The original infix expression is\n", expression)
	u = InToPre(expression)
	print("The present prefix expression is\n", u)
	
				
