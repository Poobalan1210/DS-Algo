from stack import Stack 

def reverseString(input_string):
	char_stack=Stack()
	for char in input_string:
		char_stack.push(char)

	output_string=""
	while not char_stack.isEmpty():
		output_string+=char_stack.pop()

	return output_string

if __name__=="__main__":
	input_str=input()
	print(reverseString(input_str))