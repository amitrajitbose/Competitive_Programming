class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of ints
	# @return an int
	def paint(self, A, B, C):
		MOD = 10000003
		if len(C) == 1:
			return (C[0] * B) % MOD
		if A == 1:
			return (sum(C) * B) % MOD # all work done by one worker
		low = min(C)
		high = sum(C)
		ans = float('inf')
		while low <= high:
			mid = (low + high)//2
			x = self.countSubs(C, mid * B, B)
			if x <= A:
				ans = min(ans, self.getMaxSub(C, mid * B, B))
				high = mid - 1
			else:
				low = mid + 1
		return ans % MOD
	
	def countSubs(self, A, maxsum, B):
		"""utility function to count number of
		subarrays such that none of them sum upto
		more than maxsum value """
		count  = 0
		i = 0
		wsum = 0
		while i < len(A):
			wsum += (A[i] * B)
			if wsum > maxsum:
				count += 1
				wsum = A[i] * B
			i += 1
		return count if wsum==0 else count + 1
	
	def getMaxSub(self, A, maxsum, B):
		"""returns the maximum sum of all possible subarrays such that
		maximum sum of any subarray does not maxsum"""
		i = 0
		wsum = 0
		maxwsum = -1
		while i < len(A):
			wsum += (A[i] * B)
			if wsum > maxsum:
				maxwsum = max(maxwsum, wsum-(A[i]*B))
				wsum = A[i]*B
			i += 1
		return max(maxwsum, wsum)
	
