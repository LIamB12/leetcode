class Solution:
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0
        self.heightOfBinaryTree(root)
        return self.max_diameter




    def heightOfBinaryTree(self, root):
        if not root:
            return 0

        left = self.heightOfBinaryTree(root.left)
        right = self.heightOfBinaryTree(root.right)

        self.max_diameter = max(self.max_diameter, left + right)

        return 1 + max(left, right)

