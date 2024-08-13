class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        lp = 0
        rp = len(height) - 1
        total_vol = 0 
        
        while lp <= rp:
            if max_left < max_right:
                water = max(0, max_left - height[lp])
                total_vol += water
                max_left = max(max_left, height[lp])
                lp += 1
            else:
                water = max(0, max_right - height[rp])
                total_vol += water
                max_right = max(max_right, height[rp])
                rp -= 1
        
        return total_vol
