from fractions import gcd
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.sort()
        if len(A) < 2:
            return A
        if len(A) == 2:
            return [A[1],A[0]]
        flag = 0
        i = 2
        while i < len(A):
            if A[i] != (A[i-1] + gcd(A[i-1], A[i-2])):
                flag = 1
                break
            else:
                i += 1
        if not flag:
            # if GCD condition is satisfied then check if last element can be replaced with first one
            if(A[1] != (A[0] + gcd(A[0], A[-1]))):
                return A
            else:
                return [A[-1]] + A[:-1]
        else:
            # thus for index i gcd ordering fails
            # we can try placing A[i] at the front
            if(A[1] != A[0] + gcd(A[0],A[i])):
                return [-1]
            else:
                t = A[i]
                index = i
                n = len(A)
                # means we can place A[i] in beginning but we need to check whether for rest of the array gcd ordering
                # condition is sarisfied or not
                if((i+1)<n and A[i+1]!=A[i-1] + gcd(A[i-1],A[i-2])):
                    return [-1]
                if((i+2)<n and A[i+2]!=A[i+1] + gcd(A[i+1],A[i-1])):
                    return [-1]
                for i in range(i+3, n):
                    if(A[i]!=(A[i-1] + gcd(A[i-1],A[i-2]))):
                        return [-1]
                # if for rest of the array gcd_ordering condition is satisfied then return the resultant array as answer
                #A.erase(A.begin()+i)
                A.insert(0, A.pop(i)) #A.insert(A.begin(),t) # putting A[i] in the beginning
                return A

