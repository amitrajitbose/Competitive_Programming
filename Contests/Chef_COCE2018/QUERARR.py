from bisect import bisect_left as bsl
n=int(input())
arr=[int(x) for x in input().strip().split()]
arr=sorted(arr)
q=int(input())
for _ in range(q):
	low,high,val=[int(x) for x in input().strip().split()]
	p=bsl(arr[low:high],val)
	#print(p+low)
	if(arr[p+low]==val):
		print("yes")
	else:
		print("no")

