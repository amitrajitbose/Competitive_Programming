class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positive_nums = []
        for i in range(len(nums)):
            if nums[i] > 0:
                positive_nums.append(nums[i])
        for i in range(len(positive_nums)):
            num = abs(positive_nums[i])
            if num <= len(positive_nums):            
                positive_nums[num-1] = -1 * abs(positive_nums[num-1])
        smallest = 1
        while smallest <= len(positive_nums):
            if positive_nums[smallest-1] > 0:
                return smallest
            smallest += 1
        return smallest
        
