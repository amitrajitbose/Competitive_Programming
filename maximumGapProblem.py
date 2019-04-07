# Maximum Gap Problem
# http://www.zrzahid.com/the-%E2%80%A9maximum%E2%80%A9-gap%E2%80%A9-problem-%E2%80%A9pigeonhole-%E2%80%A9principle%E2%80%A9/
# http://cgm.cs.mcgill.ca/~godfried/teaching/dm-reading-assignments/Maximum-Gap-Problem.pdf
# https://stackoverflow.com/questions/10262937/array-maximum-difference-algorithm-that-runs-in-on

import sys
from math import floor
def maxGapin(arr):
  n = len(arr)
  if(n<2):
    return 0
  minn,maxx = min(arr),max(arr)
  bucketMaxima = [sys.maxsize for i in range(n-1)]
  bucketMinima = [-sys.maxsize for i in range(n-1)]
  delta = (maxx-minn)/(n-1)
  #populate the buckets
  for i in arr:
    if(i==maxx or i==minn):
      continue
    bIndex = floor((i-minn)/delta)
    if(bucketMaxima[bIndex] == -1*sys.maxsize):
      bucketMaxima[bIndex] = i
    else:
      bucketMaxima[bIndex] = max(bucketMaxima[bIndex], i)
    #similarly for bucketMinima
    if(bucketMinima[bIndex] == sys.maxsize):
      bucketMinima[bIndex] = i
    else:
      bucketMinima[bIndex] = min(bucketMinima[bIndex], i)
  #find the max gap
  print(bucketMaxima,"\n",bucketMinima)
  print(maxx,minn)
  prev = minn
  maxGap = 0
  #following pigeonhole principle to empty bucket
  for i in range(n-1):
    if(bucketMinima[i]==sys.maxsize):
      continue
    maxGap = max(maxGap, bucketMinima[i]-prev)
    prev = bucketMaxima[i]
  return max(maxGap, maxx-prev)

#print(maxGapin([5, 3, 1, 8, 9, 2, 4]))
print(maxGapin([6,44,99,-50,8,1]))