from stack import Stack

def DecToBin(num):
	'''This function converts an integer in base 10 to an integer in base 2 or say its binary value'''
	stk=Stack()
	while(num!=0):
		stk.push(num%2)
		num=num//2
	s=""
	while(not stk.isEmpty()):
		s+=str(stk.pop())
	return s

if __name__=="__main__":
	decimal_val=int(input())
	binary_val=DecToBin(decimal_val)
	print(f"Binary value of {decimal_val} is {binary_val}")
