# MockVita Problem: Finding sum

def Combinations(mylist,prime):
	count=0
	length=len(mylist)
	for i in range(n-2):
		for j in range(i+1,n-1):
			for k in range(j+1,n):
				if((mylist[i]+mylist[j]+mylist[k])%prime==0):
					count+=1
				count=count%1009
	return count

n,p=[int(x) for x in input().strip().split(',')]
arr=[int(x) for x in input().strip().split(',')]
c=(Combinations(arr,p))
print(c)