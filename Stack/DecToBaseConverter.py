from stack import Stack

def BaseConverter(num,base):
	'''This function converts a decimal value to any base value mentioned between 2 to 36'''
	
	digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	rem_stack=Stack()
	
	#Pushing remainders to remainder stack
	while(num!=0):
		rem=num%base
		rem_converted=digits[rem]
		rem_stack.push(rem_converted)
		num=num//base
	
	#Getting the remainders in reverse order from stack to make the base string
	base_string=""
	while(not rem_stack.isEmpty()):
		base_string=base_string+rem_stack.pop()
	
	return base_string

if __name__=="__main__":
	decimal_val=int(input())
	base=int(input())
	if base>=2 and base<=36:
		base_val=BaseConverter(decimal_val,base)
		print(f"The base {base} value of {decimal_val} is {base_val}")
	else:
		print("Invalid Value. Please enter a value between 2 to 16") 