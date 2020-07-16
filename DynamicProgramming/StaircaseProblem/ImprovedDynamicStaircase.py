def nthStairs(n, m,memo):
  #In this case, we have reached apartment, hence return 1
  if n==0:
    return 1

  #We will see if memoized result is present or not
  if n in memo:
    return memo[n]

  #else we will find the result by recursion
  else:
    ways=0
    for i in range(1,m+1):
      if i<=n:
        ways+=nthStairs(n-i,m,memo)

    memo[n]=ways
    return memo[n]

def staircase(n,m):
    memo=dict()
    return nthStairs(n,m,memo)

def main():
    #number of testcases
    t=int(input())

    for i in range(t):
        n,m=map(int,input().split())
        ans=staircase(n,m)
        print(f"staircase({n},{m}) = {ans}")

if __name__=="__main__":
    main()