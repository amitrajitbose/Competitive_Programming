import heapq
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def slidingMaximum(self, nums, k):
	    out=[]
        n=len(nums)
        if(n==0):
            return out
        q=[] #create the queue we need
        #initial addition to queue
        for i in range(k):
            while(len(q) and nums[i]>=nums[q[-1]]):
                q.pop(-1)
            q.append(i)
        #slide the window and add to out array
        for i in range(k,n):
            out.append(nums[q[0]]) #previous window maximum
            #check for residuals
            while(len(q) and q[0]<=i-k):
                #element does not belong to current window
                q.pop(0)
            curr=nums[i]
            while(len(q) and curr>=nums[q[-1]]):
                q.pop(-1)
            q.append(i)
        out.append(nums[q[0]])
        return out
