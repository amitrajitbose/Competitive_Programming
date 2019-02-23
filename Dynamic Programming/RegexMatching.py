"""
DCP #25

This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
"""

class Solution:
    def __init__(self):
        self.memoize = dict()
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        if len(p) == 0:
            return len(s) == 0
        ques = s + "+" + p
        if(ques in self.memoize):
            return self.memoize[ques]
        #Recording if the first character satisfied
        firstMatch = len(s) > 0 and (p[0] == s[0] or p[0] == '.')
        #Proceeding to check next character
        if len(p) > 1 and p[1] == '*':
            if firstMatch:
                res = self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                res = self.isMatch(s, p[2:])
        else:
            res = firstMatch and self.isMatch(s[1:], p[1:])
        self.memoize[ques] = res
        return res

def main():
	obj = Solution()
	assert obj.isMatch('ray','ra.')==True
	assert obj.isMatch('raymond','ra.')==False
	assert obj.isMatch('chat','.*at')==True
	assert obj.isMatch('chats','.*at')==False
	print ("Passed All Test Cases...")

main()
