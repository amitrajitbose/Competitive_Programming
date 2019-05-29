# LC - 20
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {']':'[', '}':'{', ')':'('}
        flag = True
        for i in s:
            if i in ['[','{','(']:
                stack.append(i)
            else:
                if len(stack) and hmap[i] == stack[-1]:
                    stack.pop(-1)
                else:
                    flag = False
                    break
        return flag and len(stack)==0
