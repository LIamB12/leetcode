class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        
        lp = 0
        rp = len(heights) - 1

        while lp < rp:
            vol = min(heights[lp], heights[rp]) * (rp - lp)
            max_vol = max(vol, max_vol)

            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1

        return max_vol
