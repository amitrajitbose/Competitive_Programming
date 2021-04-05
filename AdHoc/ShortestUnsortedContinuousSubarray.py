class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        else:
            minm, maxm, flag = float('inf'), -float('inf'), False
            for i in range(1,n):
                if nums[i] < nums[i-1]:
                    flag = True
                if flag:
                    minm = min(minm, nums[i])
            flag = False
            for i in range(n-2,-1,-1):
                if nums[i] > nums[i+1]:
                    flag = True
                if flag:
                    maxm = max(maxm, nums[i])
            for l in range(n):
                if minm < nums[l]:
                    break
            for r in range(n-1,-1,-1):
                if maxm > nums[r]:
                    break
            return 0 if r-l <= 0 else r-l+1
            

"""
[2,3,3,2,4]
[2,6,4,8,10,9,15]
[2,1]
[2,1,3]
[3,2,1]
"""
