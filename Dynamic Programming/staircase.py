'''
DCP #13
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of 
positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

'''
SOLUTION FOR GENERALISED JUMP SIZE
AUTHOR : Amitrajit Bose
APPROACH : Bottom Up DP
'''
MOD = (10**9)+7
def num_ways(n,steps=[1,2]):
	steps.sort()
	table=[0 for i in range(n+1)]
	for i in steps:
		if(i<=n):
			table[i]=1 #since direct jumps are possible
	for i in range(1,n+1):
		for j in steps:
			if(j>i):
				break
			prev=max(0,i-j)
			table[i] = (table[i] + table[prev])%MOD
	return table[n]%MOD

#  --- TEST CASES ---
assert num_ways(0)==0
assert num_ways(4)==5
assert num_ways(6,[1,3,5])==8
assert num_ways(10)==89
assert num_ways(24)==75025
assert num_ways(84)==93254120