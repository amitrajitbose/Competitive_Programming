# LC 759
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
from heapq import heappop, heapify
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        timestamp = []
        for emp in schedule:
            for t in emp:
                timestamp.append((t.start, 'S'))
                timestamp.append((t.end, 'E'))
        heapify(timestamp) # O(n)
        count = [[-1,0]]
        currCount = 0
        for i in range(len(timestamp)):
            val = heappop(timestamp) # log(n)
            diff = 1 if val[1] == 'S' else -1
            currCount += diff
            if count[-1][0] == val[0]:
                count[-1][1] = currCount
            else:
                count.append([val[0], currCount])
        print(count)
        res = []
        for i in range(1,len(count)-1):
            if count[i][1] == 0 and count[i+1][1] >= 1:
                # print(thisVal,count[thisVal], nextVal,count[nextVal])
                res.append(Interval(count[i][0], count[i+1][0]))
        return res
