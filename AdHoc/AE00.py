#Problem: http://www.spoj.com/problems/AE00/
import math
def T(n,N):
	return ((N-(n**2))//n)+1

N=int(input())
reqsum=0
k=int(math.sqrt(N))
for i in range(1,k+1):
	reqsum+=T(i,N)
	#print(T(i,N))
print(reqsum)