"""
You are given two integers N and A. Task in to determine the
permutation K of (0,1,2,....(2^N)-1) such that

K0 = A
K(i) and K(i+1) differ by only one bit in their binary form
K(0) and K((2^N) - 1) must also differ by one bit, same as above rule

If there are multiple answers print any of them

Input:
2 1
Output:
1 3 2 0
"""
def generateGrayArray(n: int):
    # generate gray code for n bits
    arr = ['0', '1']
    i, j = 2, 0
    while(True):
        if i >= 1 << n:
            break
        # append reverse of list arr to itself
        for j in range(i-1, -1, -1):
            arr.append(arr[j])

        # append first part by 0
        for j in range(i):
            arr[j] = '0' + arr[j]

        # append second part by 1
        for j in range(i, 2*i):
            arr[j] = '1' + arr[j]

    # convert to decimal, base 10
    for i in range(len(arr)):
        arr[i] = int(arr[i], 2)
    return arr

def get_perm(n, a):
    perm = generateGrayArray(n)
    start = perm.index(a)
    return perm[start:] + perm[:start]

def main():
    n,a = [int(x) for x in input().strip().split()]
    print(*get_perm(n,a))

main()

# Reference
# https://www.geeksforgeeks.org/given-a-number-n-generate-bit-patterns-from-0-to-2n-1-so-that-successive-patterns-differ-by-one-bit/
