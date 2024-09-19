class Solution:
    def copyRandomList(self, head):
        mp = {}
        
        curr = head
        while curr:
            node_copy = Node(curr.val)
            mp[curr] = node_copy
            curr = curr.next

        for original_node, copy in mp.items():
            copy.next = mp.get(original_node.next, None)
            copy.random = mp.get(original_node.random, None)

        return mp.get(head)

