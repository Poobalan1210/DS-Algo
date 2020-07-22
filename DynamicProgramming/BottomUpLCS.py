import random
import string

def lcs(str1,str2):
	m=len(str1)
	n=len(str2)

	dp=[[0 for i in range(m+1)] for j in range(n+1)]

	max_length=0

	for i in range(n+1):
		for j in range(m+1):
			if str1[j-1]==str2[i-1]:
				dp[i][j]=dp[i-1][j-1]+1
				max_length=max(dp[i][j],max_length)
			else:
				dp[i][j]=0

	return max_length

def main():
	str1=''.join(random.choice(string.ascii_lowercase) for _ in range(400))
	str2=''.join(random.choice(string.ascii_lowercase) for _ in range(600))
	print(lcs(str1,str2))

	print(lcs("hel","elf"))

main()