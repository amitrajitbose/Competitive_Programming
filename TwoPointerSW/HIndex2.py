#LCM275
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def binSearch(low: int, high: int) -> int:
            mid = (low + high) // 2
            #print(low,mid,high)
            if mid < 1 or mid > len(citations) or low>high:
                return -1
            if citations[-mid] >= mid:
                return max(mid, binSearch(mid+1, high))
            else:
                return binSearch(low, mid-1)
        
        if len(citations) == 0:
            return 0
        
        if len(citations) == 1:
            return 1 if citations[-1] >= 1 else 0
        
        return max(0, binSearch(1, len(citations)+1))

