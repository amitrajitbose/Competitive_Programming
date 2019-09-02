class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = [int(i) for i in list(str(num))]
        maxd = arr[0]
        n = len(arr)
        noDip = True
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                noDip = False
                break
        if noDip:
            return num
        
        dropIndex = -1
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                dropIndex = i-1
                break
        maxd = 0
        maxindex = 0
        for i in range(dropIndex, n):
            if arr[i] >= maxd:
                maxd = arr[i]
                maxindex = i
        
        for i in range(0, dropIndex):
            if maxd > arr[i]:
                dropIndex = i
                break
                
        #print(dropIndex, maxindex)
        arr[dropIndex], arr[maxindex] = arr[maxindex], arr[dropIndex]
        arrstr = [str(i) for i in arr]
        return ''.join(arrstr)
        
"""
Inputs

32526
6357588
975537
3774616
43892634
"""
