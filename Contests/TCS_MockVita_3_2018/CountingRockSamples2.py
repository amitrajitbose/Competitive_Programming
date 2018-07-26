# function to find first index >= x
def lowerIndex(arr, n, x):
  l = 0
  h = n-1
  while (l <= h):
    mid = (l + h)//2
    if (arr[mid] >= x):
      h = mid - 1
    else:
      l = mid + 1
  return l
 
 
# function to find last index <= x
def upperIndex(arr, n, x):
  l = 0
  h = n-1
  while (l <= h):
    mid = (l + h)//2
    if (arr[mid] <= x):
      l = mid + 1
    else:
      h = mid - 1
  return h
 
 
# function to count elements within given range
def countInRange(arr, n, x, y):
  # initialize result
  count = 0;
  count = upperIndex(arr, n, y) - lowerIndex(arr, n, x) + 1;
  return count
 
# driver function
n,r=[int(x) for x in input().strip().split()]
arr=[int(x) for x in input().strip().split()]
ranges=[]
for _ in range(r):
  i,j=[int(x) for x in input().strip().split()]
  ranges.append((i,j))
 
# Preprocess array to be sorted
arr.sort()
 
# Answer queries
for c in ranges:
  print(countInRange(arr, n, c[0], c[1]))

#RUNTIME ERROR