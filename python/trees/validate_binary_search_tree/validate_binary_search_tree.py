class Solution:
    def isValidBST(self, root):
        self.is_valid = True
        self.validateBST(root, float("-inf"), float("inf"))
        return self.is_valid

    def validateBST(self, root, left, right):
        if not root:
            return

        if not (root.val < right and root.val > left):
            self.is_valid = False
            return

        self.validateBST(root.left, left, root.val)
        self.validateBST(root.right, root.val, right)

