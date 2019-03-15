from math import floor
from collections import defaultdict
for _ in range(int(input())):
	n,k=map(int,input().strip().split())
	inp = input().strip()
	inp = '0 ' + inp
	a=[int(x) for x in inp.split()]
	
	# Core calculation: Greedy
	spot=n+1
	dic = defaultdict(int).fromkeys(a)
	prefsum = [0]*(n+10)
	#First trip
	for i in range(1, 2):
		for j in range(i, n+1):
			val = floor(a[j]/(j-i+1))
			lb = (a[j]//(val+1))+1
			dic[a[j]] = [val, lb] #correct val and lower bound
			prefsum[j] = prefsum[j-1]+val
	#start from first again
	#print(dic)
	for i in range(1,n+1):
		#print(dic[a[i]])
		if(dic[a[i]][1]<=1):
			cost = prefsum[n]-prefsum[i-1]
		else:
			#recalculate
			prefsum[i-1]=0
			for j in range(i, n+1):
				val = floor(a[j]/(j-i+1))
				lb = (a[j]//(val+1))+1
				dic[a[j]] = [val, lb] #correct val and lower bound
				prefsum[j] = prefsum[j-1]+val
			cost = prefsum[n] - prefsum[i-1]
		if(cost <= k):
			spot = min(spot, i)
			break
	print(spot)
