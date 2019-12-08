class Solution:
	# @param A : list of strings
	# @return an integer
	def solve(self, A):
	    A = [float(x) for x in A]
	    window = [A[0],A[1],A[2]]
	    wsum = sum(window)
	    n = len(A)
	    if n <= 3:
	        # if there are inadequate elements to slide the window
	        return 1 if wsum > 1 and wsum < 2 else 0
	    for i in range(3,n):
	        window.sort() # 3 log 3 = constant time
	        if 1 < wsum and wsum < 2:
    	        #print(window)
    	        return 1
    	    else:
    	        if wsum < 1:
    	            # goal is to replace the smallest value in the window with the next element
    	            # aim is to increase the window sum
    	            wsum -= window[0]
    	            window[0] = A[i]
    	            wsum += window[0]
    	        else:
    	            # goal is to replace the largest value in the window with the next element
    	            # aim is to reduce the window sum
    	            wsum -= window[2]
    	            window[2] = A[i]
    	            wsum += window[2]
    	# Checking the last window
    	if 1 < wsum and wsum < 2:
	        return 1
    	return 0

