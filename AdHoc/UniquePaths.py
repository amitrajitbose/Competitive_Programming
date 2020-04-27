class Solution:
    def uniquePaths(self, A: int, B: int) -> int:
        if A==1 or B==1:
            return 1
        if A==2 or B==2:
            return max(A,B)
        ans = 1
        for i in range(max(A,B), A+B-1):
            ans *= i
            ans //= (i-max(A,B)+1)
        return ans

# LC 62 Medium
