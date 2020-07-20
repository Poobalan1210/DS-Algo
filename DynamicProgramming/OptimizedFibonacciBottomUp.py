def fibonacci(n):
	if n==1:
		return 0
	if n==2:
		return 1

	second_last=0
	last=1
	current=None

	for i in range(3,n+1):  #considering 1 and 2 position are already calculated
		current=last+second_last
		second_last=last
		last=current

	return current

def main():
	n=int(input())
	if n<1:
		print("Please enter positive number!!!")
	else:
		print(fibonacci(n))

main()