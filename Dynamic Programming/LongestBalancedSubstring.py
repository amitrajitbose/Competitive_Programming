'''
Given a string S made up of multiple brackets of type "<>" , "[]" , "()" and "{}" find the length of the longest substring which forms a balanced string . 
Conditions for a string to be balanced : 
1) Blank string is balanced ( However blank string will not be provided as a test case ). 
2) if B is balanced : (B) , [B] , {B} and <B> are also balanced. 
3) if B1 and B2 are balanced then B1B2 i.e the string formed by concatenating B1 and B2 is also balanced. 
Your function will get exactly one argument which would represent the string S.
Your function should return an integer corresponding to the answer. 

Constraints :
0 <= length(S) <= 1000000

Sample Test Case :

Input : <<<<>
Output : 2 

'''

class Solution:
    def getClosing(self,s):
        return {'{':'}', '[':']', '<':'>', '(':')'}[s]
    def getOpening(self,s):
        return {'}':'{', ']':'[', '>':'<', ')':'('}[s]
    def LBSlength(self, s):
        maxlen = 0
        dp = [0] * len(s)
        openb = ['[', '{', '(', '<']
        closeb = [']', '}', ')', '>']
        for i in range(1,len(s)):
            if s[i] in closeb:
                if s[i-1] == self.getOpening(s[i]):
                    dp[i] = (dp[i-2] if i>=2 else 0) + 2 # found "()" sequence
                elif (i-dp[i-1] > 0 and s[i-dp[i-1]-1]==self.getOpening(s[i])):
                    # found sequence for "(...)"
                    if (i-dp[i-1] >=2):
                        dp[i] = dp[i-1] + dp[i-dp[i-1]-2]+2
                    else:
                        dp[i] = dp[i-1] + 2
                maxlen = max(maxlen, dp[i])
        return maxlen

