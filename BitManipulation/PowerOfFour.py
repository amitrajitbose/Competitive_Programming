import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n == (4 ** (math.log2(n) // 2))
