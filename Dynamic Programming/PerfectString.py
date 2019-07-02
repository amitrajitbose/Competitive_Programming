"""
Alice and Bob are best friends. Today is Alice's birthday and Bob wants to gift her a perfect string. A perfect string is a string in 
which the absolute difference between adjacent characters is equal to 2, 3, or 4. For example, if the position of the characters 'd and
'g' is 4 and 7 respectively, then the absolute difference between their positions is 3. Bob has a normal string S which he has to 
convert to a perfect string so that he can gift it to Alice. Since her birthday is today, he wants to convert it into a perfect string
by using the minimum amount of time. The time to change one character to another takes the same amount of time that is equal to the 
absolute difference between the characters. 
Your task is to help Bob convert S into a perfect string by using the minimum amount of time. Note: The string contains all lowercase 
characters Input format The first and only line contains a string S. Output format Print the minimum changes that are required to modify
the string S into a perfect string. 

Constraint. 1 <= length of string <= 10^4 
-------------------------------------------------
sample input = abcdef 
sample output = 5 
Explanation
The string with minimum cost is "acaceg". The cost to convert "abcdef" to "acaceg" is 5. 
"""

from pprint import pprint
class Solution:
    def __init__(self):
        super().__init__()
    def solve(self, s: str, debug: bool) -> int:
        m = len(s)
        dp = []
        for i in range(26):
            dp.append([float('inf')]*m)
        
        for i in range(26):
            dp[i][0] = abs(ord(s[0]) - (ord('a')+i))
        
        possiblesteps = [-4, -3, -2, 2, 3, 4]
        for j in range(1,m):
            for i in range(26):
                for d in possiblesteps:
                    nextletter = i+d
                    if nextletter >= 0 and nextletter < 26:
                        cost = abs(ord(s[j]) - (ord('a')+nextletter))
                        dp[nextletter][j] = min(dp[nextletter][j], cost+dp[i][j-1])
        if debug:
            pprint(dp)
        minm = float('inf')
        for i in range(26):
            minm = min(minm, dp[i][-1])
        return minm

obj = Solution()
print(obj.solve('abcdef', debug=False))
print(obj.solve('ay', debug=True))