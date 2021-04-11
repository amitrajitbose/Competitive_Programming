# https://leetcode.com/problems/longest-increasing-path-in-a-matrix
class Solution:
    def longestIncreasingPath(self, matrix):
        m, n = len(matrix), len(matrix[0])
        neighbours = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        @lru_cache(None)
        def dfs(x, y):
            ans = 1
            for dx, dy in neighbours:
                if 0 <= x+dx < m and 0 <= y+dy < n and matrix[x+dx][y+dy] < matrix[x][y]:
                    ans = max(ans, dfs(x+dx, y+dy) + 1) 
            return ans
        
        return max(dfs(i, j) for i, j in product(range(m), range(n)))
