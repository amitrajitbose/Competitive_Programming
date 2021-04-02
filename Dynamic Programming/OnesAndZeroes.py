class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Bottom Up - Accepted
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for s in strs:
            c0, c1 = s.count('0'), s.count('1')
            for z in range(m, c0-1, -1):
                for o in range(n, c1-1, -1):
                    dp[z][o] = max(dp[z][o], dp[z-c0][o-c1] + 1)
        return dp[m][n]
        
        
    def findMaxFormTopDown(self, strs: List[str], m: int, n: int) -> int:
        # Leetcode gives TLE on this solution, although CPP is accepted
        dp = [[[0 for i in range(n+1)] for j in range(m+1)] for k in range(len(strs))]
        return self.calc(strs, 0, m, n, dp)
    
    def calc(self, strs, i, zeros, ones, dp):
        if i == len(strs):
            return 0
        if dp[i][zeros][ones]:
            return dp[i][zeros][ones]
        c0, c1 = strs[i].count('0'), strs[i].count('1')
        
        include = 0
        if (zeros-c0 >= 0 and ones-c1 >= 0):
            include = self.calc(strs, i+1, zeros-c0, ones-c1, dp) + 1
        exclude = self.calc(strs, i+1, zeros, ones, dp) + 0
        dp[i][zeros][ones] = max(include, exclude)
        return dp[i][zeros][ones]
