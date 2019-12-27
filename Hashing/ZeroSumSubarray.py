class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # line of thought
        # we can create a prefix sum
        # if any element in the prefix sum repeats or it is zero at any point
        # then we can conclude that there is atleast one subarray with sum zero
        prefixsum = set([A[0]])
        s = A[0]
        for i in range(1,len(A)):
            if s == 0:
                return 1
            s += A[i]
            if s == 0:
                return 1
            if s in prefixsum:
                return 1
            prefixsum.add(s)
        return 0

