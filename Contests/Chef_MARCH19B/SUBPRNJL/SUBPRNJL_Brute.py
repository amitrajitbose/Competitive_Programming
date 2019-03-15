from math import ceil
tc = int(input())
for tc_ in range(int(tc)):
	counter = 0
	n, k = map(int, input().strip().split())
	arr = list(map(int, input().strip().split()))
	arr = sorted(arr)
	for i in range(n):
		for j in range(i,n):
			m = ceil(k/((j-i)+1))
			S = arr[i:j+1]
			print(S)
			B = S * m
			print(B)
			Bsorted = sorted(B)
			print(Bsorted)
			X = Bsorted[k-1]
			print(X)
			F = S.count(X)
			print(F)
			print(S.count(F))
			if(S.count(F)>=1):
				counter+=1
			print("-----------------------------")
	print(counter)