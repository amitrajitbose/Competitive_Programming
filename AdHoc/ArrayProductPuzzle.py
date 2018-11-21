'''
DCP #2
This problem was asked by Uber, DE Shaw, Accolite, etc.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the 
numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

'''
Approach 1 : Double Ended Prefix Product - O(3n) - solver1()
Approach 2 : Logarithmic Sum - O(2n) - solver2()
'''

from math import log,expm1,floor
def solver1(arr):
	left=[arr[0]] #will store the left prefix sum
	right=[arr[-1]] #will store the right prefix sum
	n=len(arr) #just the length of array
	for i in range(1,n):
		left.append(left[-1]*arr[i])
	for i in range(n-2,-1,-1):
		right.append(right[-1]*arr[i])
	right.reverse()
	final=[right[1]]
	for i in range(1,n-1):
		final.append(left[i-1]*right[i+1])
	final.append(left[-2])
	return final

def solver2(arr):
	logsum=0
	for i in arr:
		logsum+=log(i)
	final=[]
	for i in arr:
		final.append(round(expm1(logsum-log(i))+1))
	return final

# TEST CASES

print(solver1([2,3,4]))
print(solver2([2,3,4]))

print(solver1([1,2,3,4,5]))
print(solver2([1,2,3,4,5]))

print(solver1([2,3,4,5,6]))
print(solver2([2,3,4,5,6]))

print(solver1([10,100,1000,10000]))
print(solver2([10,100,1000,10000]))
