class Solution:
    def findDuplicate(self, nums):
        fast, slow = 0, 0
        
        while fast == 0 or fast != slow:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]

        start = 0
        while start != slow:
            start = nums[start]
            slow = nums[slow]

        return nums[start]
