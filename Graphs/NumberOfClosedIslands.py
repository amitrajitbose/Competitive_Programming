# LC 1254
# TC: O(mxn)

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and self.dfs(grid, i, j):
                    cnt += 1
        return cnt

    def dfs(self, grid, i, j):
        if not self.valid(grid,i,j):
            return False
        if grid[i][j] == 1:
            return True
        grid[i][j] = 1 # mark
        a=self.dfs(grid, i, j+1)
        b=self.dfs(grid, i+1, j)
        c=self.dfs(grid, i, j-1) 
        d=self.dfs(grid, i-1, j)
        return a & b & c & d

    def valid(self, grid, i, j):
        return i>=0 and j>=0 and i<len(grid) and j<len(grid[0])
    def border(self, grid, i, j):
        return i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1
