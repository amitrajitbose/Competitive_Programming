class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low,mid,high = 0,0,len(arr)-1
        while(mid <= high):
            if arr[mid] == 2:
                arr[mid],arr[high] = arr[high],arr[mid]
                high -= 1
            elif arr[mid] == 0:
                arr[mid],arr[low] = arr[low], arr[mid]
                low += 1
                mid += 1
            else:
                mid += 1
