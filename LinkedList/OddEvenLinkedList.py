# 328
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        odd = head
        even = head.next
        evenStarts = head.next
        while True:
            if not odd or not even or not even.next:
                odd.next = evenStarts
                break
            # connecting odd nodes
            odd.next = even.next
            odd = even.next
            
            if not odd.next:
                even.next = None
                odd.next = evenStarts
                break
            # connecting even nodes
            even.next = odd.next
            even = odd.next
        return head

