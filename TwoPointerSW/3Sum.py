class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        # print(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            j, k = i+1, n-1
            while j < k:
                # print(i,j,k)
                triplet = nums[i] + nums[j] + nums[k]
                if triplet > 0:
                    k -= 1
                elif triplet < 0:
                    j += 1
                else:
                    # print("Got")
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
        return res
