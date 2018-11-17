# https://www.hackerrank.com/contests/game-of-codes-3-0/challenges/ramanujans-prime-substrings
# https://www.hackerrank.com/rest/contests/game-of-codes-3-0/challenges/ramanujans-prime-substrings/download_pdf?language=English

def SieveOfEratosthenes(n):
     
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p=2
    while(p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p+=1
    prime[0]=False
    prime[1]=False
    return prime

sieve=SieveOfEratosthenes(10**6)
for _ in range(int(input())):
  myd=[]
  n=str(input())
  for i in range(len(n)):
    for j in range(i+1,i+7):
      if(j>len(n)):
        break
      else:
        num=int(n[i:j])
        if(sieve[num]):
          myd.append(num)
  print(len(set(myd)))