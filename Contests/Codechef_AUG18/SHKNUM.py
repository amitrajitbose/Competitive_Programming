# Problem Link: https://www.codechef.com/AUG18B/problems/SHKNUM
import math
def upper(x):
	if(x==0):
		return 1
	return (math.ceil(math.log(x)/math.log(2)))

def lower(x):
	if(x==0):
		return 1
	return (math.floor(math.log(x)/math.log(2)))

def oneEnd(x):
	rem=x
	i=1
	while(rem!=0):
		rem=(x//i)-1
		i=i*2
	return (i//2)

def mmain(n):
	oE = oneEnd(n)
	x = n - oE
	if(n==1):
		return 2;
	elif(upper(n)==lower(n)):
		return 1;
	elif((oE == 2**upper(x))):
		out2=abs(x - 2**lower(x))
		oE = (oE*2)+1
		out1=abs(oE-n)
		return min(out1,out2)
		

	x = n - oneEnd(n)
	ud = abs(2**upper(x) - x)
	ld = abs(x - 2**lower(x))
	out = min(ld,ud)
	return out

test=int(input())
for _ in range(test):
	n = int(input())
	print(mmain(n))

