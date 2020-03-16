def main():
    for _ in range(int(input())):
        n,m = [int(x) for x in input().strip().split()]
        types = [0] * (m+1)
        present = [False] * (m+1)
        f = [int(x) for x in input().strip().split()]
        p = [int(x) for x in input().strip().split()]
        for i in range(n):
            types[f[i]] += p[i]
            present[f[i]] = True
        # get min price
        minp = float('inf')
        for i in range(1,m+1):
            if present[i]:
                minp = min(minp, types[i])
        # print(present)
        print(minp)

main()