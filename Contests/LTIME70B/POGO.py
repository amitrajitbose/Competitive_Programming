import sys
for _ in range(int(input())):
    n,k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    maxsum = -1 * sys.maxsize
    allsum = []
    for i in range(k):
        sub = arr[i::k]
        allsum.append([sub,sum(sub)])
        maxsum = max(maxsum, allsum[-1][-1])
    for i in range(k,n):
        sub = allsum.pop(0)
        rem = sub[0].pop(0)
        sub[1]=sub[1]-rem
        allsum.append(sub)
        maxsum = max(maxsum, allsum[-1][-1])
    print(maxsum)