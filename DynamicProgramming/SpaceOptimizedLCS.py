import random
import string

def lcs(str1,str2):
	n=len(str1)
	m=len(str2)

	dp=[0 for i in range(n+1)]

	max_length=0

	for j in range(1,m+1):
		thisrow=[0 for i in range(n+1)]

		for i in range(1,n+1):
			if str1[i-1]==str2[j-1]:
				thisrow[i]=dp[i-1]+1
				max_length=max(thisrow[i],max_length)
			else:
				thisrow[i]=0

		dp=thisrow

	return max_length

def main():
	str1=''.join(random.choice(string.ascii_lowercase) for _ in range(400))
	str2=''.join(random.choice(string.ascii_lowercase) for _ in range(600))
	print(lcs(str1,str2))

	print(lcs("hel","elf"))

main()