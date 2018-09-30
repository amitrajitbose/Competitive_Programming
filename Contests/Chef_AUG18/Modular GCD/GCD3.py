MOD = (10**9)+7
def gcd(a, b) :
	
	if (a == 0) :
		return b
		
	return gcd(b % a, a)


def reduceB(a, b) :
	
	mod = 0

	for i in range(0, len(b)) :
		
		mod = (mod * 10 + ord(b[i])) % a

	return mod

def power(x, y, p) :
    res = 1
    x = x % p 
 
    while (y > 0) :
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res

def gcdLarge(a, b) :
	# Reduce 'b' (second number)
	# after modulo with a
	num = reduceB(a, b)

	# gcd of two numbers
	return gcd(a, num)


# Driver program
test=int(input())
for _ in range(test):
	a,b,n = [int(x) for x in input().strip().split()]
	one = (power(a, n, MOD) + power(b, n, MOD))
	two = abs(a-b)
	if(one == 0 and two > 0):
		out=two
	elif(two == 0 and one > 0):
		out=one
	elif(one == two):
		out=one
	else:
		one = str(one)
		out = gcdLarge(two, one)
	out = out  % MOD
	print(out)



