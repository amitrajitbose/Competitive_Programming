# https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/bike-trip/

for _ in range(int(input())):
    n = int(input())
    arr1 = [int(x) for x in input().strip().split()]
    arr2 = [int(x) for x in input().strip().split()]
    
    if n==1:
        print(min(arr1[0], arr2[0]))
    else:
        cost1 = [int(x) for x in input().strip().split()]
        cost2 = [int(x) for x in input().strip().split()]
        
        dp1=arr1[0]
        dp2=arr2[0]
        
        for i in range(1,n):
            k = dp1
            l = dp2
            dp1 = min(k, l+cost2[i-1]) + arr1[i]
            dp2 = min(l, k+cost1[i-1]) + arr2[i]
        print(min(dp1, dp2))