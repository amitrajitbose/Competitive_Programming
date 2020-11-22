class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s += '#'
        t += '#'
        
        m, n = len(s), len(t)
        
        if abs(m-n) > 1:
            return False
        
        i, j, diff = 0, 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                diff += 1
                if diff > 1:
                    return False
                if m == n:
                    i += 1
                    j += 1
                if m > n:
                    i += 1
                if n > m:
                    j += 1
        
        return diff == 1
