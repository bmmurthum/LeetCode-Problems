""" Module to find a group of ranges that cover all the integers in a list. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def summary_ranges(self, nums: list[int]) -> list[str]:
        """
        Generates a minimal list of ranges that cover the given integers.

        Args:
            `nums`: An ascending, sorted list.
        Returns:
            `range_list`: A list of strings that represent a group of ranges
                that contain the numbers in the list.
        """

        # Handle empty case
        if nums == []:
            return []

        # Build the list
        start = 0
        range_list = []
        for i, value in enumerate(nums[1:], 1):
            if value - nums[i - 1] > 1:
                range_list.append([nums[start], nums[i - 1]])
                start = i
        range_list.append([nums[start], nums[len(nums) - 1]])

        # Translate the list
        for i, r in enumerate(range_list):
            if r[0] == r[1]:
                range_list[i] = str(r[0])
            else:
                range_list[i] = f"{r[0]}->{r[1]}"
        return range_list
