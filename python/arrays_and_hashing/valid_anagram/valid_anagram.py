class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_counts = {}
        t_char_counts = {}

        for c in s:
            if c in s_char_counts:
                s_char_counts[c] += 1
            else:
                s_char_counts[c] = 1

        for c in t:
            if c in t_char_counts:
                t_char_counts[c] += 1
            else:
                t_char_counts[c] = 1

        if len(s_char_counts) != len(t_char_counts):
            return False

        for c in s_char_counts:
            if t_char_counts.get(c, 0) != s_char_counts.get(c):
                return False
        return True


