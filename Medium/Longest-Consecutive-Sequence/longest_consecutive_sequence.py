""" Module to find if there is two identical numbers near each other. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def longest_consecutive(self, nums: list[int]) -> int:
        """
        Finds the longest consecutive chain of values in an unordered list. O(n) time complexity.

        Args:
            `nums`: The list of numbers to look through.
        Returns:
            `max_length`: Max count of integers that are value neighbors.
        """

        # Set to allow for hash-table speed calls.
        num_set = set(nums)
        max_length = 0
        for start in nums:
            if start - 1 not in num_set:
                end = start + 1
                while end in num_set:
                    end += 1
                max_length = max(max_length, end - start)
        return max_length
