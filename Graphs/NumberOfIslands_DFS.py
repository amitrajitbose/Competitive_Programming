# LC 200
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        if self.valid(grid,i,j) and grid[i][j] == '1':
            grid[i][j] = '0' # mark
            self.dfs(grid, i, j+1)
            self.dfs(grid, i+1, j)
            self.dfs(grid, i, j-1)
            self.dfs(grid, i-1, j)
            return 1
        return 0

    def valid(self, grid, i, j):
        return i>=0 and j>=0 and i<len(grid) and j<len(grid[0])
