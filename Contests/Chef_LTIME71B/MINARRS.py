for _ in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    maxxlen = len(bin(max(arr)))-2
    binaries = []
    for i in arr:
        bform = '{0:0'+str(maxxlen)+'b}'
        bform = bform.format(i)
        binaries.append(list(bform))
    res = []
    for i in range(maxxlen):
        zeroes, ones = 0, 0
        for j in range(n):
            if(binaries[j][i]=='0'):
                zeroes+=1
            else:
                ones+=1
        if(zeroes>=ones):
            res.append('0')
        else:
            res.append('1')
    scalarx = int(''.join(res),2)
    fsum = 0
    for i in arr:
        fsum += i^scalarx
    print(fsum)
