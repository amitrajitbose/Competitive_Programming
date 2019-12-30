class Solution:
    def dropNegatives(self, A):
        j = 0
        newlist = []
        for i in range(len(A)):
            if A[i] > 0:
                newlist.append(A[i])
        return newlist

    def firstMissingPositive(self, nums: List[int]) -> int:
        A = self.dropNegatives(nums)
        if len(A)==0:
            return 1
        if len(A)==1:
            return 1 if A[0] >= 2 else 2
        else:
            n = len(A)
            for i in range(n):
                item = abs(A[i])
                if item <= n:
                    A[item-1] = -1 * abs(A[item-1])
            res = len(A) + 1
            for i in range(n):
                if A[i] > 0:
                    return i+1
            return res
            
