def oddSetBits(n):
    # returns 1 if n has odd number of set bits, else 0 if n has even number of set bits
    if n == 0:
        return 0
    if n%2 == 0:
        return oddSetBits(n//2)
    if n%2 == 1:
        return 1 - oddSetBits(n//2)

def checkOddSetBits(n):
    # this is O(set bits) time
    cnt = 0
    while n>0:
        n = n & (n-1)
        cnt += 1
    return cnt%2

def main():
    for _ in range(int(input())):
        n,q = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        for query in range(q):
            elem = int(input().strip())
            odd, even = 0, 0
            for i in arr:
                if checkOddSetBits(elem ^ i):
                    odd += 1
                else:
                    even += 1
            print(even,odd)
    
main()
        