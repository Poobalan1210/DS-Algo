from stack import Stack

def checkBalancedParenthesis(s):
	if len(s)==1:
		return False
	stk=Stack()
	for i in s:
		if i=='(':
			stk.push(i)
		else:
			try:	
				item=stk.pop()
			except IndexError:
				return False
	if stk.size()==0:
		return True
	else:
		return False

if __name__=="__main__":
	str=input()
	print(checkBalancedParenthesis(str))	