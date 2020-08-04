#LCH-23
from heapq import heappush, heappop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, listNode):
        self.node = listNode
    def getNode(self):
        return self.node
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        h = []
        for i in lists:
            if i:
                heappush(h, NodeWrapper(i))

        dummy = ListNode()
        ptr = dummy
        
        while len(h):
            nextelem = heappop(h)
            ptr.next = nextelem.getNode()
            ptr = ptr.next
            
            if nextelem.getNode().next:
                heappush(h, NodeWrapper(nextelem.getNode().next))
            
        return dummy.next
