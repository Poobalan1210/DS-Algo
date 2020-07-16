def staircase(n, m):
  #In this case, we have reached apartment, hence return 1
  if n==0:
    return 1
    
  #Now we will use recursion to calculate the number of ways
  else:
    ways=0
    for i in range(1,m+1):
      if i<=n:
        ways+=staircase(n-i,m)
    return ways

def main():
    #number of testcases
    t=int(input())

    for i in range(t):
        n,m=map(int,input().split())
        ans=staircase(n,m)
        print(f"staircase({n},{m}) = {ans}")

if __name__=="__main__":
    main()