# https://www.interviewbit.com/problems/min-sum-path-in-matrix/
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def minPathSum(self, A):
	    for i in range(1, len(A[0])):
	        A[0][i] += A[0][i-1]
	    for i in range(1, len(A)):
	        A[i][0] += A[i-1][0]
	    for i in range(1, len(A)):
	        for j in range(1, len(A[0])):
	            A[i][j] += min(A[i-1][j], A[i][j-1])
	    return A[-1][-1]
