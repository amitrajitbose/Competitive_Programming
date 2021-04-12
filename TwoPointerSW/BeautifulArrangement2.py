# https://leetcode.com/problems/beautiful-arrangement-ii/
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        nums = [i+1 for i in range(n)]
        l, r, i = 1, n, 0
        res = [0] * n
        while i < k - 1:
            res[i] = l
            i += 1
            l += 1
            res[i] = r
            i += 1
            r -= 1
        while i < n:
            if k % 2:
                res[i] = l
                l += 1
            else:
                res[i] = r
                r -= 1
            i += 1
            
        return res
