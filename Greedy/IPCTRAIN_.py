'''
Problem : IPCTRAIN Codechef
Approach : Heap, Greedy
Ref : https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
Author : @amitrajitbose
'''
from heapq import *

def mymaxheapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i][2] < arr[l][2]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest][2] < arr[r][2]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # swap

        # Heapify the root.
        mymaxheapify(arr, n, largest)

t=int(input())
for _ in range(t):
	n,day=[int(x) for x in input().strip().split()]
	arr=[]
	for i in range(n):
		d,t,s=[int(x) for x in input().strip().split()]
		arr.append([d,t,s])
	# now sort according to sadness level, decr
	arr=sorted(arr, key=lambda x: x[2], reverse=True)
	# we need to sort arr w.r.t arr[0], which day they arrive, incr
	arr=sorted(arr, key=lambda x: x[0])
	
	# build heap
	for i in range(n,-1,-1):
		mymaxheapify(arr,n,i)
	heapify(arr)
	if(len(arr)>1):
		if(arr[0][2]<arr[1][2]):
			arr[0],arr[1]=arr[1],arr[0] #swap if not in order
		if(arr[0][0]>arr[1][0]):
			arr[0],arr[1]=arr[1],arr[0]
	
	k=1
	while(day>0):
		print(arr)
		if(arr[0][0]==k):
			arr[0][1]-=1
			if(arr[0][1]==0):
				heappop(arr)
				n-=1
			for i in range(n):
				if(arr[i][0] >= k+1):
					break
				arr[i][0] += 1
		k += 1
		day -= 1
		heapify(arr)
		mymaxheapify(arr,n,0)
	print(arr)
	totalsadness = 0
	for i in range(n):
		totalsadness += (arr[i][1]*arr[i][2])
	print(totalsadness)
