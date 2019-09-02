class MyHashMap:
    def __init__(self, cap = 10**3):
        """
        Initialize your data structure here.
        """
        self.MAXSIZE = cap
        self.map = [[] for i in range(self.MAXSIZE)]
        
    def hashCode(self, key):
        return hash(str(key)) % self.MAXSIZE

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = self.hashCode(key)
        leng = len(self.map[idx])
        if leng == 0:
            self.map[idx].append((key, value)) # add first
            
        else:
            found = False
            for i in range(leng):
                if self.map[idx][i][0] == key:
                    self.map[idx][i] = (key, value) # update
                    found = True
            if not found:
                self.map[idx].append((key, value)) # chaining
                
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = self.hashCode(key)
        leng = len(self.map[idx])
        if leng == 0:
            return -1
        else:
            for i in range(leng):
                if self.map[idx][i][0] == key:
                    return self.map[idx][i][1] # value
            return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = self.hashCode(key)
        leng = len(self.map[idx])
        if leng <= 0:
            return None
        else:
            for i in range(leng):
                if self.map[idx][i][0] == key:
                    self.map[idx].remove(self.map[idx][i])
                    return None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

