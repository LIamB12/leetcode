class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.lowest_common_ancestor = None
        self.traverseTreeAndCheckAncestry(root, p.val, q.val)
        
        if not self.lowest_common_ancestor:
            return root

        return self.lowest_common_ancestor

    def traverseTreeAndCheckAncestry(self, root, p, q):
        if not root:
            return

        if not self.lowest_common_ancestor and ((p <= root.val <= q) or (q <= root.val <= p)):
            self.lowest_common_ancestor = root

        self.traverseTreeAndCheckAncestry(root.left, p, q)
        self.traverseTreeAndCheckAncestry(root.right, p, q)
    
