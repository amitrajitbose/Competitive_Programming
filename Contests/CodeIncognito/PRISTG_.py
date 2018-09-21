# https://www.codechef.com/INCC2018/problems/PRISTG/

a=str(input().strip())
b=str(input().strip())
c=0

for i in range(0,len(a)):
	for j in range(i+1,len(a)+1):
		#print(a[i:j])
		if(a[i:j] in b):
			c+=1
print(c)
