from stack import Stack
from BalancedParenthesis import checkBalancedParenthesis

def convertInfixToPostfix(token_string):
	'''This function converts a token string in infix notation to postfix notation'''
	opstack=Stack() #This will store the incoming operators
	output_string=[] #This will store the output string in infix notation

	prec={} #Precedence dictionary
	prec['(']=1
	prec['+']=2
	prec['-']=2
	prec['*']=3
	prec['/']=3
	prec['**']=4
	#print(prec)

	for token in token_string:

		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" or token in "0123456789":
			output_string.append(token)
		elif token=='(':
			opstack.push('(')
		elif token==')':
			topToken=opstack.pop()
			while topToken!='(':
				output_string.append(topToken)
				topToken=opstack.pop()
		else:
			while not opstack.isEmpty() and prec[opstack.peek()]>=prec[token]:
				output_string.append(opstack.pop())
			opstack.push(token)
		
	while not opstack.isEmpty():              #Pop any remaining characters in the stack to output string
		output_string.append(opstack.pop())

	return output_string

def validate_input(expr):
	#Checking whether the expr is a list, int or string datatype or not
	if not expr:
		print("Not a valid datatype")
		return False
	expr=expr.strip()
	
	#Checking that parenthesis are balanced or not
	bracket_list=[]
	for e in expr:
		if e =='(' or e==')':
			bracket_list.append(e)
	bracket_expr=''.join(bracket_list)
	if not checkBalancedParenthesis(bracket_expr):
		print("Brackets not balanced")
		return False

	tokenList=expr.split(" ")
	sanitized_list=[]

	#Checking space is present between the entered characters or not
	if len(tokenList[0])>1 and type(tokenList[0])==type('a'):
		print("Not separated by spaces")
		return False

	#Checking whether the entered characters are valid or not
	for t in tokenList:
		t=t.strip()
		sanitized_list.append(t)
		if t.isdigit():
			continue
		elif t=='+' or t=='-' or t=='*' or t=='/' or t=='^':
			continue
		elif t in "0123456789":
			continue
		elif t in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
			continue
		elif t =='(' or t ==')':
			continue
		else:
			print("No characters matched")
			return False
	return sanitized_list

def readInput():
	token_string=input()
	validation_result=validate_input(token_string)

	#Asking user input until they enter a valid expression
	while not validation_result:
		print("Invalid token string. Please re-enter or type 'exit' to leave the program")
		token_string=input()
		if token_string=='exit':
			exit()
		validation_result=validate_input(token_string)
	return token_string

if __name__=="__main__":
	token_string=readInput()

	if validate_input(token_string):
		func_arg=token_string.split()
		output_string=convertInfixToPostfix(func_arg)
		print(f"The postfix form of given string \'{token_string}\' is \'{' '.join(output_string)}\'")
	else:
		print("The string is an invalid expression")


