class Solution:
    def characterReplacement(self, s, k):
        p = 0
        current_char = s[0]
        first_non_matching = 0
        remaining_replacements = k
        max_length = 0
        current_length = 0

        while p < len(s):
            char = s[p]
            if char != current_char:
                if first_non_matching == 0:
                    first_non_matching = p

                if remaining_replacements == 0:
                    p = first_non_matching
                    current_char = s[p]
                    remaining_replacements = k
                    first_non_matching = 0
                    max_length = max(current_length, max_length)
                    current_length = 0
                    continue

                else:
                    remaining_replacements -= 1

            current_length += 1
            p += 1

        if remaining_replacements > 0:
            p = len(s) - current_length

            while p > 0:
                p -= 1
                char = s[p]

                if remaining_replacements == 0:
                    break
                else:
                    remaining_replacements -= 1

                current_length += 1
                p -= 1

        return max(current_length, max_length)


        
