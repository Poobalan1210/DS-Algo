#For storing memoized results using dynamic programming
memo=dict()

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n]=fib(n-1)+fib(n-2)
        return memo[n]
        
def main():
    #Taking number of test cases
    t=int(input())

    #Taking each test case one by one and computing fibonacci number
    for i in range(t):
        n=int(input())
        ans=fib(n)
        print(ans)

if __name__=="__main__":
    main()