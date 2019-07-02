"""
Given a string S, find length of the longest substring with all distinct characters.  For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is String str.

Output:
Print length of smallest substring with maximum number of distinct characters.
Note: The output substring should have all distinct characters.

Constraints:
1 ≤ T ≤ 100
1 ≤ size of str ≤ 10000

Example:
Input:
5
abababcdefababcdab
geeksforgeeks
aewergrththy
aldshflasghdfasgfkhgasdfasdgvfyweofyewyrtyefgv
asdfasdfasdfasdf

Output:
6
7
4
10
4
"""

from collections import defaultdict as dict
for _ in range(int(input())):
    seenat = dict(int)
    s = str(input())
    maxlen = -float('inf')
    start = 0
    thislen = 0
    i = 0
    while i < len(s):
        if not s[i] in seenat:
            seenat[s[i]] = i
            thislen += 1
        else:
            thislen = 0 # start from this char
            start = seenat[s[i]]
            i = start
            del seenat # free up old array space
            seenat = dict(int) # creating new map
        maxlen = max(maxlen, thislen)
        i += 1
    print(maxlen)