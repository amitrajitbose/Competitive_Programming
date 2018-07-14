#Problem: https://codeforces.com/problemset/problem/1009/A

n,m=[int(x) for x in input().strip().split()]
c=[int(x) for x in input().strip().split()]
a=[int(x) for x in input().strip().split()]
ptrc=0
ptra=0
lc=len(c)
la=len(a)
cnt=0
while(ptrc<lc and ptra<la):
  if(c[ptrc]<=a[ptra]):
    cnt+=1
    ptrc+=1
    ptra+=1
  else:
    ptrc+=1

print(cnt)