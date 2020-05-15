from stack import Stack 
from InfixToPostfix import convertInfixToPostfix

def convertInfixToPrefix(input_string):
	infix_list=input_string[::-1]
	output_exp=convertInfixToPostfix(infix_list)
	prefix_exp=output_exp[::-1]
	return prefix_exp

if __name__=="__main__":
	input_string=input()
	output_string=convertInfixToPrefix(input_string)
	print(f"The prefix version of given infix string \'{input_string}\' is \'{' '.join(output_string)}\'")