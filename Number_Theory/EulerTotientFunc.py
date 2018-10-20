'''
Author: @amitrajitbose
Problem : https://www.hackerearth.com/practice/math/number-theory/totient-function/practice-problems/algorithm/euler-totient-function/
'''
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p=2
    while(p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p+=1
    prime[1]=False
    return prime
     

N=int(input())
prime=SieveOfEratosthenes(N+1)
ans=N
for i in range(2,N+1):
    if(prime[i] and N%i==0):
        ans=ans*(1-(1/i))
print(int(ans))
