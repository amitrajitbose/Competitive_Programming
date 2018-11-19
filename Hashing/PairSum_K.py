'''
DCP #1
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

def findpair(arr,k):
	visited=dict()
	for i in arr:
		if(i not in visited):
			visited[i]=1
		else:
			visited[i]+=1
		j=k-i
		if(j in visited):
			if(i==j and visited[j]>=2):
				return True
			elif(i==j and visited[j]>2):
				continue
			elif(i!=j):
				return True
	return False

print(findpair([10,15,3,7],17))
print(findpair([11,4,0,3],3))
print(findpair([1,2,3,4],8))
print(findpair([4,2,3,4],8))
print(findpair([11,4,0,3],13))