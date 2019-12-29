#https://www.interviewbit.com/problems/max-distance/
def maximumGap(A):
    left = [A[0]]
    right = [A[-1]]
    n = len(A)
    for i in range(1,n):
        left.append(min(left[-1], A[i]))
    for i in range(n-2, -1, -1):
        right.insert(0, max(right[0], A[i]))
    i,j,gap = 0, 0, -1
    while (i < n and j < n):
        if left[i] < right[j]:
            gap = max(gap, j-i)
            j += 1 # look for a larger gap
        else:
            i += 1
    return gap

# test cases
assert(maximumGap([3,5,4,2])==2)
assert(maximumGap([3,2,1,0])==-1)