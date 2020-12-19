# LC 200
# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid):
                return 0
            if j < 0 or j >= len(grid[i]):
                return 0
            if grid[i][j] == '0':
                return 0
            else:
                grid[i][j] = '0' # marking visited
                dfs(grid, i, j+1)
                dfs(grid, i, j-1)
                dfs(grid, i+1, j)
                dfs(grid, i-1, j)
                return 1
        
        if not grid or len(grid) <= 0 :
            return 0
        else:
            numIslands = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == '1':
                        numIslands += dfs(grid, i, j)
            return numIslands

#BFS
from collections import deque
class Solution:
    def isvalid(self, mat, i, j):
        if i<0 or i>=len(mat) or j<0 or j>=len(mat[i]):
            return False
        if mat[i][j] != '1':
            return False
        return True
    
    def numIslands(self, binaryMatrix: List[List[str]]) -> int:
        if not binaryMatrix or len(binaryMatrix) <= 0:
            return 0
        res = 0
        queue = deque()
        for i in range(len(binaryMatrix)):
            for j in range(len(binaryMatrix[i])):
                if binaryMatrix[i][j] == '1':
                    res += 1
                    queue.append([i, j])
                    while queue:
                        nexti, nextj = queue.popleft()
                        if self.isvalid(binaryMatrix, nexti, nextj):
                            binaryMatrix[nexti][nextj] = '2' # mark
                            queue.append([nexti, nextj+1])
                            queue.append([nexti+1, nextj])
                            queue.append([nexti, nextj-1])
                            queue.append([nexti-1, nextj])
        return res

