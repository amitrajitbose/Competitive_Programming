# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if not A:
            return None
        slow, fast = A, A
        while True:
            if not slow or not fast or not fast.next:
                return None # no loop present
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        # getting start of loop
        # get length of cycle
        n = 1
        slow = slow.next
        while slow != fast:
            slow = slow.next
            n += 1
        slow = A
        fast = A
        for i in range(n):
            fast = fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
