# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = head.next
        ptr = head
        prev = None
        while ptr:
            if ptr.next:
                tmp = ptr.next.next
                ptr.next.next = ptr
                if prev:
                    prev.next = ptr.next
                ptr.next = tmp
                prev = ptr
                ptr = tmp
            else:
                return newhead
        return newhead
 
