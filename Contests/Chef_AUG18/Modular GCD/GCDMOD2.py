#Problem: https://www.codechef.com/AUG18B/problems/GCDMOD
#Author : Amitrajit Bose

MOD = (10**9)+7
# Function to return gcd of a and b
def gcd(a, b): 
    if a == 0 :
        return b 
    
    return gcd(b%a, a)

def power(x, y, p) :
    res = 1
    x = x % p 
 
    while (y > 0) :
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res

# MAIN
test=int(input())
for _ in range(test):
    a,b,n = [int(x) for x in input().strip().split()]
    one = (power(a, n, MOD) + power(b, n, MOD))
    two = abs(a-b)
    out = gcd(one, two) % MOD
    print(out)