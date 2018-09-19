#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(grid):
    grid=sorted(grid)
    print(grid)
    #grouping them
    A=[grid[0]]
    B=[grid[4]]
    C=[]
    for i in range(1,4):
        item=grid[i]
        if(item[0]==A[0][0]):
            A.append(item)
        elif(item[0]==B[0][0]):
            B.append(item)
        else:
            C.append(item)
    if(len(A)==1 and len(B)==1 and len(C)==3):
        print("Middle")
        if(grid[1][0]==grid[2][0] and grid[2][0]==grid[3][0]):
            # got straight line
            if((grid[0][0]==grid[1][0]-1 and grid[4][0]==grid[3][0]+1) and (grid[4][0]-grid[0][0]==2)):
                if((grid[4][0]-grid[2][0])==(grid[2][0]-grid[0][0]))and(grid[0][1]==grid[4][1]):
                    return "Yes"
        return "No"
    elif(len(A)==3 and len(B)==1 and len(C)==1):
        print("Left")
        if(grid[0][0]==grid[1][0] and grid[1][0]==grid[2][0]):
            # got straight line
            if((grid[3][0]==grid[2][0]+1 and grid[4][0]==grid[3][0]+1) and (grid[4][0]-grid[0][0]==2)):
                if((grid[3][0]-grid[2][0])==(grid[4][0]-grid[3][0]))and(grid[3][1]==grid[4][1]):
                    return "Yes"
        return "No"
    elif(len(A)==1 and len(B)==3 and len(C)==1):
        print("Right")
        if(grid[2][0]==grid[3][0] and grid[3][0]==grid[4][0]):
            # got straight line
            if((grid[2][0]==grid[1][0]+1 and grid[1][0]==grid[0][0]+1) and (grid[4][0]-grid[0][0]==2)):
                if((grid[1][0]-grid[0][0])==(grid[2][0]-grid[1][0]))and(grid[0][1]==grid[1][1]):
                    return "Yes"
        return "No"
    return "No"
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        points = []

        for _ in range(5):
            points.append(list(map(int, input().rstrip().split())))

        result = solve(points)

        fptr.write(result + '\n')

    fptr.close()

