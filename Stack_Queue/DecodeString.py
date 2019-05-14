# https://leetcode.com/problems/decode-string/

class Stack:
    def __init__(self):
        self.stack = []
    def __repr__(self):
        return ''.join(self.stack)
    def pushlist(self, x):
        self.stack.extend(x)
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop(-1)
    def isempty(self):
        return len(self.stack)==0
    def peek(self):
        return self.stack[-1]

class Solution:
    # Author : @amitrajitbose
    def decodeString(self, s: str) -> str:
        stack = Stack()
        for i in s:
            if i!=']':
                stack.push(i)
            else:
                x = stack.pop()
                tmp = ''
                val = ''
                while(x!='['):
                    tmp = x + tmp
                    x = stack.pop()

                while(not stack.isempty() and stack.peek().isdigit()):
                    x = stack.pop()
                    val = x + val
                stack.push(int(val) * tmp)
        return(repr(stack))
