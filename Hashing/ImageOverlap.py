from collections import defaultdict as d
class Solution:
    
    def getindices(self, matrix):
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==1: res.append((i,j))
        return res
    
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        # ---- O(n^2) solution -----
        a, b = self.getindices(A), self.getindices(B)
        res = 0
        translationcost = d(int)
        for i in a:
            for j in b:
                cost = (j[0]-i[0],j[1]-i[1])
                translationcost[cost] += 1
                res = max(res, translationcost[cost])
        #print(translationcost)
        return res