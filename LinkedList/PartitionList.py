# LC 86 - M [AMZN]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less = more = None
        lesshead = morehead = None
        if not head:
            return head
        if head.val < x :
            less = lesshead = head
            head = head.next
            while(head):
                if head.val < x :
                    less.next = head
                    less = less.next
                else:
                    more = morehead = head
                    head = head.next
                    break
                head = head.next
                
        else:
            more = morehead = head
            head = head.next
            while(head):
                if head.val >= x :
                    more.next = head
                    more = more.next
                else:
                    less = lesshead = head
                    head = head.next
                    break
                head = head.next

        while(head):
                if head.val >= x:
                    more.next = head
                    more = more.next
                else:
                    less.next = head
                    less = less.next
                head = head.next
        
        if more:
            more.next = None
        if less:
            less.next = morehead
            return lesshead
        else:
            return morehead
