class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        idx = [0]*len(row)
        for i in range(len(row)):
            idx[row[i]] = i
        swaps = 0
        # print(row)
        for i in range(0, len(row), 2):
            if row[i+1] != (row[i] ^ 1):
                swaps += 1
                
                t = idx[row[i]^1]
                
                # updating idx map
                idx[row[i]^1] = i+1
                idx[row[i+1]] = t
                
                # swapping
                row[i+1], row[t] = row[t], row[i+1]
                
                # print(row)
        return swaps
