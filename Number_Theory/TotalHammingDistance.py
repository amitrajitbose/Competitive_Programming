# IB # LCM477
from math import ceil, log
class Solution:
	# @param A : list of integers
	# @return an integer
	def ithBitSet(self, n, i):
	    return (n >> (i-1))%2
	def cntBits(self, A):
	    # Leetcode Hack
	    #return sum(2 * b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, A))) % ((10**9)+7)
	    # Gareebo Ka Soluchaan
	    if len(A) < 1:
            return 0
	    if max(A) < 2:
	        return max(A)
	    m = ceil(log(max(A),2))
	    res = 0
	    n = len(A)
	    MOD = ((10**9)+7)
	    for i in range(1,m+2):
	        setcount = sum([self.ithBitSet(j,i) for j in A])
	        #print(setcount, n-setcount)
	        #res += setcount * (n-setcount) # when i <= j
	        res += setcount * (n-setcount) * 2 # because all pairs, i can be greater than j as well
	    return res % MOD

'''
The function f(x,y) is called the hamming distance for bitwise algebra
'''

