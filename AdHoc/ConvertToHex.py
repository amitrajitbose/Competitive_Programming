class Solution:
    def toHex(self, num: int) -> str:
        val = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        if num < 0:
            num += (16**8)
        ans = ''
        res = num
        while res>=16:
            ans = val[res%16] + ans
            res = res // 16
        
        return val[res]+ans
    
    
    def toHexEasy(self, num: int) -> str:
        if num >= 0:
            return (hex(num))[2:]
        else:
            return hex((16**8)+num)[2:]