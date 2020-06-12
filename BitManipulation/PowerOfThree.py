threePow19 = 1162261467 # 3**19
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n>0 and not (threePow19 % n)
