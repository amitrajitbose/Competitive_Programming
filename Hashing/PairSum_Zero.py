'''
Pair Sum Will Be Zero
Print such pairs from the array
Approach: Hashing
'''
def findPair(arr):
	myhash={}
	#sweep 1
	for i in arr:
		if i in myhash:
			myhash[i]+=1
		else:
			myhash[i]=1
	#sweep 2
	for i in arr:
		if(i==0):
			continue
		comp=0-i
		if(comp in myhash):
			f=myhash[i]*myhash[comp]
			myhash[i]=0
			myhash[comp]=0
			for j in range(f):
				print(min(i,comp),max(i,comp))


a=[int(x) for x in input().strip().split()]
findPair(a[1:])
