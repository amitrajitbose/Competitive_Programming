#https://www.codechef.com/IEMCO5/problems/IEMCO5C/

from fractions import gcd
n,q,k=[int(x) for x in input().strip().split(' ')]
segments=[]
starts=[]
for _ in range(n):
    s,e=[int(x) for x in input().strip().split(' ')]
    starts.append(s) #start elements
    elementsinsegment=((e-s)//k)+1
    segments.append(elementsinsegment)
 
avg=0
for query in range(q):
    val=int(input())
    for i in range(n):
        if(segments[i]<val):
            val-=segments[i]
        else:
            avg+=(starts[i]+(k*(val-1)))
            break
 
g=gcd(avg,q)
numerator=avg//g
deno=q//g
print(numerator,end="")
print("/",end="")
print(deno) 