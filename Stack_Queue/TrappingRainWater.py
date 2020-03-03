# One Iteration, Linear Space (Stack) Sol.
# IB : Rain Water Trapped
# Author : @amitrajitbose
#
#
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
	    st = []
	    i = 0
	    ans = 0
	    while i<len(A):
	        while st and A[i]>A[st[-1]]:
	            top = st.pop(-1)
	            if not st:
	                break
	            dist = i-st[-1]-1
	            bounded_height = min(A[i], A[st[-1]]) - A[top]
	            ans += (dist * bounded_height)
	        st.append(i) #push
	        i += 1
	    return ans
	    # Ref : https://leetcode.com/articles/trapping-rain-water/
