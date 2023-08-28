# https://leetcode.com/problems/employee-free-time/description/
# LC 759 HARD
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        timestamp = []
        for emp in schedule:
            for t in emp:
                timestamp.append((t.start, 'S'))
                timestamp.append((t.end, 'E'))
        # compression of timestamps
        timestamp.sort(key=lambda x: x[0])
        count = {}
        currCount = 0
        for i in timestamp:
            diff = 1 if i[1] == 'S' else -1
            currCount += diff
            count[i[0]] = currCount
        # print(count)
        keys = sorted(count.keys())
        res = []
        for i in range(len(keys)-1):
            thisVal = keys[i]
            nextVal = keys[i+1]
            if count[thisVal] == 0 and count[nextVal] >= 1:
                # print(thisVal,count[thisVal], nextVal,count[nextVal])
                res.append(Interval(thisVal, nextVal))
        return res
