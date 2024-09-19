class Solution:    
    def mergeKLists(self, lists):
        
        if len(lists) == 0:
            return None
        merged_list = lists[0]

        for new_list in lists[1:]:
            merged_list = Solution.merge2Lists(merged_list, new_list)

        return merged_list

    @staticmethod 
    def merge2Lists(list1, list2):

            l1 = list1
            l2 = list2

            dummy_head = ListNode()
            curr = dummy_head

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                    curr = curr.next
                else:
                    curr.next = l2
                    l2 = l2.next
                    curr = curr.next
            
            while l1:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            while l2:
                curr.next = l2
                l2 = l2.next
                curr = curr.next

            return dummy_head.next







