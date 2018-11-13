# Author: @amitrajitbose
# Inspiration & Support : Pratik <3

from collections import deque as deq

def makeString(arr):
	a=''.join(arr)
	return a

def findSequences(s):
	l=list(len(x) for x in s.split('0'))
	return l

def adjust(x,k):
	#adjust in terms of limit k
	if(x>=k):
		return k
	else:
		return x

def main():
	n,q,k=[int(x) for x in input().strip().split()]
	arr=[str(x) for x in input().strip().split()]
	queryString=list(str(input()))
	arrString=makeString(arr)
	seq=findSequences(arrString)
	seq1=seq[:]
	seq1.sort(reverse=True) #descending
	seq2=seq[:]

	max1,max2=seq1[0],seq1[0] #storing first and second maximum sequences' lengths
	if(len(seq)>1):
		max2=seq1[1] #storing second max if it is distinct
	seq2=seq2[::-1]
	table={} #used for caching
	state=0
	ind1=len(seq2)-seq2.index(max1)-1 #index of first occurance of max1 in seq2 which is in non-increasing order

	items=deq(arr) #queue
	itemLens=deq(seq) #queue
	l=len(itemLens)
	table[0]=adjust(max1,k)

	maxUpdates=min(n,queryString.count('!'))
	while(maxUpdates>0):
		maxUpdates-=1
		state=state+1
		items.rotate()
		if(items[0]=='1'):
			itemLens[0]+=1
			itemLens[l-1]-=1
			if(ind1==l-1):
				max1-=1
		if(itemLens[l-1]==0):
			itemLens.rotate()
			ind1+=1
			ind1=ind1%l
			if(ind1==0):
				ind1=1
			max1=itemLens[ind1]
		if(not state%n in table):
			if(n<=1000):
				table[state%n]=adjust(max(itemLens),k)
			else:
				table[state%n]=adjust(max(max1,max2,itemLens[0]),k)

	#answer queries
	state=0
	for quer in queryString:
		if quer=='!':
			state=(state+1)%n
		elif quer=='?':
			print(adjust(table[state],k))

if __name__ == '__main__':
	main()
