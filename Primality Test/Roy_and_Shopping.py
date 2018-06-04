#Sieve
def SieveOfEratosthenes(n):
     
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    reqlist=[]
    p=2
    while(p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p+=1
     
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            reqlist.append(p)
    return(reqlist)

primes=SieveOfEratosthenes(10**6 +1)
t=int(input())
for _ in range(t):
	r=int(input())
	for i in primes:
		if i>=r:
			print(0)
			break
		elif r%i==0:
			print(r-i)
			break