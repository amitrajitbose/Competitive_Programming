# Author: Amitrajit Bose
# MockVita Problem 2 - Digital Time

'''
The objective is to form the maximum possible time in 
the HH:MM:SS format using any six of nine given single 
digits (not necessarily distinct)

Given a set of nine single (not necessarily distinct) digits, 
ay 0, 0, 1, 3, 4, 6, 7, 8, 9, it is possible to form many 
distinct times in a 24 hour time format HH:MM:SS, such 
as 17:36:40 or 10:30:41 by using each of the digits only 
once. The objective is to find the maximum possible valid 
time (00:00:01 to 24:00:00) that can be formed using some 
six of the nine digits exactly once. In this case, 
it is 19:48:37.

'''
testcase=1
for _ in range(testcase):
	#initialising freqlist
	freqlist=[0,0,0,0,0,0,0,0,0,0]
	#freqlist represent the count of the element at the position in freqlist

	digits=[int(x) for x in input().strip().split(',')]
	maximizedTime=""

	for d in digits:
		freqlist[d]+=1
	#freqlist is ready

	flag=0

	for i in range(2,-1,-1):
		if(freqlist[i]>0):
			maximizedTime+=str(i)
			freqlist[i]-=1
			flag=1
			break
	#if there is no 0,1,2
	if(flag==0):
		print("Impossible")
		continue

	#second digit of hour
	flag=0
	if(freqlist[0]>=4 and freqlist[4]>0):
		print("24:00:00")
		continue

	elif(maximizedTime[0]=='2'):
		#if hour>=20
		for i in range(3,-1,-1):
			if(freqlist[i]>0):
				maximizedTime+=str(i)
				freqlist[i]-=1
				flag=1
				break
		#if there is no 0,1,2,3
		if(flag==0):
			print("Impossible")
			continue

	else:
		for i in range(9,-1,-1):
			if(freqlist[i]>0):
				maximizedTime+=str(i)
				freqlist[i]-=1
				flag=1
				break
		#if there is no 0,1,2,3,4,5,6,7,8,9
		if(flag==0):
			print("Impossible")
			continue

	'''if(maximizedTime[:]=="24" and freqlist[0]==4):
					print("24:00:00")
					continue'''

	maximizedTime+=":"
	#now minute
	flag=0
	for i in range(5,-1,-1):
		if(freqlist[i]>0):
			maximizedTime+=str(i)
			freqlist[i]-=1
			flag=1
			break
	#if there is no 0,1,2,3,4,5
	if(flag==0):
		print("Impossible")
		continue

	flag=0
	for i in range(9,-1,-1):
		if(freqlist[i]>0):
			maximizedTime+=str(i)
			freqlist[i]-=1
			flag=1
			break
	#if there is no 0,1,2,3,4,5,6,7,8,9
	if(flag==0):
		print("Impossible")
		continue

	maximizedTime+=":"
	#now seconds
	flag=0
	for i in range(5,-1,-1):
		if(freqlist[i]>0):
			maximizedTime+=str(i)
			freqlist[i]-=1
			flag=1
			break
	#if there is no 0,1,2,3,4,5
	if(flag==0):
		print("Impossible")
		continue

	flag=0
	for i in range(9,-1,-1):
		if(freqlist[i]>0):
			maximizedTime+=str(i)
			freqlist[i]-=1
			flag=1
			break
	#if there is no 0,1,2,3,4,5,6,7,8,9
	if(flag==0):
		print("Impossible")
		continue

	print(maximizedTime)
