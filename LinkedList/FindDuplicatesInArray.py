class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        slow, fast = A[0], A[A[0]]
        while slow!=fast:
            slow = A[slow]
            fast = A[A[fast]]
        # https://medium.com/solvingalgo/solving-algorithmic-problems-find-a-duplicate-in-an-array-3d9edad5ad41
        slow = 0
        while slow!=fast:
            slow = A[slow]
            fast = A[fast]
        if slow == 0:
            return -1
        else:
            return slow
