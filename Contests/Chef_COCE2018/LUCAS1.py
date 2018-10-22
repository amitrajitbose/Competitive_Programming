t=int(input())
for _ in range(t):
	freq=[0 for x in range(26)]
	s=list(str(input()))
	for ch in s:
		freq[ord(ch)-97]+=1
	freq=filter(lambda a: a != 0, freq)
	freq=sorted(freq)

	flag=True
	if(freq[0]==1 and freq[1]==2 and len(freq)>2):
		freq[0]=2
		freq[1]=1
		for i in range(2,len(freq)):
			if(freq[i] != (freq[i-1]+freq[i-2])):
				flag=False
		if(flag==True):
			print("FIT")
		else:
			print("UNFIT")
	elif(freq[0]==1 and freq[1]==2 and len(freq)==2) or (len(freq)==1 and freq[0]==2):
		print("FIT")
	else:
		print("UNFIT")

	



