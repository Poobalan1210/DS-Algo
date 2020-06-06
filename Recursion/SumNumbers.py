'''This module contains the recursive solution for getting the sum of a list of integers'''

class SumNumbers:
	'''This class is created for the purpose of encapsulating the sum_numbers method'''

	@staticmethod
	def sum_numbers(num_list):
		'''The sum_numbers method sums the numbers in a list and returns it'''
		if len(num_list)==1:
			return num_list[0]
		else:
			return num_list[0]+SumNumbers.sum_numbers(num_list[1:])

if __name__=="__main__":
	num_list=list(map(int,input().strip().split()))
	summ=SumNumbers.sum_numbers(num_list)
	print(f"The sum of this list of numbers {num_list} is {summ}")	