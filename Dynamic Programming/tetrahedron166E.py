'''
Problem Link: https://codeforces.com/contest/166/problem/E
Approach: DP
'''
#import timeit

MOD = (10**9)+7
global dp

#TOP DOWN METHOD
#FAILED DUE TO RECURSION LIMIT

def trace(home,steps,dp):
	if(dp[home][steps]!=0):
		return dp[home][steps]
	if(steps==0):
		if(home==1):
			return 1 #possible cycle
		else:
			return 0 #cannot reach home, not possible
	else:
		if(home==1):
			dp[1][steps]=(3*trace(0,steps-1,dp))%MOD
		else:
			dp[0][steps]=((2*trace(0,steps-1,dp))+trace(1,steps-1,dp))%MOD
		return dp[home][steps]

def main():
	n=int(input())
	temp=[0 for i in range(n+1)]
	dp=[]
	dp.append(temp)
	dp.append(temp[:])
	print(trace2(1,n,dp))
	print(dp) #debug

#BOTTOM UP APPROACH
def tetra(n,home=1,away=0):
	#at n=0
	for i in range(1,n+1):
		tmphome=(3*away)%MOD #if I reach D, that means I was at A,B or C
		tmpaway=((2*away)+home)%MOD #if I reach A(suppose), then I was at B,C or D(home)
		home,away=tmphome,tmpaway
	return home

def newmain():
	n=int(input())
	#start=timeit.default_timer()
	print(tetra(n))
	#stop=timeit.default_timer()
	#print(stop-start)
if __name__ == '__main__':
	newmain()

#VERDICT : TLE
'''
This problem cannot be solved in linear time using Python 3.
We might pass through with CPP solution. But it is logically correct.
So I will retry the bottom up version using CPP.
'''