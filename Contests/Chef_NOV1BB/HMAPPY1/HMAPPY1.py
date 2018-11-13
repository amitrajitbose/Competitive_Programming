# Author : @amitrajitbose
from collections import deque
def count(arr,k):
  gsum=0
  lsum=0
  for i in arr:
    if(i==1):
      lsum+=1
    else:
      gsum=max(gsum,lsum)
      lsum=0
  gsum=max(gsum,lsum)
  if(gsum<k):
    return gsum
  else:
    return k
    

n,q,k=[int(x) for x in input().strip().split()]
arr2=[int(x) for x in input().strip().split()]
arr2=deque(arr2)
queryString=list(input())
shift=0
table={}

for quer in queryString:
  if(quer == '?'):
    if(not (shift in table)):
      x=count(list(arr2),k)
      print(x)
      table[shift]=x
    else:
      print(table[shift])
  else:
    arr2.rotate(1)
    shift+=1
    shift=shift%n

