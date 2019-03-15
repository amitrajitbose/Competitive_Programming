tc = int(input())
for tcs in range(tc):
	n = int(input())
	inputs = []
	for i in range(n):
		tmp = str(input().strip())
		inputs.append(list(set(list(tmp))))
	cnt=0
	for i in range(n-1):
		for j in range(i+1,n):
			a = inputs[i]
			b = inputs[j]
			thislist = a+b
			if(len(set(thislist[:]))==5):
				cnt += 1
	print(cnt)
