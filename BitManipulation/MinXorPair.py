from math import floor, log2
class TrieNode:
    def __init__(self):
        self.child = [None] * 2
        self.value = None
class Trie:
    def __init__(self):
        self.root = self.getNewNode() # constructor
    def getRoot(self):
        return self.root
    def getNewNode(self):
        return TrieNode()
    def insert(self, n, maxbits):
        # insert value n into trie
        curr = self.getRoot()
        for i in range(maxbits-1, -1, -1):
            bit = (n >> i) & 1
            if not curr.child[bit]:
                curr.child[bit] = self.getNewNode()
            curr = curr.child[bit]
        curr.value = n
        
    def xorUtil(self, key, maxbits):
        # traverse the trie and xor with the most similar element
        curr = self.getRoot()
        for i in range(maxbits-1, -1, -1):
            bit = (key >> i) & 1
            if curr.child[bit]:
                curr = curr.child[bit]
            elif curr.child[1 - bit]:
                curr = curr.child[1 - bit]
        return curr.value ^ key

def minXor(arr):
    m = 2**31
    maxbits = floor(log2(max(arr))) + 1
    trie = Trie()
    trie.insert(arr[0], maxbits)
    arr.pop(0)
    for i in arr:
        m = min(m, trie.xorUtil(i, maxbits))
        trie.insert(i, maxbits)
    return m
    
class Solution:
    def findMinXor(self, nums):
        return minXor(nums)

