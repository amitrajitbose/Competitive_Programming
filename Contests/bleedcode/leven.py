# @amitrajitbose
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
	
	return table[m][n]

for _ in range(int(input())):

	str1, str2 = [str(x) for x in input().strip().split()]
	print(editDistance(str1,str2))