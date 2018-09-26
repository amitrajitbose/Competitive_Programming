# https://www.codechef.com/problems/TACHSTCK
# Approach : Greedy

n,d=[int(x) for x in input().strip().split()]
arr=[]
for _ in range(n):
	arr.append(int(input().strip()))
arr=sorted(arr)
c=0
i=0
while(i < n-1):
	if(arr[i]>=arr[i+1]-d):
		i+=2
		c+=1
	else:
		i+=1
print(c)

