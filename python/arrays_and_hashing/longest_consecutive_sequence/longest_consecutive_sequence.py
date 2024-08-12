class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_sequence = 0

        for num in nums:
            if num - 1 in nums:
                continue

            sequence_length = 1
            while num + 1 in nums:
                sequence_length += 1
                num += 1
            longest_sequence = max(longest_sequence, sequence_length)

        return longest_sequence


