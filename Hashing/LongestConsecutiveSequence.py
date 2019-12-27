class Solution:
    def longestConsecutive(self, A: List[int]) -> int:
        s = set(A)
        A = list(s)
        if len(s)==0:
            return 0
        maxcount = 1
        i = 0
        while i < len(s):
            if A[i]-1 in s:
                # to verify that (i) is not a start element
                i += 1
            else:
                count = 1
                j = 1
                while A[i]+j in s:
                    count += 1
                    j += 1
                maxcount = max(maxcount, count)
                i += 1
        return maxcount

# LC 128 Hard
# Tags: Hashing

