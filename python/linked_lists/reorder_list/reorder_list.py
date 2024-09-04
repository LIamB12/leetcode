# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head): 

        if not head.next:
            return head

        # find midpoint
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # reverse second half
        prev.next = None
        prev = None
        curr = slow

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        second_head = prev

        #create new list
        dummy = ListNode()
        dummy_curr = dummy
        reversed_curr = second_head
        curr = head

        while curr and reversed_curr:
            dummy_curr.next = curr
            curr = curr.next
            dummy_curr.next.next = reversed_curr
            reversed_curr = reversed_curr.next
            dummy_curr = dummy_curr.next.next

        while curr:
            dummy_curr.next = curr
            curr = curr.next
            dummy_curr = dummy_curr.next
        while reversed_curr:
            dummy_curr.next = reversed_curr
            reversed_curr = reversed_curr.next
            dummy_curr = dummy_curr.next

        return dummy.next
