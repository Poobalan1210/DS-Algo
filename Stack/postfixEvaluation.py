from stack import Stack

def doMath(first,second,operator):
	if operator=='+':
		return first+second
	elif operator=='-':
		return first-second
	elif operator=='*':
		return first*second
	elif operator=='/':
		return first/second
	else:
		return first%second

def evaluatePostfix(postfix_string):
	opstack=Stack()
	print(postfix_string)
	for token in postfix_string:
		if token in "0123456789":
			opstack.push(int(token))
		else:
			second_operand=opstack.pop()
			first_operand=opstack.pop()
			op_result=doMath(first_operand,second_operand,token)
			opstack.push(op_result)
	return opstack.pop()

if __name__=="__main__":
	postix_expression=input()
	result=evaluatePostfix(postix_expression)
	print(f"The result of postfix expression {postix_expression} is {result}")
