'''
Find the element which is present only once.
All other elements are present thrice in the array.
'''

import math
class Solution:
    def ithBit(self,n,i):
        return (n>>(i-1))%2 # return 1 if ith Bit is Set else 0
	
	def special(self,lst):
	    # From CareerCup #In Linear Time
        ones = 0
        twos = 0
        for x in lst:
            twos |= ones & x
            ones ^= x
            not_threes = ~(ones & twos)
            ones &= not_threes
            twos &= not_threes
        return ones
        
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
	    '''
	    # n*logn FAILS
	    return (3*(sum(set(A))) - sum(A))//2 # one method
	    '''
	    
	    '''
	    # n*log(max) PASSES
	    if len(A)==1:
	        return A[0]
	    m = math.ceil(math.log(max(A),2))
	    res = ''
	    for i in range(1,m+1):
	        val = sum([self.ithBit(j,i) for j in A]) % 3
	        res = str(val) + res
	    return int(res,2)
	    '''
	    # n PASSES
	    return self.special(A)

