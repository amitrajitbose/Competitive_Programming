# Author: @amitrajitbose
from collections import deque as deq
from math import ceil
def seqcount(arr):
	#greedy counter -- O(n)
	start,end=-1,-1
	tmp=-1
	st2,en2=-1,-1
	l=len(arr)
	gsum,lsum=0,0
	for i in range(l):
		if(arr[i]==1):
			lsum+=1 #local update
		elif(arr[i]==0):
			if(lsum>gsum):
				gsum=lsum
				end=i-1
			if(lsum==gsum):
				tmp=gsum
				en2=i-1
			lsum=0
	if(lsum>gsum):
		end=l-1
		gsum=lsum
	if(lsum==gsum):
		en2=l-1
		tmp=gsum
	start=(end-gsum)+1
	if(gsum>tmp):
		st2,en2=0,0 #reset, cause only one sequence
	elif(gsum==tmp):
		st2=(en2-tmp)+1
	return (start, end, st2, en2)

def adjust(x,k):
	#adjust in terms of limit k
	if(x>=k):
		return k
	else:
		return x

def main():
	n,q,k=[int(x) for x in input().strip().split()]
	oriarr=[int(x) for x in input().strip().split()]
	items=deq(oriarr)
	queryString=list(input())
	state=0 #there can be upto n-1 states including 0
	table={} #look-up table // python dictionary
	maxUpdates=min(n,queryString.count('!'))
	sp,ep,sp2,ep2=seqcount(oriarr) #start and end pointers
	#cleaning the array for second max
	temparr=oriarr[:]
	pointer=sp
	turns=ep-sp+1
	while(turns>0):
		turns-=1
		temparr.pop(pointer)
	#cleaning done
	temp1,temp2,temp3,temp4=seqcount(temparr)
	sp2,ep2=temp1,temp2
	#adjusting sp2,ep2
	if(sp2>=sp):
		sp2=sp2+(ep-sp+1)
		ep2=ep2+(ep-sp+1)
	#print(sp,ep,sp2,ep2)
	table[0]=ep-sp+1
	#preparing the lookup table
	if(oriarr.count(1)==0):
		for i in range(n):
			table[i]=0
	elif(oriarr.count(1)==n):
		for i in range(n):
			table[i]=n
	else:
		while(maxUpdates>0):
			maxUpdates-=1
			state+=1
			items.rotate(1)
			arr=list(items)
			sp=(sp+1)%n
			sp2=(sp2+1)%n
			ep=(ep+1)%n
			ep2=(ep2+1)%n
			if(sp<=ep and ep<n and arr[sp-1]==0):
				#print("YO1")
				#print(sp,ep,"HERE")
				#just shifting of sequence
				table[state]=ep-sp+1
				#now check if there is a larger sequence in front
				fleng=0
				for y in range(0,table[state]):
					if(arr[y]==0):
						break
					else:
						fleng+=1
				if(fleng>=table[state]):
					sp=0
					ep=fleng-1
			elif(sp<=ep and ep<n and arr[sp-1]==1):
				#print("YO2")
				#new element gets added in front
				table[state]=table[state-1]+1 
				sp=(sp-1)%n
			elif(ep<sp):
				#sequence broken
				if(ep==0):
					#print("YO3")
					#print(sp,ep,"HERE")
					if(arr[ep+1]==1):
						#chance that sequence may elongate
						for y in range(ep+1,sp):
							if(arr[y]==0):
								break
							else:
								ep+=1
						oldlength=(n-1)-sp+1
						newlength=ep+1
						if(oldlength>newlength):
							table[state]=table[state-1]-1
						else:
							table[state]=newlength
							sp=0
					else:
						table[state]=table[state-1]-1
						curr=table[state]
						tmp1,tmp2=sp2,ep2
						curr2=tmp2-tmp1+1
						if(curr2>curr):
							sp,ep=tmp1,tmp2
							table[state]=curr2
				elif(sp==ceil(n/2)+1):
					#print(sp,ep,"HERE")
					#half point is reached
					if(ep+1 >= n-sp):
						#print("YO4")
						sp=0
						table[state]=ep-sp+1
					else:
						table[state]=table[state-1]-1
				else:
					#print("YO5")
					table[state]=max(table[state-1]-1,ep+1)
					curr=table[state]
					tmp1,tmp2=sp2,ep2
					curr2=tmp2-tmp1+1
					if(curr2>curr):
						sp,ep=tmp1,tmp2
						table[state]=curr2
	
	state=0
	for quer in queryString:
		if quer=='!':
			state=(state+1)%n
		elif quer=='?':
			print(adjust(table[state],k))

if __name__ == '__main__':
	main()
	'''
	t=int(input())
	for _ in range(t):
			print("TC-# ",_+1)
			main()
	'''