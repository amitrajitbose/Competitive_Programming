def bs(arr,low,high):
	l=0
	r=len(arr)-1
	while(l<=r):
		mid=l+(r-l)//2
		if(arr[mid]>=low and arr[mid]<=high):
			return True #index present in range
		elif(arr[mid]<low):
			l=mid+1
		else:
			r=mid-1
	return False #element not found

n=int(input())
arr=[int(x) for x in input().strip().split()]
mydict={} #empty dictionary
for i in range(n):
	if(mydict.get(arr[i])):
		mydict[arr[i]].append(i) #entry present, appending
	else:
		mydict[arr[i]]=[i] #entry not present, make it
qn=int(input())
for _ in range(qn):
	l,r,x=[int(x) for x in input().strip().split()]
	if(mydict.get(x)==None):
		print("no")
		continue
	if(bs(mydict[x],l,r)):
		print("yes")
	else:
		print("no")

