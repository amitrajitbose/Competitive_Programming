# https://www.interviewbit.com/problems/unique-paths-in-a-grid/
class Solution:
	# @param A : list of list of integers
	# @return an integer
	def uniquePathsWithObstacles(self, A):
	    dp = [[0 for i in range(len(A[0]))] for j in range(len(A))]
	    if A[0][0] == 1 or A[-1][-1] == 1:
	        return 0
	    dp[0][0] = 1
	    for i in range(1,len(A[0])):
	        dp[0][i] = dp[0][i-1] if A[0][i] == 0 else 0
	    for i in range(1,len(A)):
	        dp[i][0] = dp[i-1][0] if A[i][0] == 0 else 0
	    for i in range(1, len(A)):
	        for j in range(1, len(A[0])):
	            if A[i][j] == 1:
	                dp[i][j] = 0
	            else:
	                dp[i][j] = dp[i-1][j] + dp[i][j-1]
	    return dp[-1][-1]
