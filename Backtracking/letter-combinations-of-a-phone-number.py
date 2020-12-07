class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        res = []
        # this is the backtracking part
        def calc(comb: str, nextdigits: str) -> None:
            if len(nextdigits) == 0:
                res.append(comb) # base condition
            else:
                for ch in numpad[nextdigits[0]]:
                    calc(comb + ch, nextdigits[1:]) # recurse
        if len(digits) > 0:
            calc("", digits)
        return res
