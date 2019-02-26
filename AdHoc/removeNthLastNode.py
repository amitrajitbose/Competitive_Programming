'''
DCP #26

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        rear = head;
        prevrear = head;
        front = head;
        for i in range(n):
            front = front.next
        
        while(front):
            front = front.next
            prevrear = rear
            rear = rear.next
        
        # when n is equal to the length of the list
        if(not front and rear==head):
            return head.next
        
        #removing the node at rear
        prevrear.next = rear.next
        return head
