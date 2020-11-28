# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heads = []
        for i,node in enumerate(lists):
            if node:
                heappush(heads, (node.val, i, node)) # value, sequence, node ref
        newlist = ptr = ListNode(0)
        while heads:
            _v, _s, cur = heappop(heads)
            ptr.next = cur
            if cur.next:
                heappush(heads, (cur.next.val, _s, cur.next))
            ptr = ptr.next
        return newlist.next
