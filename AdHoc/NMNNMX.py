# Problem: https://www.codechef.com/JULY18B/problems/NMNMX/

'''
from itertools import combinations
MOD=(10**9)+7
t=int(input())
for _ in range(t):
	n,k=[int(x) for x in input().strip().split()]
	a=[int(x) for x in input().strip().split()]
	a=sorted(a)
	product=1
	comb=list(combinations(a,k))
	for i in comb:
		print(*i)
		for j in range(1,k-1):
			product=(product*(i[j]))%MOD
	print(product)
'''

from math import factorial as fact

mod= int(10**9+7)

#returns nCr value if n>=r else 0
def C(n,r):
    if(n<r):
        return 0 #not possible
    else:
        return fact(n) // (fact(r) * fact(n-r))

for _ in range(int(input())):
    n,k=[int(x) for x in input().strip().split()]
    a=list(map(int,input().split()))
    
    a=sorted(a)
    minCount=[]
    tot,ans=C(n-1,k-1),1
    x=tot
    #print(x) #prints n-1 C r-1 , debugging

    for i in range(n-k+1):
        minCount.append(x)
        x=(x*(n-k-i))//(n-i-1)
    for i in range(n-k+1,n):
        minCount.append(0)
    #since maxCount will be just the reverse of minCount
    #thus maxCount[i]=minCount[n-i-1]
    for i in range(n//2):
        power=tot-(minCount[i]+minCount[n-1-i])
        ans = (ans*(pow(a[i]*a[n-i-1],power,mod)))%mod
    if(n%2!=0):
        power=tot-2*(minCount[n//2])
        ans=(ans*pow(a[n//2],power,mod))%mod
    #print(minCount)
    print(ans%mod) 