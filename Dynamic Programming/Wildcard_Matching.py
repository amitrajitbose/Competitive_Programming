# LC 44 [Hard]

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns, np = len(s), len(p)
        cache = [[False]*(ns+1) for i in range(np+1)]
        
        # Empty pattern matches empty string
        cache[0][0] = True
        
        # Even empty string should match *
        if len(p) and p[0] == '*':
            for i in range(len(p)):
                if p[i] == '*':
                    cache[i+1][0] = cache[i][0]
        
        for i in range(np):
            for j in range(ns):
                if  p[i]==s[j] or p[i]=='?':
                    cache[i+1][j+1] = cache[i][j] 
                elif p[i]=='*':
                    cache[i+1][j+1]=cache[i+1][j] or cache[i][j+1]
        #print(cache)
        return cache[np][ns]
