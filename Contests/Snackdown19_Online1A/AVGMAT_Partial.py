def manhattan(x1,y1,x2,y2):
  return (abs(x1-x2)+abs(y1-y2))

t=int(input())
for _ in range(t):
  n,m=[int(x) for x in input().strip().split()]
  arr=[]
  for eachrow in range(n):
    row=list(str(input()))
    arr.append(row)
  ones=[]
  for i in range(n):
    for j in range(m):
      if(arr[i][j]=='1'):
        ones.append((i,j))
  maxrange=(n+m)-2
  d=[0 for i in range((n+m)-1)]
  l=len(ones)
  for i in range(l):
    for j in range(i+1,l):
      #if(i!=j):
      d[manhattan(ones[i][0],ones[i][1],ones[j][0],ones[j][1])]+=1
  for i in range(1,maxrange+1):
    print(d[i],end=" ")
  print("")
  
