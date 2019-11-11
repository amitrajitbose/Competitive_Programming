# LCH164

class Bucket:
    def __init__(self):
        self.low = float('inf')
        self.high = -float('inf')
        self.empty = True
    def add(self, item):
        self.low = min(self.low, item)
        self.high = max(self.high, item)
        self.empty = False
    def __repr__(self):
        return ''.join(['(',str(self.low),',',str(self.high),')'])

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        maxi = max(nums)
        mini = min(nums)
        if n == 2:
            return maxi-mini
        bucketsize = max(((maxi-mini)//(n-1)), 1)
        bucketNum = ((maxi-mini)//bucketsize)+1
        buckets = [Bucket() for i in range(bucketNum)]
        for i in nums:
            idx = (i-mini)//bucketsize
            buckets[idx].add(i)
        #print(buckets)
        maxgap = 0
        prevBucketMax = mini
        for i in buckets:
            if i.empty:
                continue
            maxgap = max(maxgap, i.low-prevBucketMax)
            prevBucketMax = i.high
        return maxgap
