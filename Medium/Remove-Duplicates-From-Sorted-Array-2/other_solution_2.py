""" Module to remove elements from list, if there are more than 2 of that value. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def remove_duplicates_2(self, nums: list[int]) -> int:
        """Someone else's solution."""
        to_be_inserted_idx = 0
        is_twice = False
        prev = -987654321
        k = 0
        for _, v in enumerate(nums):
            if v == prev:
                if is_twice:
                    continue
                elif not is_twice:
                    k += 1
                    is_twice = True
                    nums[to_be_inserted_idx] = v
                    to_be_inserted_idx += 1
            else:
                k += 1
                is_twice = False
                nums[to_be_inserted_idx] = v
                to_be_inserted_idx += 1
                prev = v
        return k
