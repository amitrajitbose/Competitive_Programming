# LCH 4
# Python 3 Code
# Ref: https://youtu.be/LPFhl65R7ww
class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        if len(arr1) > len(arr2):
            return self.findMedianSortedArrays(arr2, arr1)
        x, y = len(arr1), len(arr2)
        low, high = 0, x
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = ((x + y + 1) // 2) - partitionX
            
            '''
            arr1 = ....a | b ......
            arr2 = ....... c | d ..
            '''
            a = float('-inf') if partitionX == 0 else arr1[partitionX-1]
            b = float('inf') if partitionX == x else arr1[partitionX]
            c = float('-inf') if partitionY == 0 else arr2[partitionY-1]
            d = float('inf') if partitionY == y else arr2[partitionY]
            
            if a<=d and c<=b:
                # correct partitioning occured
                # let us find median now
                # if even length total
                if (x+y)%2 == 0:
                    return (max(a,c) + min(b,d))/2 #float(2) for Python2.7
                else:
                    return max(a,c)
            elif a>d:
                # median would be towards left
                high = partitionX - 1
            elif c>b:
                # median would be towards right
                low = partitionX + 1
        raise Exception("Control Should Not Be Here")
