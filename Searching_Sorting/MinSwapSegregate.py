'''
Given a binary string segregate 1s and 0s by swapping only adjacent elements. You need to print the minimum number
of adjacent swaps required to bring all 1s in front and all 0s behind it or vice versa
'''
def minswap(arr):
	oneptr=0
	onepenalty=0
	zeroptr=0
	zeropenalty=0
	n=len(arr)
	for i in range(n):
		if(arr[i]==1):
			onepenalty+=(i-oneptr)
			oneptr+=1
		if(arr[i]==0):
			zeropenalty+=(i-zeroptr)
			zeroptr+=1
	return(min(onepenalty,zeropenalty))

print(minswap([1,1,1,0,1,0]))
print(minswap([1,0,0,0,0,1]))
print(minswap([0,0,1,1,0,0]))
print(minswap([1,1,0,1,0,0]))
print(minswap([0,0,1,0,0,1]))
print(minswap([1,0,0,1,1]))
print(minswap([1,0,1,0,1,1]))