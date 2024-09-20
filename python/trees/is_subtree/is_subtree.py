class Solution:   
    def isSubtree(self, root, subRoot):
        self.contains_subtree = False
        self.traverseTreeAndCheckSubtree(root, subRoot)
        return self.contains_subtree


    def isSameTree(self, p, q):
        if not p and not q:
            return

        if not p or not q:
            self.is_same = False
            return

        if p.val != q.val:
            self.is_same = False
            return

        self.isSameTree(p.left, q.left)
        self.isSameTree(p.right, q.right)

    def traverseTreeAndCheckSubtree(self, root, sub_root):
        if not root:
            return

        self.is_same = True
        self.isSameTree(root, sub_root)
        if self.is_same:
            self.contains_subtree = True
            return

        self.traverseTreeAndCheckSubtree(root.left, sub_root)
        self.traverseTreeAndCheckSubtree(root.right, sub_root)

