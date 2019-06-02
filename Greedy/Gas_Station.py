class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        rem = 0 #remaining gas in tank
        cos = 0 #cost to go to next stop
        start = 0
        prev = 0
        debug = False
        while start < n and start >= prev:
            if debug:
                print("Start at",start)
            i = start
            rem = gas[i]
            cos = cost[i]
            if debug:
                print(rem)
            i = (i + 1) % n
            while i<n:
                if debug:
                    print("Goto",i)
                if(cos > rem):
                    if i == start:
                        return -1
                    prev = start
                    start = i
                    break
                rem += (gas[i] - cos)
                cos = cost[i]
                i = (i + 1) % n
                if debug:
                    print(rem)
                if i == start and rem>=cos:
                    return start
        return -1

