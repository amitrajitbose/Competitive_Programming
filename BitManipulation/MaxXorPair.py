#LC 421
from math import log2, floor
class TrieNode:
    def __init__(self):
        self.left = None
        self.right = None
        
def insert(head, n, maxbit):
    if not head:
        return None
    curr = head
    for i in range(maxbit - 1, -1, -1):
        bit = (n >> i) & 1
        # left = 0, right = 1
        if bit:
            if not curr.right:
                curr.right = TrieNode()
            curr = curr.right
        else:
            if not curr.left:
                curr.left = TrieNode()
            curr = curr.left
    return head
                
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        try:
            maxbit = floor(log2(max(nums))) + 1
        except:
            maxbit = 0
        head = TrieNode()
        for n in nums:
            head = insert(head, n, maxbit)
        
        maxXor = -float('inf')
        for n in nums:
            currXor = 0
            curr = head
            for i in range(maxbit - 1, -1, -1):
                bit = (n>>i) & 1
                # if bit is set, try to unset it to get max pair
                if bit:
                    if curr.left:
                        currXor += 2**i
                        curr = curr.left
                    else:
                        curr = curr.right
                else:
                    if curr.right:
                        currXor += 2**i
                        curr = curr.right
                    else:
                        curr = curr.left
            maxXor = max(maxXor, currXor)
        return maxXor

