"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        """
        Given a list of daily temperatures, return a list of how many days from
        a current day you'd have to wait to have a higher temperature.

        Args:
            `temperatures`: A list of daily temperatures.
        Returns:
            `output`: The list of values.
        """

        # Build a monotonic stack with the temperatures and their index.
        output = [0] * len(temperatures)
        stack = [[temperatures[0], 0]]
        for day in range(1, len(temperatures)):
            temp = temperatures[day]
            if len(stack) == 0 or temp <= stack[-1][0]:
                stack.append([temp, day])
            else:
                while len(stack) > 0 and temp > stack[-1][0]:
                    output[stack[-1][1]] = day - stack[-1][1]
                    stack.pop()
                stack.append([temp, day])
        return output
