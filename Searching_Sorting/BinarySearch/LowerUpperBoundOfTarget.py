class Solution:   
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        n = len(nums)
        r = n-1
        while 1:
            if l > r:
                return [-1,-1]
            else:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid+1
                elif nums[mid] > target:
                    r = mid-1
                else:
                    break
        ans = [mid, mid]
        i = mid
        while nums[i] == target:
            ans[0] = i
            i -= 1
            if i<0:
                break
        i = mid
        while nums[i] == target:
            ans[1] = i
            i += 1
            if i>=n:
                break
        return ans
            

'''
# THIS METHOD WORKS TOO
import bisect as bs
class Solution:   
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(len(nums)==0):
            return [-1,-1]
        left = bs.bisect_left(nums, target)
        right = bs.bisect_right(nums, target)-1
        if(left == 0 and nums[left]!=target):
            left = -1
        if(left<len(nums) and nums[left]!=target):
            left = -1
        if(left == len(nums)):
            left = -1
        if(right <= 0 and nums[right]!=target):
            right = -1
        if(right == len(nums)):
            right = -1
        if(right<len(nums) and nums[right]!=target):
            right = -1
        return [left, right]
'''
