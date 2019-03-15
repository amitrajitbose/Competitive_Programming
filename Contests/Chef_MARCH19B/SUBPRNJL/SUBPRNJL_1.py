	from math import ceil as CEIL
	for _ in range(int(input())):
		cnt = 0
		n, k = [int(x) for x in input().strip().split()]
		arr = [int(x) for x in input().strip().split()]
		for i in range(n):
			for j in range(i,n):
				m = CEIL(k/((j-i)+1))
				subseq = arr[i:j+1]
				subseq = sorted(subseq)
				X = subseq[CEIL(k/m)-1]
				F = subseq.count(X)
				if(F in subseq == True):
					cnt+=1
		print(cnt)