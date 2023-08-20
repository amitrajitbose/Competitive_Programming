# https://leetcode.com/problems/happy-number/description/
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set([n])
        n = self.getNext(n)
        while n != 1 and n not in visited:
            visited.add(n)
            n = self.getNext(n)
        return n == 1
    def getNext(self, n):
        res = 0
        while n>0:
            res = res + ((n%10)**2)
            n = n // 10
        return res
