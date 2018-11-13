#author: amitrajitbose
MOD=(10**9)+7
table=[[1 for i in range(1001)] for j in range(1001)]
for i in range(1,1001):
	for j in range(1,1001):
		table[i][j]=(table[i][j-1]+table[i-1][j])%MOD

t=int(input())
for _ in range(t):
	n=int(input())
	arr=[int(x) for x in input().strip().split()]
	sarr=set(arr)
	if(len(sarr)==n):
		print((2**(n-1))%MOD)
	else:
		arr=sorted(arr,reverse=False)
		ga,gb=0,0
		while(gb<n):
			tmp=gb #sequence start
			mark=tmp+1 #sequence end
			while(mark<n):
				if(arr[mark]==arr[tmp]):
					mark+=1 #increasing marker sequence
				else:
					break
			gb=mark
			for i in range(tmp,mark):
				for j in range(i,mark):
					low,right=i,(n-j-1)
					val=0
					#if(low<1001 and right<1001):
					val=(table[low][right])%MOD
					ga=(ga+val)%MOD
		print(ga%MOD)
