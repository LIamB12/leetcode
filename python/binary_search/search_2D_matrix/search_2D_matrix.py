class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search(nums, target):
            L = 0
            R = len(nums) - 1

            while L <= R:
                M = (L + R) // 2
                
                val = nums[M]

                if val == target:
                    return M
                elif val < target:
                    L = M + 1
                else:
                    R = M - 1

            return -1
        def bin_search_mtrx_first_col(mtrx, target):
            L = 0
            R = len(mtrx) - 1

            while L <= R:
                M = (L + R) // 2
                
                val = mtrx[M][0]

                if val == target:
                    return M
                elif val < target:
                    L = M + 1
                else:
                    R = M - 1

            return M

        
        row_index = bin_search_mtrx_first_col(matrix, target)
        print(row_index)
        if matrix[row_index][0] > target:
            row_index -= 1

        return bin_search(matrix[row_index], target) != -1  
