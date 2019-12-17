class Solution:
	# @param A : tuple of strings
	# @return a list of list of integers
	def anagrams(self, A):
	    hmp = dict()
	    pairs = []
	    for i in range(len(A)):
	        vec = self.vectorize(A[i]) # get the vector string
	        if vec not in hmp:
	            hmp[vec] = [i+1]
	        else:
	            # found an anagram
	            hmp[vec].append(i+1)
	    return list(hmp.values())

	def vectorize(self, w):
	    vec = [0] * 26
	    for i in range(len(w)):
	        vec[ord(w[i])-97] += 1
	    return ''.join(list(map(str, vec)))
