#LC1128
from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = defaultdict(int)
        for i,j in dominoes:
            if (i,j) in freq:
                freq[(i,j)] += 1
            else:
                freq[(j,i)] += 1
        pairs = 0
        for i in freq:
            pairs += (freq[i] * (freq[i] - 1)) // 2
        return pairs
