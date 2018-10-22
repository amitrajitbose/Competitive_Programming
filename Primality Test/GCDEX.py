
'''
Author: @amitrajitbose
'''
phi=[0 for x in range(1000005)]
phi[1]=1
for i in range(2,1000002):
	if(phi[i]==0):
		phi[i]=i-1
		for j in range(i+1,1000001,i):
			if(phi[j]==0):
				phi[j]=j
			phi[j]-=phi[j]/i
res=[0 for x in range(1000001)]
for i in range(1,1000001):
	for j in range(i+1,1000001,i):
		res[j]+=(i*phi[j//i])

for i in range(1,1000001):
	res[i]+=res[i-1]
n=1
while(n!=0):
	n=int(input())
	if(n==0):
		break
	else:
		print(res[n])



