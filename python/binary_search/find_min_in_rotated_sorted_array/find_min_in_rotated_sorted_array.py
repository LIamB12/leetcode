class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1 
        base = nums[0]

        min_num = base
        
        while l <= r:

            m = (l + r) // 2

            if nums[m] >= base:
                l = m + 1
            else:
                r = m - 1
                min_num = min(min_num, nums[m])

        return min_num


