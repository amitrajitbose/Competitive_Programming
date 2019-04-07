MOD = (10**9) + 7

def subtractArrays(a,b):
	'''
	return array a - array b;
	assumes array a >= array b
	lengths should be same to subtract
	'''
	if(len(a)!=len(b)):
		return -1
	else:
		c=[]
		for i in range(len(a)):
			c.append(a[i]-b[i])
		return c

def findCount(l,r,a):
	if(l>r):
		return -1
	if(l==1 and r==1):
		return globalmap[0]
	elif(l>1):
		return subtractArrays(a[r-1],a[l-2])
	elif(l==1):
		empty=[0 for i in range(26)]
		return subtractArrays(a[r-1],empty)

def maxPalin(l,r):
	count = findCount(l,r,globalmap)
	start=''
	mid=''
	end=''
	for i in range(26):
		if(count[i] & 1):
			mid=chr(97+i)
			count[i]-=1
			i-=1
		else:
			for j in range(count[i]//2):
				start = start + chr(97+i)
	end = start[::-1]
	return start+mid+end

def countMaxPalins(l,r):
	longest_palindrome = maxPalin(l,r)
	oricount = findCount(l,r,globalmap)
	palcount = [0 for x in range(26)]
	
	for i in range(len(longest_palindrome)):
			palcount[ord(longest_palindrome[i])-97]+=1

	if(len(longest_palindrome)%2):
		#odd length
		replaceable = subtractArrays(oricount, palcount)
		#print(longest_palindrome) #DEBUG
		return sum(replaceable)+1
	else:
		#even length
		#print(palcount)
		return 26-palcount.count(0)

globalmap = []
s=str(input())
s=s.lower()

#adding first character to map
row = [0 for i in range(26)]
a=ord(s[0])-97
row[a]=1
globalmap.append(row)

#fill up the global map
for i in range(1,len(s)):
	a=ord(s[i])-97
	new_row = globalmap[-1][:] #copy of previous
	new_row[a]+=1
	globalmap.append(new_row)
for _ in range(int(input())):
	l,r=[int(x) for x in input().strip().split()]
	print(countMaxPalins(l,r)%MOD)


# print(findCount(l,r,globalmap))