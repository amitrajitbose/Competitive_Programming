'''
Given a stack of N integers where you can either push or pop an
element in each operation. You are required to maximize the top
element of the stack after performing exactly K operations. If
the stack becomes empty after performing K operations and there is
no other technique for the stack to be non-empty, then print -1.

Print the maximum possible element at the stack top after performing
exactly K operations.

1<=N<=2*10**6
1<=Ai<=10**18
1<=K<=10**9

SAMPLE
6 4
1 2 4 3 3 5 (NOTE: the first item is the top of the stack)

Out: 4

No Explanation

Help: https://stackoverflow.com/questions/51692294/maximize-the-top-element-of-the-stack-after-performing-exactly-k-operations

'''

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n,k = [int(x) for x in input().strip().split()]
arr = [int(x) for x in input().strip().split()]
# beginning = top
# pop = pop(0)
# push = insert(0)
maxpopd = -1 * float('inf')

if k==n:
    for i in range(k-1):
        popd = arr.pop(0)
        maxpopd = max(maxpopd, popd)
    print(max(maxpopd, -1))
elif k<n:
    for i in range(k-1):
        popd = arr.pop(0)
        maxpopd = max(maxpopd, popd)
    print(max(maxpopd, arr[1]))
elif k>n:
    print(max(arr))