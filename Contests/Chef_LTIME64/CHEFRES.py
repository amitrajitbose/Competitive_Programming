from bisect import bisect_left as bs
t=int(input())
for _ in range(t):
  n,m=[int(x) for x in input().strip().split()]
  time=[]
  for i in range(n):
    a,b=[int(x) for x in input().strip().split()]
    time.append((a,b))
  time=sorted(time)
  starts=[]
  ends=[]
  for i in range(n):
    starts.append(time[i][0])
    ends.append(time[i][1])
  for i in range(m):
    p=int(input())
    #print(p,end=" ")
    if(p>=ends[-1]):
      print(-1)
    elif(p>=starts[-1] and p<ends[-1]):
      print(0)
    elif(p>=starts[0] and p<ends[0]):
      print(0)
    else:
      entry=bs(starts,p)
      exit=bs(ends,p)
      if(entry==0):
        print(starts[0]-p)
        continue
      if(p==ends[exit]):
        exit+=1
      if(starts[entry]>p and ends[entry-1]>p):
        entry-=1
      if(starts[entry]>p and ends[entry-1]<=p and ends[exit]>p):
        print(starts[entry]-p)
        continue
      if(entry==exit):
        print(0)
      elif(entry<exit):
        print(starts[exit]-p)
      
