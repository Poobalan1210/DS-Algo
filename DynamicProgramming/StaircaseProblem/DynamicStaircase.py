staircase_costs=dict()

def staircase(n, m):
  #In this case, we can't enter any value. Hence no way
  if n<0:
    return 0

  #In this case, we have reached apartment, hence return 1
  if n==0:
    return 1

  #We will see if memoized result is present or not
  if (n,m) in staircase_costs:
    return staircase_costs[(n,m)]

  #else we will find the result by recursion
  else:
    cost=[0]*(m+1)
    for i in range(1,m+1):
      cost[i]=staircase(n-i,m)

    staircase_costs[(n,m)]=sum(cost)
    return staircase_costs[(n,m)]

def main():
    #number of testcases
    t=int(input())

    for i in range(t):
        n,m=map(int,input().split())
        ans=staircase(n,m)
        print(f"staircase({n},{m}) = {ans}")

if __name__=="__main__":
    main()