class Solution:
	# @param A : list of integers
	# @return a list of integers
	def lszero(self, A):
	    if len(A)==0:
	        return [] # corner case
	    ps = 0
	    maxlen = 0
	    maxends = [-1,-1]
	    hmap = dict()
	    hmap[ps] = -1
	    for i in range(len(A)):
	        ps += A[i]
	        if ps not in hmap:
                hmap[ps] = i
            else:
                if i-hmap[ps] > maxlen:
                    maxends = [hmap[ps]+1, i]
                    maxlen = (i-hmap[ps])
        if maxends == [-1,-1]:
            return []
        return A[maxends[0]: maxends[1]+1]

