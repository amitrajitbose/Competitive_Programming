class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not(n & (n-1)) # and n to handle n=0
