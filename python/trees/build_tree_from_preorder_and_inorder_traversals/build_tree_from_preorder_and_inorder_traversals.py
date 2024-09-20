class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        inorder_pos = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:], inorder[:inorder_pos])
        root.right = self.buildTree(preorder[1 + inorder_pos:], inorder[inorder_pos + 1:])
        return root
