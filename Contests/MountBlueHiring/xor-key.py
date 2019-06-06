#!/bin/python3
from functools import reduce
import bisect

NBITS = 15
ALLONES = (1 << NBITS) - 1

def lookup(low, high, data):
    ''' returns >= 0 - index of a single match, < 0 - multiple matches with low = -(m+1),
    None - no matches '''
    left = bisect.bisect_left(data, low)
    right = bisect.bisect_right(data, high)
    n = right - left
    return None if n <= 0 else -data[left] - 1 if n > 1 else data[left]

def getMatch(goal, low, high, index, bit):
    ind = index[bit]
    data = ind[goal >> bit]
    return lookup(low, high, data) if data else None

def matchImpossible(andOfX, orOfX, goal, mask):
    gm = goal & mask
    return (gm == 0 and andOfX & mask == mask) or (gm == mask and orOfX & mask == 0)
    
def solve(andOfX, orOfX, goal, low, high, index):
    
    bit = 8
    mask = ((1 << bit) - 1)
    highMask = ALLONES & ~mask
    if matchImpossible(andOfX, orOfX, goal, highMask):
        goal = (ALLONES & ~goal & highMask) | (goal & mask)
        bit -= 1
        match = None
    else:
        bit = 7
        match = getMatch(goal, low, high, index, bit)
        if match == None:
            bit = 11
            match = getMatch(goal, low, high, index, bit)
            if match == None:
                bit = NBITS - 1
        else:
            bit2 = 3
            match2 = getMatch(goal, low, high, index, bit2)
            if match2 != None:
                bit, match = bit2, match2

    if match == None:
        while bit >= 0:
            match = getMatch(goal, low, high, index, bit)
            if match != None:
                break
            goal ^= 1 << bit
            bit -= 1
    
    bit -= 1
    while bit >= 0 and match < 0:
        match = getMatch(goal, low, high, index, bit)
        if match == None:
            goal ^= 1 << bit
            match = getMatch(goal, low, high, index, bit)
        bit -= 1

    return match if match >= 0 else -match - 1
    
def buildIndexFor(x, bit):
    size = 1 << (NBITS - bit)
    vec = [[] for _ in range(size)]
    for i, v in enumerate(x):
        vec[v >> bit].append(i)
    return vec

def buildIndex(x):
    index = [buildIndexFor(x, b) for b in range(NBITS)]    
    return index

def findHighBit(x):
    r = 0
    x >>= 1
    while x:
        r += 1
        x >>= 1
    return r

def andFun(x, y): return x & y
def orFun(x, y): return x | y
    
def main():
    t = int(input())
    for _t in range(t):
        _n, nq = [int(i) for i in input().split()]
        x = [int(i) for i in input().split()]
        index = buildIndex(x)
        andOfX = reduce(andFun, x, ALLONES)
        orOfX = reduce(orFun, x, 0)
        for _q in range(nq):
            a, low, high = [int(i) for i in input().split()]
            goal = ALLONES ^ a
            ibest = solve(andOfX, orOfX, goal, low - 1, high - 1, index)
            answer = a ^ x[ibest]
            print(answer)

main()
