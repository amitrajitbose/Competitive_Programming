'''
The problem was asked by Google
Given a stack of N elements, interleave the first half of it with the second half 
but reversed, using one and only one other queue. This should be done in-place.
You can only push and pop from stack, enqueue and dequeue from queue.
Ex: [1,2,3,4,5] -> [1,5,2,4,3]
Ex: [1,2,3,4]   -> [1,4,2,3]
'''
from collections import deque
def interleave(st):
	n=len(st)
	if(n<=1):
		return st
	q=deque([]) #initialise empty queue
	for _ in range(n-1):
		q.append(st.pop(-1))
	st.append(q.popleft())
	while(len(q)>=2):
		q.rotate()
		st.append(q.popleft())
		st.append(q.popleft())
	if(len(q)>0):
		st.append(q.popleft())
	return(st)

# Test Cases
assert interleave([1,2,3,4,5])==[1,5,2,4,3]
assert interleave([1,2,3,4,5,6,7])==[1,7,2,6,3,5,4]
assert interleave([1,2,3,4])==[1,4,2,3]
assert interleave([1,2,3,4,5,6])==[1,6,2,5,3,4]
assert interleave([])==[]
assert interleave([1])==[1]
assert interleave([1,2])==[1,2]
assert interleave([1,2,3])==[1,3,2]

