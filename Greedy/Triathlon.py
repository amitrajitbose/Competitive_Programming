'''
Author : @amitrajitbose
Problem : https://www.codechef.com/INOIPRAC/problems/INOI1201
Approach : Greedy
'''
n=int(input())
arr=[]
pref=[0]
for _ in range(n):
	r=[int(x) for x in input().strip().split()]
	r.append(r[1]+r[2]) #sum of last two
	r.append(r[3]+r[0]) #total time
	arr.append(r)
arr=sorted(arr,key=lambda x: x[0])
arr=sorted(arr,key=lambda x: x[3], reverse=True)
for i in arr:
	pref.append(pref[-1]+i[0])
totaltime=arr[0][4]
for i in range(1,n):
	tmp=pref[i]+arr[i][4]
	totaltime=max(totaltime,tmp)
print(totaltime)
