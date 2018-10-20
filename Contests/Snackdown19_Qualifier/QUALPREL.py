import bisect
for _ in range(int(input())):
    n,k=map(int,input().split())
    ar=list(map(int,input().split()))
    ar.sort()
    min=ar[n-k]
    x=bisect.bisect_left(ar,min)
    tmp=ar[x:]
    #print(ar,x,tmp)
    print(len(tmp))
