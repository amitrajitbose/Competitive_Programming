class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 :
            return 0
        minlen = n+1
        l = r = m = 0
        while(r < n):
            # keep adding from right end
            m += nums[r]
            if m >= s :
                # keep removing from left end
                while (m - nums[l]) >= s :
                    m -= nums[l]
                    l += 1
                minlen = min(minlen, r-l+1)
            r += 1
        if minlen > n:
            return 0
        return minlen
        
        
    def minSubArrayLen2(self, s: int, nums: List[int]) -> int:
        queue = []
        if(len(nums)==0):
            return 0
        queuesum = 0
        minlen = len(nums)
        idx = 0
        #print(queue)
        while(queuesum+nums[idx] < s):
            queue.append(nums[idx])
            queuesum += nums[idx]
            idx += 1
            if(idx >= len(nums)):
                return 0
            #print(queue)
        #print("----")
        while(idx < len(nums)):
            queue.append(nums[idx])
            queuesum += nums[idx]
            #print(queue)
            if(queuesum == s):
                minlen = min(minlen, len(queue))
                idx += 1
                continue
            while(queuesum > s):
                minlen = min(minlen, len(queue))
                pop = queue.pop(0)
                queuesum -= pop
                if(queuesum >= s):
                    minlen = min(minlen, len(queue))
                #print(queue)
            idx += 1
        return minlen
                
            
    def minSubArrayLen3(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        
        prefix = [nums[0]]
        for i in range(1,n):
            prefix.append(nums[i] + prefix[-1])
        
        low = 0
        high = 0
        # finding the first position
        while (prefix[high] < s):
            high += 1
            if high > n-1:
                return 0
        minlen = (high-low)+1
        if(high > n-1):
            return minlen
        
        while(low < high and high < n):
            #print(low,high)
            if (prefix[high] - prefix[low] < s):
                high += 1
            else:
                low +=1
            minlen = min(minlen, high-low+1)
        return minlen
            
