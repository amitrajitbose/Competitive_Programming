# LC 994

from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[False for i in range(m)] for j in range(n)]
        
        def isSafe(i, j):
            return (i >= 0 and i < n) and (j >= 0 and j < m)
        
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rotten_count, empty_count, minutes = 0, 0, 0
        q = deque([]) # primary queue to be used for BFS
        
        # counting in the rotten tomatoes and putting them inside queue
        # counting in the empty cells
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    visited[i][j] = True
                    q.append((i, j, 0))
                    rotten_count += 1
                elif grid[i][j] == 0:
                    visited[i][j] = True
                    empty_count += 1
                
        while q:
            i, j, minutes = q.popleft()
            
            for i1, j1 in neighbours:
                i2 = i + i1
                j2 = j + j1
                if isSafe(i2, j2) and not visited[i2][j2] and grid[i2][j2] == 1:
                    visited[i2][j2] = True
                    grid[i2][j2] = 2
                    q.append((i2, j2, minutes + 1))
                    rotten_count += 1
        
        if rotten_count + empty_count == n * m:
            return minutes
        return -1

