def knapsack(weights, prices, capacity):
	if capacity==0 or len(weights)==0:
		return 0
  
	ans=0
	if weights[0]<=capacity:
		ans1=prices[0]+knapsack(weights[1:],prices[1:],capacity-weights[0])
		ans2=knapsack(weights[1:],prices[1:],capacity)
		ans=max(ans1,ans2)
		
	return ans  

def main():
	weights=list(map(int,input().split()))
	prices=list(map(int,input().split()))
	capacity=int(input())
	ans=knapsack(weights,prices,capacity)
	print(ans)

main()