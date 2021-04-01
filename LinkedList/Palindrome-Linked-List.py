# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prevn, currn, nextn = None, head, head.next
        head.next = None
        head = nextn
        while (nextn):
            prevn = currn
            currn = nextn
            nextn = head.next
            currn.next = prevn #reversing the link
            head = nextn
        return currn
    
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        prevSlow, slow, fast = None, head, head
        while fast and fast.next:
            prevSlow = slow
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            # odd len list, slow at mid, just before start of second list
            secondStart = self.reverse(slow.next)
            # ignored middle element (pointed by slow)
        else:
            # even len list, slow is at start of second list
            secondStart = self.reverse(slow)
        prevSlow.next = None
    
        a, b = head, secondStart
        while a and b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return True
