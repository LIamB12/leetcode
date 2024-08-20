import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        min_k = r

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)

            if hours > h:
                l = m + 1
                continue

            min_k = min(m, min_k)

            r = m - 1

        return min_k
