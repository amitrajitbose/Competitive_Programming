from math import gcd
test=int(input())
for _ in range(test):
	x,y,n,m=[int(bla) for bla in input().strip().split()]
	lcm=(x*y)//gcd(x,y)
	if((lcm//x)<=n and (lcm//y)<=m):
		print("YES")
	else:
		print("NO")
