class Solution:
    def maxPathSum(self, root):
        self.max_sum = root.val
        self.find_math_path_sum(root)
        return self.max_sum

    def find_math_path_sum(self, root):
        if not root:
            return 0
        
        left_path_sum = max(self.find_math_path_sum(root.left), 0)
        right_path_sum = max(self.find_math_path_sum(root.right), 0)


        self.max_sum = max(self.max_sum, root.val + left_path_sum + right_path_sum)

        return root.val + max(left_path_sum, right_path_sum)
       
