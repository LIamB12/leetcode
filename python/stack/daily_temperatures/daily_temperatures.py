class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days_until_warmer = [0] * len(temperatures)

        for index, elem in enumerate(temperatures):

            while stack and elem > stack[-1][0]:
                days_until_warmer[stack[-1][1]] = index - stack[-1][1]
                stack.pop()

            stack.append((elem, index))

        return days_until_warmer
