class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        i = 0
        j = k-1
        out = []
        n = len(arr)
        if n==0:
            return []
        if n <= k:
            return [max(arr)]
        # Create the heap and heapify 
        heap = arr[i:j + 1] 
        heapq._heapify_max(heap) 

        # Print the maximum element from  
        # the first window of size k 
        out.append(heap[0])
        last = arr[i] 
        i+= 1
        j+= 1
        nexts = arr[j] 

        # For every remaining element 
        while j < n: 

            # Add the next element of the window 
            heap[heap.index(last)] = nexts 

            # Heapify to get the maximum  
            # of the current window 
            heapq._heapify_max(heap) 

            # Print the current maximum 
            out.append(heap[0])
            last = arr[i] 
            i+= 1
            j+= 1
            if j < n: 
                nexts = arr[j]
        return out
