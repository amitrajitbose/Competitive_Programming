from collections import Counter
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        freq = Counter(A + B)
        n = len(A)
        maxkey, maxval = -1, -1
        for i in freq:
            if freq[i] > maxval:
                maxkey = i
                maxval = freq[i]
        if maxval < n:
            return -1
        Acnt, Bcnt = 0, 0
        for i in range(n):
            if A[i] != maxkey and B[i] != maxkey:
                return -1
            if A[i] != maxkey:
                Acnt += 1
            elif B[i] != maxkey:
                Bcnt += 1
        return min(Acnt, Bcnt)

