# LC24
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, h1, h2, newhead = None, head, head.next, head.next
        
        while h1 and h2:
            if prev:
                prev.next = h2
            nxt = h2.next
            h2.next = h1
            prev = h1
            if nxt:
                h1 = nxt
                h2 = nxt.next
                prev.next = nxt
            else:
                prev.next = None
                break
        return newhead
