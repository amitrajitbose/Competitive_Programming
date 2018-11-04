'''
Problem Name: Boredom - Codeforces
Approach - Dynamic Programming
'''
import itertools
n=int(input())
arr=[int(x) for x in input().strip().split()]
dp=list(itertools.repeat(0,((10**5)+2)))

myd={}

for i in arr:
	if i in myd:
		myd[i]+=1
	else:
		myd[i]=1

if 1 in myd:
	dp[1]=myd[1]

for i in range(2,(10**5)+1):
	# either we dont take the ith number
	# or we take it and thus all i-1 will also be deleted
	# not considering i+1 because it has not been yet computed
	if(i in myd):
		x = max(dp[i-1], dp[i-2]+(i*myd[i]))
	else:
		x = max(dp[i-1], dp[i-2])
	dp[i]=x

print(dp[10**5])

