class Solution:
    def goodNodes(self, root):
        self.good_nodes = 0
        self.traverseTreeAndCountGoodNodes(root, root.val)
        return self.good_nodes

    def traverseTreeAndCountGoodNodes(self, root, maxVal):
        if not root:
            return

        if root.val >= maxVal:
            maxVal = root.val
            self.good_nodes += 1

        self.traverseTreeAndCountGoodNodes(root.left, maxVal)
        self.traverseTreeAndCountGoodNodes(root.right, maxVal)

