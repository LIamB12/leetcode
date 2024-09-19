class Solution:
    def lengthOfLongestSubstring(self, s):
        p = 0
        seen = {}
        max_length = 0

        while p < len(s):
            char = s[p]
            if char in seen:
                max_length = max(max_length, len(seen))
                p = seen.get(char) + 1
                seen = {}

            else:
                seen[char] = p
                p += 1 

        return max(len(seen), max_length)
