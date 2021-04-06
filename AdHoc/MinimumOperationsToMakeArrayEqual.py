# https://leetcode.com/problems/minimum-operations-to-make-array-equal/
class Solution:
    def minOperations(self, n: int) -> int:
        """
        Approach and thought:
        
        1) Given an n, I can find out last number = 2(n-1) + 1
        2) Sum of array = 1-1, 2-4, 3-9, 4-16, 5-25, 6-36 ... = n^2
        3) Target value for all elements = n^2 / n = n
        4) Iterate till half length and get the sum of all differences between n and A[i]
        
        Linear Time solution below:
        """
        # moves = 0
        # for i in range(n//2):
        #     moves += n-((2*i)+1)
        # return moves
        """
        Follow up thought:
        
        This is dependent on n. So there must be a pattern.
        Essentially, we are finding out the sum of first half elements.
        Then we are subtracting it from n/2 times n. So, it is (n*(n/2)) - (sum of first half)
        
        We can calculate the sum of first half elements directly!
        How?
        To calculate sum of first n odd numbers we do n^2
        So to calculate sum of first n/2 odd numbers (that is first half)
        We have to do (n/2)^2 = (n^2)/4
        
        So the final formula is ((n*n)/2 - (n*n)/4) = (n*n)/4
        
        Constant Time Solution:
        """
        #return (n*n)//4
        return (n*n) >> 2 # faster way to perform the above line
