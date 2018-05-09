#https://www.codechef.com/DEME2018/problems/CREP/

import collections
t=int(input())
for _ in range(t):
	n,k=[int(x) for x in input().strip().split()]
	a=[int(x) for x in input().strip().split()]
	counter=collections.Counter(a)
	summ=0
	flag=0
	for i in counter.keys():
		if(counter[i]==k):
			summ+=i
			flag=1
	if(flag==1):
		print(summ)
	elif(flag==0):
		print(-1) 