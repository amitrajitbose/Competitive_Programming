# https://www.codechef.com/ELE32018/problems/JACKJILL

t=int(input())
for _ in range(t):
  n,k,d=[int(x) for x in input().strip().split()]
  a=[int(x) for x in input().strip().split()]
  b=[int(x) for x in input().strip().split()]
  flag=0
  res1=0
  res2=0
  for i in range(k):
    res1 += a[i]
    res2 += b[i]
  if(res1+res2 >= d):
    flag=1
  else:
    for i in range(k,n):
      res1 = res1 + a[i] - a[i-k]
      res2 = res2 + b[i] - b[i-k]
      if(res1+res2 >= d):
        flag=1
        break

  if(flag):
    print("no")
  else:
    print("yes")
