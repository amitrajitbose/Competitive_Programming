# https://leetcode.com/problems/largest-number-at-least-twice-of-others/
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxidx = nums.index(max(nums))
        maxval = nums[maxidx]
        flag = True
        for i in nums:
            if i != maxval and i != 0:
                if (maxval // i) < 2:
                    return -1
        return(maxidx)

