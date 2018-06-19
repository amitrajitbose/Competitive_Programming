'''
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.

Source: Edit Distance | GFG
Explanation: https://youtu.be/Thv3TfsZVpw
'''
#import pprint #pretty printer to print the table in line 27
def editDistance(str1,str2):
	m=len(str1)
	n=len(str2)
	table=[[0 for x in range(n+1)] for x in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if(i==0):
				table[i][j]=j
			elif(j==0):
				table[i][j]=i
			elif(str1[i-1]==str2[j-1]):
				table[i][j]=table[i-1][j-1] #diagonal value + 1, i.e replacing
			else:
				table[i][j]=1+min(table[i-1][j-1],table[i-1][j],table[i][j-1]) #replace,remove,insert
	#pprint.pprint(table)
	return table[m][n]

str1=str(input().strip())
str2=str(input().strip())
print(editDistance(str1,str2),"OPERATIONS REQUIRED")