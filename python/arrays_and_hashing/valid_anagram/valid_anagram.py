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
        
        larger_map = s_char_counts if len(s_char_counts) > len(t_char_counts) else t_char_counts
        shorter_map = t_char_counts if len(s_char_counts) > len(t_char_counts) else s_char_counts

        for c in larger_map:
            if shorter_map.get(c, 0) != larger_map.get(c):
                return False
        return True


