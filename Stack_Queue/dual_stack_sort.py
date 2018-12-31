'''
@Challenge By : @iamriddhi

Sort a Stack

Given a stack, sort the elements inside that stack in ascending order using only push and pop operation. You can use one additional stack only.
For eg.

Input Stack :  5 (top)
               4
               3
               2
               1
Output Stack : 1 (top)
               2
               3
               4
               5
Input format :

Line 1 : No. of elements in stack

Line 2 : Stack elements (separated by space)

Sample Input
5
1 2 3 4 5
Sample Output
1 2 3 4 5
'''
class Stack(object):
	"""docstring for stack"""
	stack=[]
	def __init__(self, arr=[]):
		self.stack = arr[:]
	def push(self, x):
		self.stack.append(x)
	def pop(self):
		return self.stack.pop()
	def peek(self):
		return self.stack[-1]
	def len(self):
		return len(self.stack)

def printSorted(s, l):  
    mainstack = Stack()  
    tempstack = Stack()

    # append first number   
    mainstack.push(s[0]) 
    # iterate for all character in string  
    for i in range(1, l):
        a = s[i]
        b = mainstack.peek()
        # if greater or equal to top element  
        # then push to stack
        if(a>=b): 
            mainstack.push(s[i]) 
        # if smaller, then push all element  
        # to the temporary stack

        elif(b>a): 
            # push all greater elements 
            while(b>a):
                # push operation  
	            tempstack.push(mainstack.pop()) 
	            # push till the stack is not-empty  
	            if(mainstack.len()>0): 
	                b = mainstack.peek()
	            else: 
	                break
            # push the i-th character  
            mainstack.push(a) 
            # push the tempstack back to stack  
            while(tempstack.len()>0): 
                mainstack.push(tempstack.pop())
                  
    # return stack in reverse order  
    return mainstack.stack


n=int(input())
arr=[int(x) for x in input().strip().split()]
print(*printSorted(arr,n))
