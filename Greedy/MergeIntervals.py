# LC 56 - M
class Solution:
    def merge(self, inv: List[List[int]]) -> List[List[int]]:
        if not len(inv):
            return []
        inv = sorted(inv, key=lambda x: x[0])
        finv = [inv[0]]
        for i in range(1, len(inv)):
            if finv[-1][1] >= inv[i][0]:
                finv[-1][1] = max(finv[-1][1], inv[i][1]) #merging
            else:
                finv.append(inv[i])
        return finv
