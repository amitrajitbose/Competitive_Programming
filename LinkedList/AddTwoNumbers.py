# 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        dummy = ListNode(0)
        p3 = dummy
        carry = 0
        while p1 or p2:
            if p1 and p2:
                s = p1.val + p2.val + carry
                carry = 0
                if s > 9:
                    carry = 1
                    s = s % 10
                p3.next = ListNode(s)
                p1 = p1.next
                p2 = p2.next
            elif p1:
                s = p1.val + carry
                carry = 0
                if s > 9:
                    carry = 1
                    s = s % 10
                p3.next = ListNode(s)
                p1 = p1.next
            elif p2:
                s = p2.val + carry
                carry = 0
                if s > 9:
                    carry = 1
                    s = s % 10
                p3.next = ListNode(s)
                p2 = p2.next
            p3 = p3.next
        if carry == 1:
            p3.next = ListNode(carry)
        return dummy.next

