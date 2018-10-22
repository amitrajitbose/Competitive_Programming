def digitSum(n,step):
	res=0
	while(n>0):
		res+=n%10
		n=n//10
	step+=1
	if(res<=9):
		return (res,step)
	else:
		return digitSum(res,step)


t=int(input())

for _ in range(t):
	minstep=[99999999 for i in range(10)] #cache
	hitratio=[0 for i in range(10)]
	maxhit=0
	n,d=[int(x) for x in input().strip().split()]	
	if(n==1):
		print("{0} {1}".format(n,0))
		continue
	if(d>9):
		d=digitSum(d,0)[0] #minimize it to single digit
	
	steps=0
	if(n>9):
		n,steps=digitSum(n,steps)
		minstep[n]=min(minstep[n],steps)
	minstep[n]=min(minstep[n],steps)
	hitratio[n]+=1
	maxhit=max(maxhit,hitratio[n])
	
	if(n==1):
		print("{0} {1}".format(n,steps))
		continue
	iteration=1
	while(n!=1 and iteration<(10**8)):
		iteration+=1
		#print(minstep)
		n=n+d
		steps+=1
		if(n<10):
			minstep[n] = min(minstep[n],steps)
			hitratio[n]+=1
			maxhit=max(maxhit,hitratio[n])
		if(n>9):
			n,steps=digitSum(n,steps)
			minstep[n] = min(minstep[n],steps)
			hitratio[n]+=1
			maxhit=max(maxhit,hitratio[n])
		if(maxhit>100):
			break
	tempmin=10
	for i in range(2,10):
		if(minstep[i]!=99999999 and i<tempmin):
			tempmin=i
	print("{0} {1}".format(tempmin,minstep[tempmin]))
