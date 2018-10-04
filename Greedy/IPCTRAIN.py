'''
Author : @amitrajitbose
Problem Link : https://www.codechef.com/JULY17/problems/IPCTRAIN
Approach : Greedy
Complexity : O(day*nlogn)
Remarks : Bound to get TLE. Need a max heap for better performance.
'''
t=int(input())
for _ in range(t):
	n,day=[int(x) for x in input().strip().split()]
	arr=[]
	for i in range(n):
		d,t,s=[int(x) for x in input().strip().split()]
		arr.append([d,t,s])
	
	# now sort according to sadness level
	# jo sabse zyada sad hota h usko zyada wait mat karwao
	arr=sorted(arr, key=lambda x: x[2], reverse=True)
	# we need to sort arr w.r.t arr[0], which day they arrive
	arr=sorted(arr, key=lambda x: x[0])
	k=1
	while(day>0):
		print(arr)
		if(arr[0][0]==k):
			#curr=arr[0] #current trainer
			arr[0][1]-=1 #since he takes one lecture
			if(arr[0][1]==0):
				arr.pop(0) #if all lectures taken then pop, no need
				n-=1 # if popped then maintain total

			for i in range(n):
				if(arr[i][0] >= k+1):
					break
				arr[i][0]+=1 #one day passes
		
		k+=1 #going to next day
		day=day-1
		arr=sorted(arr, key=lambda x: x[2], reverse=True)
		# we need to sort arr w.r.t arr[0], which day they arrive
		arr=sorted(arr, key=lambda x: x[0])
	print(arr)
	totalsadness=0
	for i in range(n):
		totalsadness += (arr[i][1]*arr[i][2])
	print("TOTAL SADNESS: ", totalsadness)
	print(totalsadness)