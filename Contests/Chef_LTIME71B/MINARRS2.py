for T in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    check = [[0 for x in range(20)] for x in range(n)]
    m = 0
    for i in range(n):
        s = bin(a[i]).replace("0b","")
        l = len(s)
        m = max(l, m)
        for j in range(l-1, -1, -1):
            print(s[j])
            a[i][l-1-j] = int(s[j])
    s = ''
    for i in range(m):
        c_z = 0
        c_1 = 0
        for j in range(n):
            if a[j][i] == 0:
                c_z += 1
            else:
                c_1 += 1
        if c_1 > c_z:
            s += '1'
        else:
            s += '0'
    s = s.lstrip('0')
    s = s[::-1]
    ans = int(s, 2)
    summ = 0
    for i in range(n):
        summ += (a[i] ^ ans)
    print(summ)