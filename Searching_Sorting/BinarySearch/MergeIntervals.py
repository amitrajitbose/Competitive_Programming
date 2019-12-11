# https://www.interviewbit.com/problems/merge-intervals/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        
        #intervals.append(new_interval)
        #intervals.sort(key=lambda x: x.start) # sorting not needed
        
        if len(intervals) == 0:
            return [new_interval]
        
        # inserting new interval in log(n) time
        low = 0
        high = len(intervals)
        if new_interval.start <= intervals[0].start:
            intervals.insert(0, new_interval)
        elif new_interval.start >= intervals[-1].start:
            intervals.append(new_interval)
        else:
            while low <= high:
                mid = (low + high) // 2
                if intervals[mid].start <= new_interval.start and intervals[mid+1].start > new_interval.start:
                    break
                elif intervals[mid].start > new_interval.start:
                    high = mid - 1
                else:
                    low = mid + 1
            intervals.insert(mid+1, new_interval)
        
        # merge in O(n) time
        merged = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i].start <= merged[-1].end:
                merged[-1].end = max(merged[-1].end, intervals[i].end) # merging action
            else:
                merged.append(intervals[i])
        return merged
