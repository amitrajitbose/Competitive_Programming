'''
Author : @amitrajitbose
Problem : https://www.codechef.com/problems/LEMUSIC
Approach : Greedy
'''
t=int(input())
for _ in range(t):
	n=int(input())
	arr=[]
	for i in range(n):
		b,l=[int(x) for x in input().strip().split()]
		arr.append((b,l))
	arr=sorted(arr, key=lambda x: x[1])
	band={}
	for i in range(n):
		band[arr[i][0]]=0 #use as hashmap
	k=0
	uniqueval=0
	repeatedval=0
	for i in range(n):
		if(band[arr[i][0]]==0):
			k+=1 #first time listening to this band
			band[arr[i][0]]=1
			uniqueval+=arr[i][1]*k
		else:
			#repeated bands, k unchanged
			repeatedval+=arr[i][1]
		#print(">>>",uniqueval,",",repeatedval,",",k)
	print(uniqueval+(repeatedval*k))

