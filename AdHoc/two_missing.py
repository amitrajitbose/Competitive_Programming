# Given an array of n unique integers where each element in the array is in range [1, n]. 
# The array has all distinct elements and size of array is (n-2). 
# Hence Two numbers from the range are missing from this array. Find the two missing numbers.

def findtwomissing(arr, n):
    # Space = O(1)
    # Time = O(n)
    #
    assert len(arr)==n-2
    
    currxor = 0
    
    for i in range(1,n+1):
        currxor ^= i
    
    for i in arr:
        currxor ^= i
    
    rem = currxor & -currxor

    x = 0
    y = 0
    
    for i in arr:
        if i & rem:
            x ^= i
        else:
            y ^= i

    for i in range(1,n+1):
        if i & rem:
            x ^= i
        else:
            y ^= i
    return [x,y]

assert(findtwomissing([1,3,5,6],6)==[2,4])
assert(findtwomissing([1,2,4],5)==[3,5])
assert(findtwomissing([1,2],4)==[3,4])
assert(findtwomissing([1,6,4,2],6)==[3,5])