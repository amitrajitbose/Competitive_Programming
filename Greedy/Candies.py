# Link: https://www.hackerrank.com/challenges/candies/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    incr=[1 for x in range(n)]
    decr=[1 for x in range(n)]
    final=[1 for x in range(n)]
    for i in range(1,n):
        if(arr[i]>arr[i-1]):
            #increasing
            incr[i]=incr[i-1]+1
    for i in range(n-2,-1,-1):
        if(arr[i]>arr[i+1]):
            #decreasing
            decr[i]=decr[i+1]+1
    #print(incr)
    #print(decr)
    for i in range(n):
        final[i]=max(incr[i],decr[i])
    #print(final)
    return sum(final)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)
    result = candies(n, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
