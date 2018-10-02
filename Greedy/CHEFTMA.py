'''
Author : @amitrajitbose
Problem: https://www.codechef.com/problems/CHEFTMA
Approach : Greedy
'''
from bisect import bisect_left as bs
def binsrch(arr,x):
	if(len(arr)==0):
		return 0
	k=bs(arr,x)
	if(x>arr[-1]):
		tmp=arr[-1]
		arr.pop(-1)
		return [arr,tmp]
	if(arr[k]==x):
		arr.pop(k)
		return [arr,x]
	if(k==0):
		return [arr,0]
	else:
		tmp=arr[k-1]
		arr.pop(k-1)
		return [arr,tmp]

t=int(input())
for _ in range(t):
	n,w,b=[int(x) for x in input().strip().split()]
	a=[int(x) for x in input().strip().split()]
	b=[int(x) for x in input().strip().split()]
	for i in range(n):
		a[i]=a[i]-b[i] #remaining work
	button=[int(x) for x in input().strip().split()]
	tmp=[int(x) for x in input().strip().split()]
	button.extend(tmp)
	button=sorted(button)
	a=sorted(a, reverse=True)
	answer=0
	for i in range(n):
		if(a[i]==0):
			continue
		button,k=binsrch(button,a[i])
		answer += (a[i]-k)
	print(answer)

