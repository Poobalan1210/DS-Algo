def catalan(n):
  if n == 0:      # base case; C(0) = 1
    return 1
  sum = 0
  # iterate from 1...n to evaluate: C(0)*C(n-1) + C(1)*C(n-2) ... + C(n-1)*C(0)
  for i in range(n):  
    sum += (catalan(i) * catalan(n-1-i))  # C(i)*C(n-1-i)
  return sum

print(catalan(4))