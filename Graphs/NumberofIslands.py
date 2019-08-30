# LC 200
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

