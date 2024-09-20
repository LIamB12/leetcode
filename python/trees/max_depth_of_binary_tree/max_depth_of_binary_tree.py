from collections import deque


class Solution:
    def maxDepthIterativeDFS(self, root):
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 1

        while stack:
            node = stack.pop()
            max_depth = max(max_depth, node[1])
            if node[0].left:
                stack.append((node[0].left, node[1] + 1))
            if node[0].right:
                stack.append((node[0].right, node[1] + 1))

        return max_depth

    def maxDepthBFS(self, root):
        if not root:
            return 0
        
        q = deque()
        q.append(root)

        max_depth = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            max_depth += 1

        return max_depth

    def maxDepthRecursiveDFS(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        


