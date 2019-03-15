from math import ceil

def binary_search(arr, key):
	return (key in arr)

for _ in range(int(input())):
	count = 0
	n,k = map(int, input().strip().split())
	arr = [int(x) for x in input().strip().split()]
	frequency_vector = [0]*2001
	for i in arr:
		frequency_vector[i] += 1
	pref_sum_fv = [0]*2001
	pref_sum_fv[0] = frequency_vector[0]
	for i in range(1,2001):
		pref_sum_fv[i] = pref_sum_fv[i-1]+frequency_vector[i]
	for i in range(n):
		for j in range(i,n):
			m = ceil(k/((j-i)+1))
			subseq = pref_sum_fv[i:j+1]
			X = pref_sum_fv.index(k)
			F = frequency_vector[X]
			if(F in sub):
				count+=1
	print(count)