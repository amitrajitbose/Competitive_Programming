# This Fetches TLE
# Expected Approach O(n)
# Moore's Voting Algorithm - [Majority Element]

# This problem has a good implementation of Python dictionary. Thus kept intentionally.
# Problem : SPOJ -> MAJOR

from collections import Counter

t=int(input())

for _ in range(t):
	n=int(input())
	A=[int(x) for x in input().strip().split()]
	D=dict(Counter(A))

	#find the maximum occurance
	mymax=(max(list(D.values())))
	
	#find the item with maximum occurance
	ans=list(D.keys())[list(D.values()).index(mymax)]
	
	#check if condition is satisfied
	if(mymax > n//2):
		print("YES {0}".format(ans))
	else:
		print("NO")
