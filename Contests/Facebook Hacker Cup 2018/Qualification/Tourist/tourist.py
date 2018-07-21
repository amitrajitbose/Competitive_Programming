'''
Author: Amitrajit Bose
Problem: Facebook HackerCup Qualification Round
'''
with open("Output.txt", "w") as text_file:

	testcase=int(input())
	for _ in range(testcase):
		#entire program will be contained here now
		n,k,v=[int(x) for x in input().strip().split()]
		citynames=[]
		#citydict={}
		out=[]
		for i in range(n):
			x=str(input().strip())
			citynames.append(x)
			#citydict[x]=0
		tot=k*(v-1)
		d1=tot//n
		d2=tot%n
		cnt=0
		for i in range(n):
			#citydict[citynames[i]]+=d1
			if(i<d2):
				#citydict[citynames[i]]+=1
				cnt+=1
		
		#cnt = number of cities that are more visited
		morevisited=cnt
		lessvisited=n-cnt
		#print(citydict)
		#print("k=",k)
		#print("lessvisited=",lessvisited)
		if(k<=lessvisited):
			for i in range(n-lessvisited,n-lessvisited+k):
				out.append(citynames[i])
		else:
			moretovisit=k-lessvisited
			for i in range(moretovisit):
				out.append(citynames[i])
			for i in range(n-lessvisited,n):
				out.append(citynames[i])
		print("Case #{0}: ".format(str(_+1)),end="",file=text_file)
		print(*out,file=text_file)


		