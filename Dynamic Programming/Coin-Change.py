# LC 322 M
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        nums = [float('inf')] * (amount + 1)
        nums[0] = 0
        for deno in coins:
            for amt in range(amount+1):
                if deno <= amt:
                    nums[amt] = min(nums[amt], 1 + nums[amt-deno])
        return nums[amount] if nums[amount] < float('inf') else -1
