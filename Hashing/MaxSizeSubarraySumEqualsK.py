"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Array  1 -1 5 -2 3
Array  -2 -1  2 1
"""

from collections import defaultdict as d
def maxLen(n, arr, p=0):
    """
    15 -2 2 -8 1 7 10 23
    15 13 15 7 8 15 25 48
    
    max  =  5
    
    hashmap
    key   value
    0      -1
    15      0
    13      1
    7       3
    8       4
    25      6
    48      7
    """
    first_occurance_idx = d(int)
    cumulative_sum = 0
    k = -1
    maxlen = 0
    first_occurance_idx[cumulative_sum] = k 
	#initialising the dictionary with the value / dummy
    while (k < n-1):
        k += 1
        cumulative_sum += arr[k]
        if cumulative_sum not in first_occurance_idx:
            first_occurance_idx[cumulative_sum] = k
        elif cumulative_sum-p in first_occurance_idx:
            maxlen = max(maxlen, k-first_occurance_idx[cumulative_sum-p])
    return maxlen 
