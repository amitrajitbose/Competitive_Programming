'''
Author: Amitrajit Bose
Problem: nQueen's Problem - Single Solution
We use tuples to keep track of the position of the queen.
For the backtracking part, we pop the current wrong position of the
placed queen from a stack, which we maintain from the beginning of the 
algorithm.
We pop it and check the next possible location for the queen to be plaed 
basically. We keep recursively doing this.
'''
ans=[]
queens=[]
def isSafe(row,col,queens):
    for i in range(len(queens)-1):
        r=queens[i][0]
        c=queens[i][1]
        if(r==row):
            #same row
            return False
        elif(abs(r-row)==abs(c-col)):
            #diagonal element
            return False
    return True
def placeQueen(col):
    if(col>=n):
        return True
    row=0
    while(row<n):
        queens.append((row, col)) #pushing to the stack
        #print(queens)
        if(isSafe(row, col, queens) and placeQueen(col+1)):
            return True
        queens.pop();
        #print(queens)
        row+=1;
    return False

def nQueenSolver(n, start):
    if(n<=0):
        return None
    if(placeQueen(start)):
        return sorted(queens)
    else:
        return None

if __name__ == '__main__':
    n=int(input())
    print(nQueenSolver(n,0))
