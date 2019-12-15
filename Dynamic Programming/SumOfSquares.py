'''
Given a number n, find the least number of squares needed to sum up to the number.
'''
from math import ceil, sqrt
def square_sum(n):
	dp = [0] * (n+1)
	for i in range(4):
		dp[i] = i
	for i in range(4, n+1):
		dp[i] = i # max value is always by 1*1 + 1*1 + 1*1 ...
		for j in range(1, ceil(sqrt(i))+1):
			tmp = j**2
			if tmp > i:
				break
			dp[i] = min(dp[i], 1+dp[i-tmp])
	op = dp[n]
	del dp
	return op

assert(square_sum(13)== 2)
assert(square_sum(4) == 1)
assert(square_sum(6) == 3)

