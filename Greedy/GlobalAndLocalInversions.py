# https://leetcode.com/problems/global-and-local-inversions/
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        """
        Approach:
        1) Every local inversion is a global inversion where i and j differ by one
        2) If we can find atleast one global inversion which is not local inversion, then return False
        3) We need to find atleast one pair of A[i] > A[j] such that j-i > 1
        4) Can be done in linear time by maintaining a global max as we traverse the array
        """
        gmax = -float('inf')
        for i in range(len(A)-2):
            gmax = max(gmax, A[i])
            if (gmax > A[i+2]):
                return False
        return True
