# LC 381 HARD - https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/
from random import choice
class RandomizedCollection:

    def __init__(self):
        self.vals = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        self.vals.append(val)
        if val not in self.idx:
            self.idx[val] = set([])
        self.idx[val].add(len(self.vals)-1)
        return len(self.idx[val])==1


    def remove(self, val: int) -> bool:
        if val not in self.idx: 
            return False
        removeIdx = self.idx[val].pop()
        lastVal = self.vals[-1]
        prevIdx = len(self.vals)-1
        # swap the target idx with last value
        self.vals[removeIdx] = lastVal # swap the value
        self.vals.pop(-1) # remove last item from the list, since already copied

        # update the map for the last value that got swapped
        self.idx[lastVal].add(removeIdx)
        self.idx[lastVal].remove(prevIdx) # same as discard(prevIdx)

        if not self.idx[val]:
            del self.idx[val]
        return True

    def getRandom(self) -> int:
        return choice(self.vals)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
