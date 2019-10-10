class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        s, l, g = 0, 0, 0
        for i in range(n-1):
            l=max(l, i+nums[i]) 
            if i==g:
                s+=1
                g=l
        return s

