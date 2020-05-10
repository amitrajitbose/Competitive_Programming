class Solution:
	# @param A : list of integers
	# @return an integer
	def findMinXor(self, A):
	    A.sort()
	    minxor = 2**32
	    for i in range(1,len(A)):
	        minxor = min(A[i]^A[i-1], minxor)
	    return minxor
