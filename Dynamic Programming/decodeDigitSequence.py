'''
DCP #7
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''
def decodings(msg):
	msg1=list(str(msg))
	msg=[]
	for i in msg1:
		msg.append(int(i))
	n=len(msg)
	dp=[0 for x in range(n+1)] #bottom up table
	dp[0]=1
	dp[1]=1 #whatever number it is will always be one
	for i in range(1,n):
		if(msg[i]>=0):
			#if current digits is >= 0, then curr-1 counts will get added
			dp[i+1]=dp[i]
		lasttwo=(msg[i-1]*10)+msg[i]
		if(lasttwo<27):
			dp[i+1] += dp[i-1]
	return dp[n]

assert decodings(111)==3
assert decodings(121)==3
assert decodings(1234)==3
assert decodings(918)==2
