# LC 462
#from statistics import median
from random import randrange
from math import floor
class Solution:
    #Quick Select Algorithm
    def partition(self,x, pivot_index = 0):
        i = 0
        if pivot_index !=0: x[0],x[pivot_index] = x[pivot_index],x[0]
        for j in range(len(x)-1):
            if x[j+1] < x[0]:
                x[j+1],x[i+1] = x[i+1],x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        return x,i

    def RSelect(self,x,k):
        if len(x) == 1:
            return x[0]
        else:
            xpart = self.partition(x,randrange(len(x)))
            x = xpart[0] # partitioned array
            j = xpart[1] # pivot index
            if j == k:
                return x[j]
            elif j > k:
                return self.RSelect(x[:j],k)
            else:
                k = k - j - 1
                return self.RSelect(x[(j+1):], k)
    
    def median(self,lst):
        lstLen = len(lst)
        index = (lstLen - 1) // 2
        if (lstLen % 2):
            return self.RSelect(lst,index)
        else:
            return (self.RSelect(lst,index) + self.RSelect(lst,index+1))/2.0

    def sorting_median(self,lst):
        lstLen = len(lst)
        lst.sort()
        index = (lstLen - 1) // 2
        if (lstLen % 2):
            return lst[index]
        else:
            return (lst[index] + lst[index+1])/2.0
    
    def minMoves2(self, nums: List[int]) -> int:
        mdn = floor(self.sorting_median(nums))
        movesmdn = 0
        for i in nums:
            movesmdn += abs(i-mdn)
        return movesmdn
