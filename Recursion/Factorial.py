def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

def main():
	n=int(input())
	if n<0:
		print("Factorial can be found of only positive number!!")
	else:
		print(factorial(n))
		
main()