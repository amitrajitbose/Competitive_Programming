'''
Staircase Problem
https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(cache,n):
    return cache[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    cache=[1,1,2]
    for i in range(3,51):
        cache.append(cache[i-1]+cache[i-2]+cache[i-3])
    s = int(input())
    for s_itr in range(s):
        n = int(input())
        res = stepPerms(cache,n)
        fptr.write(str(res) + '\n')

    fptr.close()
