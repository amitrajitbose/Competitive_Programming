import sys
sys.setrecursionlimit(110000)
def reverse_precompute(arr):
    n = len(arr)
    temp = [0]*n
    temp[-1] = arr[-1]
    for i in range(n-2,-1,-1):
        temp[i] = temp[i+1] + arr[i]
    return temp

def switch(a,b,ind,n,precomputed_b):
    if(ind==n-1):
        return max(a[-1],b[-1])
    else:
        return max(precomputed_b[ind], a[ind]+switch(a,b,ind+1,n,precomputed_b))

for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    b = [int(x) for x in input().strip().split()]
    precomputed_b = reverse_precompute(b)
    print(switch(a,b,0,n,precomputed_b))
