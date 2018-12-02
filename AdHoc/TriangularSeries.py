'''
Triangular Series : 1,3,6,10,15,21,28...
Given a number n, find its position in the triangular series (nearest smaller or equal to value).
For example: n=8, output=6
'''
'''
Approach: Sridhara Acharya
(n(n+1))/2 = nth element in triangular series
We need to calculate n given the element is known
'''
from math import floor
from math import sqrt
def find(n):
	k = (floor(sqrt(4*2*n))-1)//2
	val = ((k+1)*(k+2))//2
	if(val == n):
		return n
	else:
		return (k*(k+1))//2

assert find(6)==6
assert find(8)==6
assert find(10)==10
assert find(16)==15