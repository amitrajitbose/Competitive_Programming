#Author: Amitrajit Bose
#Problem: https://www.hackerrank.com/challenges/magic-square-forming/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def matdiff(a,b):
    cost=0
    for i in range(3):
        for j in range(3):
            cost+=abs(a[i][j]-b[i][j])
    return cost
def formingMagicSquare(s):
    #all possible magic squares
    #magic square
    magic1=[[8,1,6],[3,5,7],[4,9,2]]
    magic2 = list(zip(*magic1[::-1]))
    magic3 = list(zip(*magic2[::-1]))
    magic4 = list(zip(*magic3[::-1]))
    #transposed magic square, also a magic square
    tmagic1=[[8,3,4],[1,5,9],[6,7,2]]
    tmagic2 = list(zip(*tmagic1[::-1]))
    tmagic3 = list(zip(*tmagic2[::-1]))
    tmagic4 = list(zip(*tmagic3[::-1]))
    #computing costs
    cost1=matdiff(magic1,s)
    cost2=matdiff(magic2,s)
    cost3=matdiff(magic3,s)
    cost4=matdiff(magic4,s)
    cost5=matdiff(tmagic1,s)
    cost6=matdiff(tmagic2,s)
    cost7=matdiff(tmagic3,s)
    cost8=matdiff(tmagic4,s)
    return min(cost1,cost2,cost3,cost4,cost5,cost6,cost7,cost8)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
