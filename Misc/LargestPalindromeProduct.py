'''
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

 

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
'''


class Solution:

    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        maxlim = (10**n)-1
        minlim = 10**(n-1)
        for i in range(maxlim-1, maxlim//10, -1):
            u = int(str(i) + str(i)[::-1])
            j = maxlim
            while (j**2 >= u):
                if u % j == 0:
                    return u
                j -= 1
        return 0


print([Solution().largestPalindrome(i) for i in [1, 2, 3, 4, 5, 6, 7, 8]])
