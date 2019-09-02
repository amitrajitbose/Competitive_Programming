class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i] = A[i][::-1] # reversing
            for j in range(len(A[i])):
                A[i][j] ^= 1
        return A

