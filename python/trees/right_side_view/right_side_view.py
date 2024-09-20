from collections import deque


class Solution:
    def rightSideView(self, root):
        if not root: 
            return []

        q = deque()
        q.append(root)
        right_side_nodes = []

        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

                if i == level_length - 1:
                    right_side_nodes.append(node.val)
        return right_side_nodes





