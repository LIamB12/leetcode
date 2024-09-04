# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):

        if not head.next:
            return None
            
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        target = length - n
        if target == 0:
            return head.next
            
        curr = head
        prev = None
        for _ in range(target):
            prev = curr
            curr = curr.next

        
        if prev == None:
            return head
        prev.next = curr.next
        return head



