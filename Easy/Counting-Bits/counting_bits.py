"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def count_bits(self, n: int) -> list[int]:
        """
        Build a list that contains the number of 1s in the binary
        representations from 0 -> n.

        Args:
            `n`: The ending number.
        Returns:
            `output`: The list of values.
        """

        # Edge-case: First two numbers
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        # Go forward building on last known values.
        output = [0, 1]
        last = 1
        for i in range(2, n + 1):
            if i >= last * 2:
                last = last * 2
            output.append(output[i - last] + 1)
        return output
