class Solution:
    def isSameTree(self, p, q):
        self.is_same = True
        self.traverseTwoBinaryTrees(p, q)
        return self.is_same

    def traverseTwoBinaryTrees(self, p, q):
        if not p and not q:
            return

        if not p:
            self.is_same = False
            return
        if not q:
            self.is_same = False
            return

        if p.val != q.val:
            self.is_same = False
            return

        self.traverseTwoBinaryTrees(p.left, q.left)
        self.traverseTwoBinaryTrees(p.right, q.right)




