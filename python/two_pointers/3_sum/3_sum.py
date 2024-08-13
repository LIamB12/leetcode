class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        if len(nums) < 3:
            return []

        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue
            lp = index + 1
            rp = len(nums) - 1
            while lp < rp:
                summ = num + nums[lp] + nums[rp]
                if summ > 0:
                    rp -= 1
                elif summ < 0:
                    lp += 1
                else:
                    triplets.append([num, nums[lp], nums[rp]])
                    lp += 1
                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1
        return triplets

