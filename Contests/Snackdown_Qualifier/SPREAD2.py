#Author : @amitrajitbose
t=int(input())
for _ in range(t):
  n=int(input())
  arr=[int(x) for x in input().strip().split()]
  pref=[0 for x in range(n)]
  pref[0]=arr[0]
  day=0
  for i in range(1,n):
    pref[i]=pref[i-1]+arr[i]
  know=1
  dontknow=n-1
  sumk=pref[0]
  while(dontknow>0):
    know+=sumk
    dontknow=n-know
    if(know-1>=n):
      sumk=pref[n-1]
    else:
      sumk=pref[know-1]
    day+=1
  print(day)
