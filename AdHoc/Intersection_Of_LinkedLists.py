'''
DCP #20

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. 
The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

Further ref: https://leetcode.com/problems/intersection-of-two-linked-lists/

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getLength(self, head):
        count = 0
        while(head):
            count += 1
            head = head.next
        return count
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        diff = abs(lenA - lenB)
        if(lenB > lenA):
            headA, headB = headB, headA
        """
        now we can safely assume list A to be >= list B in terms of length
        """
        for i in range(diff):
            if(not headA):
                return None
            headA = headA.next
        while(headA and headB):
            if(headA == headB):
                return headA
            headA = headA.next
            headB = headB.next
        return None