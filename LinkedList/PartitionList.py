# LC 86 - M [AMZN]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        less, more, lp, mp = None, None, None, None
        p = head

        while p:
            if p.val < x:
                if lp:
                    lp.next = p
                    lp = lp.next
                else:
                    less = p
                    lp = less
            else:
                if mp:
                    mp.next = p
                    mp = mp.next
                else:
                    more = p
                    mp = more
            p = p.next
        # join lists
        if lp and mp:
            lp.next = more
            mp.next = None
            return less
        elif not mp:
            return less
        elif not lp:
            return more
        
        
