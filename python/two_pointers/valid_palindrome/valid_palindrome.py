class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1
        s = s.lower()
        alpha_numeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        alpha_numeric = set(alpha_numeric)

        while lp < rp:
            if s[lp] not in alpha_numeric:
                lp += 1
                continue
            if s[rp] not in alpha_numeric:
                rp -= 1
                continue
            
            if s[lp] != s[rp]:
                return False

            lp += 1
            rp -= 1

        return True

