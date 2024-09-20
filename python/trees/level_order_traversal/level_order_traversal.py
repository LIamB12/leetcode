from collections import deque


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        q = deque()
        q.append(root)

        levels = []

        while q:
            current_level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                current_level.append(node.val)

            levels.append(current_level)
        return levels
