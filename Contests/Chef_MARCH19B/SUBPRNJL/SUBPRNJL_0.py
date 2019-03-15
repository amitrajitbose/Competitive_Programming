def one_hot_encode(arr):
	one_hot = [0]*2001 #because maximum can be 2000
	for i in arr:
		one_hot[i] += 1
	return one_hot

from math import ceil
tc = int(input())
for tc_ in range(int(tc)):
	counter = 0
	n, k = map(int, input().strip().split())
	arr = list(map(int, input().strip().split()))

	for i in range(n):
		for j in range(i,n):
			m = ceil(k/((j-i)+1))
			S = arr[i:j+1]
			freq = one_hot_encode(S)
			freq_copy = freq[:]
			for index in range(2001):
				freq[index] = freq[index] * m
			lsum = 0
			for val in range(2001):
				if(lsum < k):
					lsum = lsum + freq[val]
				else:
					X = val-1
					break

			F = freq_copy[X] #S.count(X)
			if(freq_copy[F]>=1):
				counter+=1
	print(counter)
