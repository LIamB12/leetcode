# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):

        l1_curr, l2_curr = l1, l2

        power_of_ten = 0
        summ = 0

        while l1_curr and l2_curr:
            multiplier = 10 ** power_of_ten
            summ += (l1_curr.val * multiplier) + (l2_curr.val * multiplier)
            power_of_ten += 1
            l1_curr = l1_curr.next
            l2_curr = l2_curr.next

        while l1_curr:
            multiplier = 10 ** power_of_ten
            summ += (l1_curr.val * multiplier)
            power_of_ten += 1
            l1_curr = l1_curr.next

        while l2_curr:
            multiplier = 10 ** power_of_ten
            summ += (l2_curr.val * multiplier)
            power_of_ten += 1
            l2_curr = l2_curr.next

        string_val = str(summ)
        dummy_head = ListNode()
        curr = dummy_head

        for char in string_val[::-1]:
            node = ListNode(int(char))
            curr.next = node
            curr = curr.next

        return dummy_head.next



