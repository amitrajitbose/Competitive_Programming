"""
Given an array of positive and negative elements, return the maximum
sum of a contiguous subarray
"""

def max_sum(arr):
    max_so_far = 0
    max_ending_here = 0
    for i in arr:
        max_ending_here += i
        if max_ending_here < 0:
            max_ending_here = 0
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    return max_so_far

print(max_sum([-2,-3,4,-1,-2,1,5,-3]))