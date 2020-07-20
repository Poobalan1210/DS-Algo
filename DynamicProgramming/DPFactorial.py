'''This factorial program is build up using bottom up dynamic programming i.e. the tabulation approach'''

def DPfactorial(n):
	table=[0]*(n+1)

	#base case
	table[0]=1 

	for i in range(1,n+1):
		table[i]=table[i-1]*i

	return table[n]

def main():
	n=int(input())
	if n<0:
		print("Negative numbers don't have factorial")
	else:
		print(DPfactorial(n))

main()	