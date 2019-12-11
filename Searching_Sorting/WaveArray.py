# https://www.interviewbit.com/problems/wave-array/
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def wave(self, A):
	    A.sort()
	    B = []
	    n = len(A)
	    for i in range(1,n,2):
	        B.append(A[i])
	        B.append(A[i-1])
	    if n%2:
	        B.append(A[-1])
	    return B
