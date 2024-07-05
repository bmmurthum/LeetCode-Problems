""" Module to remove elements from list, if there are more than 2 of that value. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201
# Ignore unused variable. This is someone else's solution.
# pylint: disable=W0612


class Solution:
    """Problem given by LeetCode."""

    def remove_duplicates_3(self, nums: list[int]) -> int:
        """Someone else's solution."""
        total = len(nums)
        k = 0
        start = 2
        prev = -999999
        num_counter = 1
        index = 0
        for i in range(0, total):
            current = nums[i]
            if prev == current:
                num_counter += 1
            else:
                num_counter = 1
            if num_counter <= 2:
                nums[index] = nums[i]
                index += 1
            prev = current
        return index
