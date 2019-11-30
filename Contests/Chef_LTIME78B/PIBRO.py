def verify(a,n,k,seg):
    pass

def longestSubSeg(a,n,k):
    low = 0
    high = n
    x = 0
    while low <= high:
        mid = (low + high)//2
        if verify(a,n,k,mid):
            x = max(x, mid)
        else:
            

for _ in range(int(input())):
    n,k = [int(x) for x in input().strip().split()]
    a = [int(x) for x in list(input())]
    print(a)
    print(longestSubSeg(a, n, k))