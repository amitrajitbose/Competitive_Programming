# Stacks
# IB : Nearest Smallest Element
# @amitrajitbose
#
#
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
	    incrStack = [A[0]]
	    res = [-1]
	    for i in range(1, len(A)):
	        if A[i] <= incrStack[0]:
	            # first element stores the smallest 
	            # replace the stack
	            incrStack = [A[i]]
	            res.append(-1)
	        else:
	            for j in range(len(incrStack)-1, -1, -1):
	                if incrStack[j] < A[i]:
	                    res.append(incrStack[j])
	                    incrStack.append(A[i])
	                    break
	    return res
