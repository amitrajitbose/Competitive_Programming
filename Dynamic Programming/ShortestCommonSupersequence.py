'''
Given two strings str1 and str2, find the length of the smallest string which has both, str1 and str2 as its sub-sequences.

Input:
The first line of input contains an integer T denoting the number of test cases.Each test case contains two space separated strings.

Output:
Output the length of the required string.

Company : Microsoft
'''
def memoized_lcs(memo,a,b,i,j):
	if(i==-1 or j==-1):
		return 0
	if(memo[i][j]!=-1):
		return memo[i][j]
	if(a[i]==b[j]):
		memo[i][j]=memoized_lcs(memo,a,b,i-1,j-1)+1
		return memo[i][j]
	else:
		memo[i][j]=max(memoized_lcs(memo,a,b,i-1,j),memoized_lcs(memo,a,b,i,j-1))
		return memo[i][j]

def scs(a,b):
	'''shortest common subsequence'''
	'''=sum of len of two strings - len of lcs'''
	memo=[[-1 for x in range(len(b))] for x in range(len(a))]
	lcs_length=memoized_lcs(memo,a,b,len(a)-1,len(b)-1)
	return(len(a)+len(b)-lcs_length)

for _ in range(int(input())):
	s1,s2=[str(x) for x in input().strip().split()]
	print(scs(s1,s2))