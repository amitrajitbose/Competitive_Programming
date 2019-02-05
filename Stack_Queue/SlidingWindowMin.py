from collections import deque as Queue

def slider(arr,k):
    n=len(arr)
    q=Queue()

    #from the first k elements keep the max and decreasing
    for i in range(k):
        while(len(q) and arr[i]<=arr[q[-1]]):
            q.pop()
        q.append(i)
    for i in range(k,n):
        #previous window min
        print(arr[q[0]],end=" ")
        #if any element does not belong to this window we pop the,
        while(len(q) and q[0]<=i-k):
            #this index does not belong to this window
            q.popleft()
        #remove all smaller elements
        curr=arr[i]
        while(len(q) and curr<=arr[q[-1]]):
            q.pop()
        q.append(i)
    print(arr[q[0]])

slider([10, 5, 2, 7, 8, 7],3)
slider([2, 10, 5, 7, 7, 8],3)
slider([10,0,3,2,5],2)