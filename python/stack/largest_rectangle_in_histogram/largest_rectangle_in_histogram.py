class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        for index, h in enumerate(heights):
            if not stack:
                stack.append((h, 0))
                continue
            h_start_index = index
            while stack and h < stack[-1][0]:
                current_rect = stack.pop()
                area = current_rect[0] * (index - current_rect[1])
                max_area = max(max_area, area)
                h_start_index = current_rect[1]
            
            stack.append((h, h_start_index))

        while stack:
            current_rect = stack.pop()
            area = current_rect[0] * (len(heights) - current_rect[1])
            max_area = max(max_area, area)
        return max_area
