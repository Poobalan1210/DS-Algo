'''This module contains the solution to convert a python integer into its string equivalent '''

class IntToStr:
	'''This class is a wrapper for holding the static method to_str which converts an integer to its string equivalent'''

	@staticmethod
	def to_str(num):
		'''This method converts takes an integer as argument,convert it to its string equivalent and returns it'''
		convertString="0123456789"
		if num<10:
			return convertString[num]
		else:
			rem=convertString[num%10]
			return IntToStr.to_str(num//10)+rem

if __name__=="__main__":
	number=int(input())
	string_equiv=IntToStr.to_str(number)
	print(f"The string equivalent of {number} is '{string_equiv}' ")