# IB rearrange-array

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        for i in range(len(A)):
            A[i] += (A[A[i]]%len(A))*len(A)
        for i in range(len(A)):
            A[i] //= len(A)

