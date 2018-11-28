'''
DCP #9
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''
def maximumSum(arr):
	incl0=arr[0]
	excl0=0
	n=len(arr)
	for i in range(1,n):
		incl1=excl0+arr[i] #if we include this element we need to exclude previous one
		excl1=max(incl0,excl0) #if we exclude this element we consider the maximum till previous
		incl0,excl0=incl1,excl1
	return max(incl1,excl1)

assert maximumSum([2,4,6,2,5])==13
assert maximumSum([5,1,1,5])==10
assert maximumSum([3,1,1,5,1])==8
assert maximumSum([1,0,3,9,2])==10

