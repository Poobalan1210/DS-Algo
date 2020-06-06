'''This module contains the function to reverse a string'''

def reverseString(original_string):
	'''This method takes a string and reverses and returns it'''
	if len(original_string)<2:
		return original_string
	else:
		return reverseString(original_string[1:])+original_string[0]

if __name__=="__main__":
	string=input()
	reversed_string=reverseString(string)
	print(f"The reverse of {string} is {reversed_string}")