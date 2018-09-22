# https://math.stackexchange.com/questions/1656120/formula-to-find-the-first-intersection-of-two-arithmetic-progressions

from math import gcd
x,p=[int(x) for x in input().strip().split()]
y,q=[int(x) for x in input().strip().split()]
origx=x
if(abs(p-q) % gcd(x,y) != 0):
	print("-1")
else:
	# they will meet
	rhs = (q-p)+(x-y)
	#print("RHS",rhs)
	oldx=x
	while(x<rhs):
		x+=oldx
		#print(x)
	while((x-rhs)%y != 0):
		x+=oldx
		#print(x)
	print(abs((x+p)-origx))