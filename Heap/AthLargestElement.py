import heapq
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        hp = []
        heapq.heapify(hp)
        res = []
        for val in B:
            if len(hp)==A and val < hp[0]:
                pass # when incoming element is less than Ath min element (root of heap)
            elif len(hp) == A:
                heapq.heappushpop(hp, val) # when incoming element will get inside top A elements
            else:
                heapq.heappush(hp, val) # when heap is undersized, less than A, we fill everything
            
            if len(hp) < A:
                res.append(-1)
            else:
                res.append(hp[0])
        return res

