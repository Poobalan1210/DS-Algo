def catalan(n):
    if n==0:
        return 1
    if n==1:
        return 1

    table=[0]*(n+1)
    table[0]=1
    table[1]=1

    for i in range(2,n+1):
        val=0
        for j in range(0,i):
            #print(j,i-j-1)
            val+=table[j]*table[i-j-1]
        table[i]=val

    return table[n]

def main():
	for i in range(int(input())):
		print(catalan(int(input())))

main()