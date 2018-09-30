# https://www.codechef.com/problems/PPERM

MAX=5000001
MOD=1000000007
def SieveOfEratosthenes(n):
    prime = [1 for i in range(n+1)]
    prime[1]=0
    p=2
    while(p*p <= n):
         
        if (prime[p] == 1):
            for i in range(p*2, n+1, p):
                prime[i] = 0
        p+=1
    return prime

def pperm():
    prime=SieveOfEratosthenes(MAX)
    perm=[1 for x in range(MAX)]
    primes=[0 for x in range(MAX)]

    for i in range(2,MAX):
        primes[i]=primes[i-1]+prime[i] # cumulating no. of primes
        perm[i]=(perm[i-1]*(primes[i]+1))%MOD
    
    return perm

perm=pperm()
t=int(input())
for _ in range(t):
    n=int(input())
    print(perm[n])
