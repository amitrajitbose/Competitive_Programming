'''
Given an array, find the total number of contiguous
subarrays that sum up to k.
'''
class Solution:
    def subarraySum(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cumulative_sum = 0
        counter = 0
        previously_seen = dict()
        for i in range(len(arr)):
            cumulative_sum += arr[i]
            if(cumulative_sum == k):
                counter += 1
            if(cumulative_sum-k in previously_seen):
                counter += previously_seen[cumulative_sum-k]
            if(cumulative_sum in previously_seen):
                previously_seen[cumulative_sum] += 1
            else:
                previously_seen[cumulative_sum] = 1
        return counter