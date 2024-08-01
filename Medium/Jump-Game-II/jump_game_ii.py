""" Module to find the minimum jumping path to the end index. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201
# Ignore the advise to use enumerate()
# pylint: disable=C0200


class Solution:
    """Problem given by LeetCode."""

    def jump(self, nums: list[int]) -> int:
        """
        Returns the minimum number of "jumps" to get from the first index to
        the last if each value represents how far you can jump from the current
        value.

        Given lists are confirmed to have possibility of reaching the end.

        Args:
            `nums`: A list of distances jumpable.
        Return:
            `new_count`: The minimum number of jumps to reach the end.
        """

        # Handle single item case.
        if len(nums) == 1:
            return 0

        # A list of how many jumps to get to a position.
        jump_count = [None] * len(nums)
        jump_count[0] = 0

        # At any position declare the furthest points it can reach as reachable
        # in "current count" plus one jumps. If that is less than a number
        # previously recorded, overwrite.

        # If the ending range of a jump is the last index, we can stop search.
        for i in range(len(nums)):
            new_count = jump_count[i] + 1
            end_range = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, end_range + 1):
                if jump_count[j] is None or new_count < jump_count[j]:
                    jump_count[j] = new_count
            if end_range == len(nums) - 1:
                return new_count
