import random
import string

def lcs(str1,str2,i,j,count,memo):
	if i>=len(str1) or j>=len(str2):
		return count

	if (i,j,count) in memo:
		return memo[(i,j,count)]

	c=count

	if str1[i]==str2[j]:
		c=lcs(str1,str2,i+1,j+1,count+1,memo)

	memo[(i,j,count)]=max(c,lcs(str1,str2,i+1,j,0,memo),lcs(str1,str2,i,j+1,0,memo))

	return memo[(i,j,count)]

def main():
	str1=''.join(random.choice(string.ascii_lowercase) for _ in range(40))
	str2=''.join(random.choice(string.ascii_lowercase) for _ in range(60))
	memo=dict()

	print("hello","elf")
	print(lcs("hello","elf",0,0,0,memo))
	print(str1,str2)
	print(lcs(str1,str2,0,0,0,memo))

main()