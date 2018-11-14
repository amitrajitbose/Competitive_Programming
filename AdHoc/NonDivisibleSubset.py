'''
Problem Type: Implementation
Problem Link: https://www.hackerrank.com/challenges/non-divisible-subset/problem
'''
n,k=[int(x) for x in input().strip().split()]
arr=[int(x) for x in input().strip().split()]
d={}
for i in range(n):
	x=arr[i]%k
	if x in d:
		d[x].append(arr[i])
	else:
		d[x]=[arr[i]]
# so the dictionary is ready now

# now check for all ways of forming k by two digits
maxlen=0
#print(d)
if(0 in d):
	maxlen=1
for i in range(1,(k//2)+1):
	comp=k-i
	if(i!=comp):
		if(i in d and comp in d):
			maxlen+=max(len(d[i]),len(d[comp]))
			#max because we have to maximise
			#we cannot consider both because they can sum up in themselves
			#and result in MOD = 0
		elif(i in d and comp not in d):
                maxlen+=len(d[i])
            elif(i not in d and comp in d):
                maxlen+=len(d[comp])
	else:
		#when i==comp, that is for k=4 -> 2+2; happens for even numbers only
		if(i in d and len(d[i])>0):
			maxlen+=1
			#because if i and comp are same for more than 1 value then
			#they can add up themselves and result in MOD = 0, or divisible
			#thus we can take only one

print(maxlen)

