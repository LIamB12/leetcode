class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff in visited_nums:
                return [visited_nums.get(diff), index]
            else:
                visited_nums[num] = index

        return -1

