"""
Given a 1-d array candy crush, return the shortest array after removing all the continuous same numbers (the repeating number >= 3)
input: 1-d array [1, 3, 3, 3, 2, 2, 2, 3, 1] return: [1, 1]
[3,1,2,2,2,1,1,1,2,2,3,1,1,2,2,2,1,1,1,2,3] should return [3,1,3,2,3]
Time complexity should be better than O(n^2)
"""

def candy(arr):
    stack = []
    k = 0
    stack.append([arr[k],1])
    k += 1
    n = len(arr)
    print(stack)
    while k < n:
        if stack[-1][1] > n:
            break
        if arr[k] == stack[-1][0]:
            stack[-1][1] += 1
        else:
            if stack[-1][1] >= 3:
                #you can pop it
                stack.pop(-1)
            if arr[k] == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([arr[k],1])
        k += 1
        print(stack)
    print(stack)

candy([1, 3, 3, 3, 2, 2, 2, 3, 1])
print("---")
candy([3,1,2,2,2,1,1,1,2,2,3,1,1,2,2,2,1,1,1,2,3])