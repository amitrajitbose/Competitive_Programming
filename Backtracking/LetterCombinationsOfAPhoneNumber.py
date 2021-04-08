class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        self.pad = [
            [], [],
            ['a','b','c'],
            ['d','e','f'],
            ['g','h','i'],
            ['j','k','l'],
            ['m','n','o'],
            ['p','q','r','s'],
            ['t','u','v'],
            ['w','x','y','z']
        ]

        self.res = []
        self.dfs(list(digits))
        return self.res
        
    def dfs(self, digits, patt = "", idx = 0):
        if len(digits) == idx:
            self.res.append(patt)
        else:
            x = int(digits[idx])
            for ch in self.pad[x]:
                self.dfs(digits, patt + ch, idx + 1)
