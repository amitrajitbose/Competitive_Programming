#https://www.codechef.com/APRIL18B/problems/WGHTNUM

t=int(input())
MOD=1000000007
for _ in range(t):
  n,w=[int(x) for x in input().strip().split(' ')]
  if(abs(w)<=9):
    if(w>=0):
      x=n-2
      res=(9-w)*pow(10,x,MOD)
      print(res%MOD)
    else:
      x=n-2
      res=(10+w)*pow(10,x,MOD)
      print(res%MOD)
  else:
    print(0) 