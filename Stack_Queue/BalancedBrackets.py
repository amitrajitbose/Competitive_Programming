'''
DCP #27
Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
'''
class Solution(object):
    def __init__(self):
        self.lookup = {
        '}':'{',
        ']':'[',
        ')':'('
        }
    def checkBalance(self, string):
        if(len(string)==0):
            return True
        if(len(string)%2):
            return False
        arr = list(string.strip())
        stack = []
        stack.append(arr.pop(0))
        while(len(arr)>0):
            curr = arr.pop(0)
            if(curr in self.lookup and self.lookup[curr]==stack[-1]):
                stack.pop(-1)
            else:
                stack.append(curr)
        if(len(stack)==0):
            return True
        else:
            return False

#testcases
sol = Solution()
assert sol.checkBalance('([])[]({})')==True
assert sol.checkBalance('([])[]({}){}[()]')==True
assert sol.checkBalance('([)][}')==False
assert sol.checkBalance('((()')==False
assert sol.checkBalance('[])')==False
assert sol.checkBalance('')==True
