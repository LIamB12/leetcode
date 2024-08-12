class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            chars_count = [0] * 26

            for c in s:
                alphabet_index = ord(c) - 97
                chars_count[alphabet_index] += 1

            chars_count = tuple(chars_count)
            if chars_count in anagram_map:
                anagram_map[chars_count].append(s)
            else:
                anagram_map[chars_count] = [s]

        return [anagram_map[key] for key in anagram_map]
