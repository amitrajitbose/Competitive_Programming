class Solution:
	# @param A : tuple of strings
	# @return an integer
	def isValidSudoku(self, A):
	    # check repetitions in rows
	    for row in A:
	        row = list(row.replace('.', '')) # removing dots
	        if len(row) != len(set(row)):
	            return 0 # false
	    
	    # check repetitions in column
	    for i in range(9):
	        col = [A[j][i] for j in range(9) if A[j][i] != '.']
	        if len(col) != len(set(col)):
	            return 0 # false
	    
	    # check boxes each of size 3*3
	    for i in range(0,9,3):
	        for j in range(0,9,3):
	            box = set([])
	            for p in range(i, i+3):
	                for q in range(j, j+3):
	                    if A[p][q] != '.' and A[p][q] not in box:
	                        box.add(A[p][q])
	                    elif A[p][q] != '.' and A[p][q] in box:
	                        return 0 # false
	    return 1 # true

