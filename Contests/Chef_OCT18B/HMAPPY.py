'''
Author: Amitrajit Bose
Passes TC: Only Last
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
currmean=sum(a)//n
meanpos=bs(a,currmean)
if(a[meanpos]!=currmean and meanpos>0):
	meanpos=meanpos-1
for i in range(n-1,meanpos,-1):
	diff=abs(a[i]-a[meanpos])
	prevai=a[i]
	a[i]=max(0,a[i]-diff)
	m=m-(prevai-a[i])
	if(m<=0):
		break
s=0
for i in range(n):
	s=max(s,(a[i]*b[i]))
print(s)
