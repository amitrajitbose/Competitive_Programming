# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
# https://leetcode.com/problems/squares-of-a-sorted-array/

# Two Pointer Solution
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]: # TIme Complexity = O(n) Space Complexity = O(n) 
        l = len(A)
        ans = [None]*l
        i = 0
        j = l-1
        for k in range(l-1,-1,-1):
            if abs(A[i]) > abs(A[j]):
                ans[k]=A[i]**2
                i+=1
            else:
                ans[k]=A[j]**2
                j-=1
        return ans
        
        
