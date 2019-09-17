'''
Input:
1
10
A 10
A 15
A 20
I 10
A 22
D 5
A 27
P 3
P 2
P 5

Output:
20
25
15

Where A means add that value to the list
I means increment all items by the value
D means decrement all items by the value
P means print the Kth largest value else -1 if not exist

Approach:
insertion using log(n) binary search then followed by insertion
delta used to store the differences
'''



'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
import heapq, bisect
for _ in range(int(input())):
    queries = int(input())
    values = []
    #heapq.heapify(values)
    delta = 0
    size = 0
    for q in range(queries):
        op, val = input().strip().split()
        val = int(val)
        if op == 'A':
            size += 1
            bisect.insort_left(values, val-delta, lo=0, hi=size-1)
            #heapq.heappush(values, val-delta)
        elif op == 'I':
            delta += val
        elif op == 'D':
            delta -= val
        else:
            if val>size:
                print(-1)
            else:
                print(values[-val] + delta)
                #print(heapq.nlargest(val, values)[-1] + delta)