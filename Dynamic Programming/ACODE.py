#Problem Link: http://www.spoj.com/problems/ACODE/

from itertools import repeat
while(True):
	a=str(input())
	arr=list(map(lambda x:x,a))
	n=len(arr)
	#thus the word has been broken to characters
	dp=list(repeat(0,n+1))
	#bottom up dynamic approach
	#traverse the string/number from last to first
	if(n==1 and a=='0'):
		break
	elif(n==1):
		print(1)
	else:
		dp[n]=1
		if(arr[n-1]!='0'):
			dp[n-1]=1
		else:
			dp[n-1]=0

		for i in range(n-2,-1,-1):
			if(arr[i]=='0'):
				dp[i]=0
			elif(arr[i]=='1'):
				dp[i]=dp[i+1]+dp[i+2]
			elif(arr[i]=='2'):
				if(int(arr[i+1])>6):
					dp[i]=dp[i+1]
				else:
					dp[i]=dp[i+1]+dp[i+2]
			elif(int(arr[i])>2):
				dp[i]=dp[i+1]
		print(dp[0])
