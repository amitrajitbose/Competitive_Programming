a,d,m = [int(x) for x in input().strip().split()]
g,p,b = [int(x) for x in input().strip().split()]
flag = 1
if(g<a):
  flag = 0 #not enuf green for andrew
else:
  g=g-a
  a=0
print(g,p,b)
if(g+p < d):
  flag = 0
else:
  gnew = max(0, g-d)
  d = d-g
  p = p-d
  g = gnew
  d=0
print(g,p,b)
if(g+p+b < m):
  flag = 0
else:
  g = max(0, g-m)
  m = m-g
  p = max(0, p-m)
  m = m-p
  b = b-m
  m=0
print(g,p,b)
if(flag):
  print("YES")
else:
  print("NO")

