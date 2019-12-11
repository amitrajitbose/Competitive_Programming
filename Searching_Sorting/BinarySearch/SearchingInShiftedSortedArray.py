'''
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.

Explain your solution and analyze its time and space complexities.
'''

'''
7 8 9 1 2 3 4 5 6
'''
class Solution:
    # Author : Amitrajit Bose
    def findOffset(self, arr):
        # O(log n)
        low = 0
        high = len(arr) - 1
        if(arr[0] <= arr[-1]):
            return 0
        while(low <= high):
            mid = (low+high)//2
            #print(low,mid,high)
            if(arr[low]>arr[mid] and arr[mid]<arr[high]):
                high = mid
            elif(arr[low]<arr[mid] and arr[mid]>arr[high]):
                low = mid
            elif(high-low == 1):
                return low+1
    def binarySearch(self, arr, num, shift):
        # O(log n)
        lth = len(arr)
        low = 0
        high = lth-1
        while(low <= high):
            mid = (low + high)//2
            #print(low,mid,high)
            if(arr[(mid+shift)%lth] == num):
                return (mid+shift)%lth
            elif(num > arr[(mid+shift)%lth]):
                low = mid+1
            elif(num < arr[(mid+shift)%lth]):
                high = mid-1
        return -1
    def findIdx(self, arr, num):
        return self.binarySearch(arr, num, self.findOffset(arr))


print(Solution().findIdx([7,8,9,1,2,3,4],4))
print(Solution().findIdx([2],2))