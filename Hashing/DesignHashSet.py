#LCE 705
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = [set([])] * 1001
        

    def add(self, key: int) -> None:
        self.mem[key % 1001].add(key)
        

    def remove(self, key: int) -> None:
        if key in self.mem[key % 1001]:
            self.mem[key % 1001].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.mem[key % 1001]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
