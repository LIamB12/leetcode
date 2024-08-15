class Solution:
    def carFleet(self, target, position, speed):
        cars = zip(position, speed)

        cars = sorted(cars, key=lambda x: x[0], reverse=True)

        stack = []

        for car in cars:
            time_to_finish = (target - car[0]) / car[1]

            if not stack:
                stack.append(time_to_finish)
                continue

            if time_to_finish > stack[-1]:
                stack.append(time_to_finish)

        return len(stack)
