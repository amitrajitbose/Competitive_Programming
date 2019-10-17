"""
Given a grid where each integer refers to a color, return the maximum number
of connected colours. A color is connected to another adjacent color if the are of
the same colour, diagonal connections are not allowed.
"""

def isValid(grid, i, j):
	if i < 0 or j < 0:
		return False
	if i >= len(grid):
		return False
	if j >= len(grid[i]):
		return False
	if grid[i][j] == -1:
		return False # already visited
	return True

def visit(grid, i, j) -> int:
	if not isValid(grid, i, j):
		return 0
	cnt = 1
	thiscolor = grid[i][j]
	grid[i][j] = -1 # mark as visited
	if isValid(grid,i,j+1) and thiscolor == grid[i][j+1]:
		cnt += visit(grid, i, j+1)
	if isValid(grid,i,j-1) and thiscolor == grid[i][j-1]:
		cnt += visit(grid, i, j-1)
	if isValid(grid,i-1,j) and thiscolor == grid[i-1][j]:
		cnt += visit(grid, i-1, j)
	if isValid(grid,i+1,j) and thiscolor == grid[i+1][j]:
		cnt += visit(grid, i+1, j)
	return cnt

def getMaxCount(grid):
	maximum = 1
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			maximum = max(maximum, visit(grid, i, j))
	return maximum

def main():
	grid = [
			[1,1,2,3],
			[1,2,3,2],
			[3,2,2,2]
		   ]
	assert(getMaxCount(grid)==5)

	grid2 = [
			[1,2,1,2],
			[3,2,2,2],
			[3,3,1,2],
			[1,2,2,2],
			[2,2,3,1]
			]
	assert(getMaxCount(grid2)==11)

main()

