class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = 0
        R = len(nums) - 1

        while L < R:

            M = (L + R) // 2
            val = nums[M]

            if val == target:
                return M

            if val < target:
                L = M + 1
            else:
                R = M - 1

        return -1


