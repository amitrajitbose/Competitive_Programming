from heapq import heappush, heappop
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(start, -height, end) for start, end, height in buildings]
        # used negative heights as python maintains min heap, we need maxheap
        events.extend([(end, 0, 0) for _, end, _ in buildings])
        events.sort()
        res = [[0,0]] # point, height
        # print(events)
        
        maxheap = [(0, float("inf"))] # height, end position
        for start, negHt, end in events:
            # print(res,"<><><>", maxheap)
            while maxheap[0][1] <= start:
                # popping old entries, already seen
                heappop(maxheap)
            if negHt:
                # if it is the left/start of a building
                heappush(maxheap, (negHt, end))
            if res[-1][1] != -maxheap[0][0]:
                res.append([start, -maxheap[0][0]])
        res.pop(0)
        return res
