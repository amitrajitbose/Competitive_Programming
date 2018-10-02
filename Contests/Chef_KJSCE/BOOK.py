from bisect import bisect_left as bs
t=int(input())
for _ in range(t):
	n,m=[int(x) for x in input().strip().split()]
	arr=[int(x) for x in input().strip().split()]
	arr=sorted(arr)
	start=[int(x) for x in input().strip().split()]
	finish=[int(x) for x in input().strip().split()]
	q=len(start)
	for i in range(q):
		#print(start[i],"->",finish[i],"--",end=" ")#debug
		s=bs(arr,start[i])
		e=bs(arr,finish[i])
		if(start[i]>arr[-1] or finish[i]<arr[0]):
			print("{0} {1}".format(0,0))
		elif(s!=e):
			print("{0} {1}".format(abs(e-s),sum(arr[s:e])))
		elif(s==e):
			if(arr[s]==start[i] or arr[e]==finish[i]):
				print("{0} {1}".format(1,arr[s]))
			else:
				print("{0} {1}".format(0,0))
