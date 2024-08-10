class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_frequencies = {}
        frequencies_buckets = [[] for _ in range(len(nums) + 1)]
        top_k_frequent_nums = []

        for num in nums:
            if num in number_frequencies:
                number_frequencies[num] += 1
            else:
                number_frequencies[num] = 1

        for num in number_frequencies:
            count = number_frequencies.get(num)
            frequencies_buckets[count].append(num)

        for arr in frequencies_buckets[::-1]:
            for num in arr:
                top_k_frequent_nums.append(num)
                k -= 1
                if k == 0:
                    return top_k_frequent_nums



