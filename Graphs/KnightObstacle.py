'''
You are given a keypad with 1 to 9. You are given a start point from where you have to start traversal.
Length of the traversal is also given. Each step is like a knight's step on a chess board, like two and a
half step in L shape.
Out of the 9 keys available, you will not be allowed to go to two of them marked with 'X'.
You need to find out the number of unique paths possible from the given starting point for all the given input.
'''

class KnightPaths:
    def __init__(self):
        self.paths = 0
        self.showPaths = False

    def valid(self, matrix, i ,j):
        if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[i]) or matrix[i][j] == 'X':
            return False
        return True

    def traverse(self, matrix, path, start, targetLen, i, j):
        if not self.valid(matrix, i, j):
            return
        if len(path) == targetLen-1:
            if self.showPaths:
                print(' -> '.join(path + [matrix[i][j]])) # valid path
            self.paths += 1
            return

        # Try all possible Knight-like jumps
        self.traverse(matrix, path + [matrix[i][j]], start, targetLen, i+1, j+2)
        self.traverse(matrix, path + [matrix[i][j]], start, targetLen, i+1, j-2)
        self.traverse(matrix, path + [matrix[i][j]], start, targetLen, i-1, j+2)
        self.traverse(matrix, path + [matrix[i][j]], start, targetLen, i-1, j-2)
        self.traverse(matrix, path + [matrix[i][j]], start, targetLen, i+2, j+1)
        self.traverse(matrix, path + [matrix[i][j]], start, targetLen, i+2, j-1)
        self.traverse(matrix, path + [matrix[i][j]], start, targetLen, i-2, j+1)
        self.traverse(matrix, path + [matrix[i][j]], start, targetLen, i-2, j-1)

    def numberOfPaths(self, matrix, start, n, showPaths=False):
        self.showPaths = showPaths
        starti, startj = -1, -1
        # searching for start coordinates
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == start:
                    starti, startj = i, j
                    break
            if starti != -1 and startj != -1:
                break
        self.traverse(matrix, [], start, n, starti, startj)
        return self.paths

def main():
    print(KnightPaths().numberOfPaths([['X','2','3'],['4','X','6'],['7','8','9']], '2', 3, True))
    assert KnightPaths().numberOfPaths([['X','2','3'],['4','X','6'],['7','8','9']], '2', 3, False) == 4
    assert KnightPaths().numberOfPaths([['X','2','3'],['4','X','6'],['7','8','9']], '5', 3, False) == 0
    print(KnightPaths().numberOfPaths([['1','2','3'],['4','X','6'],['X','8','9']], '4', 4, True))

main()