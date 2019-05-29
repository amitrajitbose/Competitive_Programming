# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        l = 0
        r = n - 1
        #ans = min(height[l], height[r]) * (r-l)
        while(l != r):
            if(height[l] < height[r]):
                ans = max(ans, height[l] * (r-l))
                l += 1
            else:
                ans = max(ans, height[r] * (r-l))
                r -= 1
            #ans = max(ans, min(height[l], height[r]) * (r-l))
        return ans

    '''
    [1,8,6,2,5,4,8,3,7]
    [1,3,7,3,8,2,1,6,8,9,7,3,2,6,8,2,1,5,6,8,9,0,3,2,5]
    [1,2,4,3]
    '''
