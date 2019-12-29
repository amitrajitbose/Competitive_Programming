class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        '''
        # This is the marker concept, by list modification
        A = list(A)
        if len(A) <= 1:
            return -1
        for i in range(len(A)):
            num = abs(A[i])
            if A[num]>=0:
                A[num] = -1 * A[num] # marking negative means already visited A[i]
            else:
                return num
        return -1
        '''
        
        # This is modified Floyd Warshall concept, cycle in linked list type
        # https://medium.com/solvingalgo/solving-algorithmic-problems-find-a-duplicate-in-an-array-3d9edad5ad41
        
        slow, fast = A[0], A[A[0]]
        while slow!=fast:
            slow = A[slow]
            fast = A[A[fast]]
        # the slow and fast pointers are at the same point now, i.e start point of cycle
        slow = 0
        while slow!=fast:
            slow = A[slow]
            fast = A[fast]
        if slow == 0:
            return -1
        else:
            return slow
