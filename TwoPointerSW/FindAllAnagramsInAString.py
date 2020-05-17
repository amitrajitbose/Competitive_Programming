# 438

from collections import Counter

class SlidingHash:
    def __init__(self, initialData = []):
        self.window = Counter(initialData)
    def __eq__(self, other):
        return self.window == other
    def remove(self, item):
        if self.window[item] == 1:
            del self.window[item]
        else:
            self.window[item] -= 1
    def put(self, item):
        if item in self.window:
            self.window[item] += 1
        else:
            self.window[item] = 1

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(list(p))
        low, high = 0, len(p)-1
        window = SlidingHash(list(s[low : high + 1]))
        res = []
        while high < len(s)-1:
            if window == target:
                res.append(low)
            window.remove(s[low])
            low += 1
            high += 1
            window.put(s[high])
        if window == target:
            res.append(low)
        return res

