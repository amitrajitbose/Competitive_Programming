'''
DCP #18
This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
'''
# Help : https://www.youtube.com/watch?v=ShbRCjvB_yQ
# Reference: https://www.youtube.com/watch?v=J6o_Wz-UGvc

from collections import deque as Queue

def slider(arr,k):
	n=len(arr)
	q=Queue()

	#from the first k elements keep the max and decreasing
	for i in range(k):
		while(len(q) and arr[i]>=arr[q[-1]]):
			q.pop()
		q.append(i)
	for i in range(k,n):
		#previous window max
		print(arr[q[0]],end=" ")
		#if any element does not belong to this window we pop the,
		while(len(q) and q[0]<=i-k):
			#this index does not belong to this window
			q.popleft()
		#remove all smaller elements
		curr=arr[i]
		while(len(q) and curr>=arr[q[-1]]):
			q.pop()
		q.append(i)
	print(arr[q[0]])

slider([10, 5, 2, 7, 8, 7],3)
slider([2, 10, 5, 7, 7, 8],3)