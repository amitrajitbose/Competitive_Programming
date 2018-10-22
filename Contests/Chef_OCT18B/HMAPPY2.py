
'''
Author: Amitrajit Bose
Passed only last test case
'''
from bisect import bisect_left as bs
n,m=[int(x) for x in input().strip().split()]
a=[int(x) for x in input().strip().split()]
b=[int(x) for x in input().strip().split()]
arr=[]
for i in range(n):
	arr.append((a[i],b[i],a[i]*b[i]))
arr=sorted(arr, key=lambda x: x[2])
arr=sorted(arr, key=lambda x: x[1])
for i in range(n):
	a[i],b[i]=arr[i][0],arr[i][1]

for i in range(n-2,-1,-1):
	if(a[i]<a[i+1] and m>=(a[i+1]-a[i])):
		delta=a[i+1]-a[i]
		m-=delta
		a[i+1]-=delta
		for j in range(i+2,n,1):
			if(m>=delta):
				a[j]-=delta
	if(m<=0):
		break
	else:
		delta=m
		a[-1]=max(0,a[-1]-m)
		m-=delta
#if(m>0):
#	a[-1]-=m
s=0
for i in range(n):
	s=max(s,(a[i]*b[i]))
print(s)
