from stack import Stack

def convertInfixToPostfix(token_exp):
	'''This function converts a token string in infix notation to postfix notation'''
	token_string=token_exp.split()
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

if __name__=="__main__":
	token_string=input()
	output_string=convertInfixToPostfix(token_string)
	print(f"The postfix form of given string \'{token_string}\' is \'{' '.join(output_string)}\'")



