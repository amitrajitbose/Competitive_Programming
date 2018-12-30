'''
Link: https://www.hackerrank.com/challenges/bear-and-steady-gene/problem
'''

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the steadyGene function below.
def steadyGene(gene):
    min_length_string = len(gene)
    n = len(gene)
    occurences = defaultdict(int)
    #expected length of each character 
    expected = n//4
    #count frequency of each character
    for g in gene:
        occurences[g] += 1
    #extra characters than expected
    for x in occurences:
        occurences[x] = max(0, occurences[x] - expected)
    
    if occurences['A'] == 0 and occurences['G'] == 0 and occurences['C'] == 0 and occurences['T'] == 0:
        return 0
     
    found = defaultdict(int)
     
    front = 0
    rear = 0
    
    while rear != n:
        found[gene[rear]] += 1
        if found['A'] >= occurences['A'] and \
        found['C'] >= occurences['C'] and \
        found['G'] >= occurences['G'] and \
        found['T'] >= occurences['T']:
            # this is a valid candidate
            min_length_string = min(min_length_string, rear-front+1)
             
            # try to shorten it further
            while found[gene[front]] > occurences[gene[front]]:
                found[gene[front]] -= 1
                front += 1
                min_length_string = min(min_length_string, rear-front+1)
        rear += 1
     
    return min_length_string


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    gene = input()
    result = steadyGene(gene)
    print(result)
	#fptr.write(str(result) + '\n')
    #fptr.close()

