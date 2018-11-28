# Classical Longest Common Subsequence Problem

a="ACBDHEIHTKNASJHRJKBJWJEVOEWNV"
b="ABCDEKBSKDBUEWBUEUKHSJKHKUELWNV"

#a="AGGTAB"
#b="GXTXAYB"

#RECURSIVE APPROACH
def lcs(a,b,i=len(a)-1,j=len(b)-1):
	if(i==-1 or j==-1):
		return ""
	if(a[i]==b[j]):
		return lcs(a,b,i-1,j-1)+a[i]
	else:
		return max(lcs(a,b,i-1,j),lcs(a,b,i,j-1))



#MEMOIZATION APPROACH
global memo
memo=[[-1 for x in range(len(b))] for x in range(len(a))]
def memoized_lcs(a,b,i=len(a)-1,j=len(b)-1):
	if(i==-1 or j==-1):
		return ""
	if(memo[i][j]!=-1):
		return memo[i][j]
	if(a[i]==b[j]):
		memo[i][j]=memoized_lcs(a,b,i-1,j-1)+a[i]
		return memo[i][j]
	else:
		memo[i][j]=max(memoized_lcs(a,b,i-1,j),memoized_lcs(a,b,i,j-1))
		return memo[i][j]

#print(lcs(a,b)) #THIS MAY HANG YOUR SYSTEM xD
print(memoized_lcs(a,b)) #OUT: ACDEKSKBWJEWNV
