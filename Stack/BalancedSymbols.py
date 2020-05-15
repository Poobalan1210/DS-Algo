from stack import Stack

def checkBalancedSymbols(symbolString):
	index=0
	balanced=True
	stk=Stack()
	while index<len(symbolString) and balanced:
		symbol=symbolString[index]
		if symbol=='(' or symbol=='[' or symbol=='{':
			stk.push(symbol)
		else:
			if stk.isEmpty():
				balanced=False
			else:
				item=stk.pop()
				if symbol==')' and item=='(':
					pass
				elif symbol==']' and item=='[':
					pass
				elif symbol=='}' and item=='{':
					pass
				else:
					balanced=False
		index+=1

	if stk.size()==0 and balanced:
		return True
	else:
		return False

if __name__=="__main__":
	s=input()
	print(checkBalancedSymbols(s))