class Solution:
    def kthSmallest(self, root, k):
        self.inorder_arr = []
        self.traverseTreeAndBuildInorderArray(root, k)
        return self.inorder_arr[k-1]

    def traverseTreeAndBuildInorderArray(self, root, k):
        if not root:
            return
        
        self.traverseTreeAndBuildInorderArray(root.left, k)
        self.inorder_arr.append(root.value)
        if len(self.inorder_arr) == k:
            return
        self.traverseTreeAndBuildInorderArray(root.right, k)

