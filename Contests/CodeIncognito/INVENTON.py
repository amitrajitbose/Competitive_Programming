# https://www.codechef.com/problems/INVENTO

t=int(input())
for _ in range(t):
    n=int(input())
    x=len(str(bin(n)))
    print(x-2)