'''This module contains the code which tries to mimic recursion
using stack to convert an integer of a base into a string'''
import sys
sys.path.append('../')
from Stack.stack import Stack

def int_to_str(n,base):
	convert_string="0123456789"
	rem_stack=Stack()
	
	#Code to push digits onto the stack
	while n>0:
		if n<base:
			rem_stack.push(n)
		else:
			rem_stack.push(n%base)
		n=n//base
	
	#Code to get back the stack values
	equiv_string=""
	while not rem_stack.isEmpty():
		equiv_string=equiv_string+convert_string[rem_stack.pop()]
	return equiv_string if len(equiv_string)>1 else "0"

if __name__=="__main__":
	number=int(input())
	equiv_string=int_to_str(number,2)
	print(f"The equivalent string if {number} is '{equiv_string}'")