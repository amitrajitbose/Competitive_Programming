class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        preA = [0]
        for i in range(len(A)):
            preA.append(preA[-1]+A[i])
        A.sort()
        preB = [0]
        for i in range(len(A)):
            preB.append(preB[-1]+A[i])
        chunks = 0
        for i in range(1,len(A)+1):
            if preA[i] == preB[i]:
                chunks += 1
        return chunks

