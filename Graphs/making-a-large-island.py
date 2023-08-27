# https://leetcode.com/problems/making-a-large-island/submissions/
# LC 827 Hard

from collections import deque
class Solution:
    def getNeighbours(self, i, j, n):
        res = []
        if (i + 1) < n:
            res.append((i+1, j))
        if (i - 1) >= 0:
            res.append((i-1, j))
        if (j + 1) < n:
            res.append((i, j+1))
        if (j - 1) >= 0:
            res.append((i, j-1))
        return res

    def largestIsland(self, grid: List[List[int]]) -> int:
        islandSize = []
        n = len(grid)

        for i in range(n):
            for j in range(n):
                bfs = deque([(i,j)])

                if grid[i][j] == 1:
                    # if island then store the size of that island
                    islandSize.append(1)
                    # check for connect island pieces
                    while bfs:
                        v = bfs.popleft()
                        # marking these islands in one group, like 2,3,4...
                        grid[v[0]][v[1]] = len(islandSize) + 1

                        # do the same for all the neighbors of the node
                        for nbr in self.getNeighbours(v[0], v[1], n):
                            if (grid[nbr[0]][nbr[1]] == 1):
                                grid[nbr[0]][nbr[1]] = len(islandSize) + 1 #2,3,4...
                                islandSize[-1] += 1 # update the size of this island
                                bfs.append((nbr[0], nbr[1]))
        ans = 0
        if islandSize:
            ans = max(islandSize)
        
        for i in range(n):
            for j in range(n):
                # now look for water bodies surrounded by islands
                if grid[i][j] == 0:
                    curr_size = 1
                    neighbourGroups = set([grid[x[0]][x[1]] for x in self.getNeighbours(i, j, n) if (grid[x[0]][x[1]] != 0)])
                    for nbr in neighbourGroups:
                        # compute the resultant island size if this element to go 0 -> 1
                        curr_size += islandSize[nbr - 2]
                    ans = max(ans, curr_size)
        return ans
