# https://leetcode.com/problems/maximum-swap
class Solution:
    """
    @param num: a non-negative intege
    @return: the maximum valued number
    """
    def maximumSwap(self, num: int) -> int:
        # Write your code here
        num = str(num)
        n = len(num)
        k = n-1
        max_val = int(num)
        max_digit = 0
        max_index = 0
        while(k>=0):
            if int(num[k])>max_digit:
                max_digit = int(num[k])
                max_index = k
            else:
                temp = list(num)
                temp[max_index], temp[k] = temp[k], temp[max_index]
                temp = ''.join(temp)
                max_val = max(int(max_val), int(temp))
            k -= 1
        return int(max_val)

