s,r=[int(x) for x in input().strip().split()]
arr=[int(x) for x in input().strip().split()]
ranges=[]
for _ in range(r):
	i,j=[int(x) for x in input().strip().split()]
	ranges.append((i,j))

for c in ranges:
	count=0
	for i in arr:
		if(i>=c[0] and i<=c[1]):
			count+=1
	print(count)
#RUNTIME ERROR