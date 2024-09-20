class Solution:
    def isBalanced(self, root):
        self.balanced = True
        self.heightOfBinaryTree(root)
        return self.balanced

    def heightOfBinaryTree(self, root):
        if not root:
            return 0

        left = self.heightOfBinaryTree(root.left)
        right = self.heightOfBinaryTree(root.right)

        diff = abs(left - right)

        if diff > 1:
            self.balanced = False
            return 0
        
        return 1 + max(left, right)
