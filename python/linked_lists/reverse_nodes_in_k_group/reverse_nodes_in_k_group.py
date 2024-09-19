class Solution:
    def reverseKGroup(self, head, k):
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        curr = head

        dummy_head = ListNode()
        prev_tail = dummy_head

        for _ in range(length // k):
            prev = None
            group_head = curr
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            prev_tail.next = prev
            prev_tail = group_head

        if curr:
            prev_tail.next = curr

        return dummy_head.next
