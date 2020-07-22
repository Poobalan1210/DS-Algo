'''Program to find longest common substring between two strings'''

def lcs(str1,str2,i,j,count):
	if i>=len(str1) or j>=len(str2):
		return count

	if str1[i]==str2[j]:
		count=lcs(str1,str2,i+1,j+1,count+1)

	return max(count,lcs(str1,str2,i+1,j,0),lcs(str1,str2,i,j+1,0))

def main():
	s1=input()
	s2=input()
	print(lcs(s1,s2,0,0,0))

main()