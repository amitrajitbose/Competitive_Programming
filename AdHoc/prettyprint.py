# IB/prettyprint
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        res = []
        midrow = [i for i in range(1, A+1)]
        for i in range(A-1):
            midrow.insert(0, midrow[0]+1)
        # mid row made
        res.append(midrow)
        
        aux = midrow[:] # copy
        for i in range(A-1):
            for j in range(A-1-i, A-1+i+1):
                aux[j] += 1
            res.append(aux[:])
            res.insert(0, aux[:])
        return res
