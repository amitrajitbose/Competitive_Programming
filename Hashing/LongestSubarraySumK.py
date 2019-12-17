class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        prefix = dict()
        prefix[0] = -1 # initialising prefix sum
        ps = 0
        maxlen = -1
        for i in range(len(A)):
            ps += A[i]
            if ps not in prefix:
                prefix[ps] = i
            if ps-B in prefix:
                maxlen = max(maxlen, i-prefix[ps-B])
        return maxlen

