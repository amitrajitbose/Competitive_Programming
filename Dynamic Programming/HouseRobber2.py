class Solution:
    def util(self, hval):
        n = len(hval)
        if n == 0: 
            return 0
        if n == 1: 
            return hval[0] 
        if n == 2: 
            return max(hval[0], hval[1]) 

        # dp[i] represent the maximum value stolen so 
        # for after reaching house i. 
        dp = [0]*n 

        # Initialize the dp[0] and dp[1] 
        dp[0] = hval[0] 
        dp[1] = max(hval[0], hval[1]) 

        # Fill remaining positions 
        for i in range(2, n):
            dp[i] = max(hval[i]+dp[i-2], dp[i-1])

        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) > 2:
            return max(self.util(nums[1:]),self.util(nums[:-1]))
        else:
            if len(nums)==0:
                return 0
            else:
                return max(nums)
