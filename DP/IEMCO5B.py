#https://www.codechef.com/IEMCO5/problems/IEMCO5B/

def maxSum(arr, n):
	max = 0
	msisi = [0 for x in range(n)]
	for i in range(n):
		msisi[i] = arr[i]
	for i in range(1, n):
		for j in range(i):
			if arr[i] > arr[j] and msisi[i] < msisi[j] + arr[i]:
				msisi[i] = msisi[j] + arr[i]
	for i in range(n):
		if max < msisi[i]:
			max = msisi[i]
 
	return max
 
t=int(input())
for _ in range(t):
    n=int(input())
    arr=[int(x) for x in input().strip().split(' ')]
    print(str(maxSum(arr, n))) 