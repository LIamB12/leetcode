# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        l1_curr = list1
        l2_curr = list2
        dummy = ListNode()
        sorted_curr = dummy

        while l1_curr and l2_curr:

            if l1_curr.val < l2_curr.val:

                sorted_curr.next = l1_curr
                l1_curr = l1_curr.next
                sorted_curr = sorted_curr.next

            else:
                sorted_curr.next = l2_curr
                l2_curr = l2_curr.next
                sorted_curr = sorted_curr.next


        while l1_curr:
            sorted_curr.next = l1_curr
            l1_curr = l1_curr.next
            sorted_curr = sorted_curr.next

        while l2_curr:
            sorted_curr.next = l2_curr
            l2_curr = l2_curr.next
            sorted_curr = sorted_curr.next

        return dummy.next
